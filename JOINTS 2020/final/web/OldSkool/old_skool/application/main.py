from flask import Flask, render_template, session, make_response, \
	request, Response, redirect, url_for, flash, current_app as app, Blueprint
from flask_generic_views import TemplateView, MethodView
from flask_login import login_required, current_user
import urllib.parse
import random, time
import os
from .utils import CurhatForm, ProfileForm
from .models import Curhat, User, db
from datetime import datetime as dt
from multidict import MultiDict
import json
import re

main = Blueprint('main', __name__)


class HomeView(TemplateView):
	template_name = "index.html"

	def get(self):
		return render_template(self.template_name)

class ProfileView(TemplateView):
	template_name = "profile.html"
	decorators = [login_required]

	def get(self):
		user_dict = MultiDict(username=current_user.username,bio=current_user.bio,motto=current_user.motto)
		form = ProfileForm(user_dict)
		return render_template(self.template_name, form=form, motto=current_user.motto)

	def post(self):
		raw_body = request.stream.read()
		json_body = json.loads(raw_body)
		validate_form = MultiDict(bio=json_body["bio"], motto=json_body["motto"], username=current_user.username)
		validate_form = ProfileForm(validate_form)
		if validate_form:
			user = User.query.filter(User.id == current_user.id).one()
			user.bio = json_body["bio"]
			filtered_motto = re.sub(r"script|SCRIPT|get|post|POST|ajax|put|PUT", "", json_body["motto"])
			user.motto = filtered_motto
			db.session.commit()
			flash("Berhasil edit profile")
		else:
			flash("Gagal edit profile", "danger")

		return redirect(url_for("profile"))


class ReportView(TemplateView):
	decorators = [login_required]

	def post(self):
		url_link = request.form.get("curhat_link")
		if url_link.startswith("http"):
			os.system("node visit.js {}".format(url_link.encode("utf-8").hex()))
			return "Report Success"
		else:
			return "Report Fail, Something Wrong With The Link"


class CurhatView(TemplateView):
	template_name = "curhat.html"
	single_curhat_template = "single_curhat.html"
	decorators = [login_required]

	def get(self, curhat_id=None):
		if curhat_id is None:
			form = CurhatForm()
			curhatan_list = Curhat.query.order_by(Curhat.created.desc()).limit(50).all()
			return render_template(self.template_name, form=form, curhatan_list=curhatan_list)
		else:
			single_curhat = Curhat.query.filter(Curhat.id == curhat_id).one()
			
			if single_curhat:
				return render_template(self.single_curhat_template, curhat=single_curhat)
			else:
				return render_template("errors/404.html", error="Curhatnya gaada"), 404

	def post(self):
		form = CurhatForm(request.form)

		if form.validate():
			body = form.body.data
			new_curhat = Curhat(
							body=body,
							created=dt.now(),
							user_id=current_user.id)
			db.session.add(new_curhat)
			db.session.commit()
			flash("Curhat Berhasil Ditambahkan", "success")
			return redirect("/curhat")
		else:
			return render_template(self.template_name, form=form)




app.add_url_rule('/', view_func=HomeView.as_view('index'))
app.add_url_rule('/curhat', defaults={'curhat_id': None},
								 view_func=CurhatView.as_view('all_curhat'), methods=['GET'])
app.add_url_rule('/curhat', view_func=CurhatView.as_view('curhat_create'), methods=['POST'])
app.add_url_rule('/curhat/<int:curhat_id>', view_func=CurhatView.as_view('single_curhat_view'),
								 methods=['GET']) 

app.add_url_rule('/profile', view_func=ProfileView.as_view('profile'))
app.add_url_rule('/profile', view_func=ProfileView.as_view('edit_profile'), methods=['POST'])
app.add_url_rule('/report', view_func=ReportView.as_view('report'), methods=['POST'])

