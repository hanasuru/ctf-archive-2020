from flask import Flask, render_template, session, make_response, \
	request, Response, redirect, url_for, flash, current_app as app, Blueprint
from flask_generic_views import TemplateView, MethodView
from flask_login import login_required, current_user
import urllib.parse
import random, time
import os
import re
import requests
from .models import Writeup, db

main = Blueprint('main', __name__)


class HomeView(TemplateView):
	template_name = "index.html"

	def get(self):
		return render_template(self.template_name)

class ProfileView(TemplateView):
	template_name = "profile.html"
	decorators = [login_required]

	def get(self):
		return render_template(self.template_name)

class SubmitView(TemplateView):
	template_name = "submit.html"
	decorators = [login_required]

	def get(self):
		return render_template(self.template_name)

	def post(self):
		url = request.form["writeup"]
		try:
			resp_url = requests.get(url).text
		except:
			resp_url = "Test123"
		check = re.findall(r"<title.*>(.*?)</title>", resp_url)
		if check:
			new_wu = Writeup(
				url=url,
				title=check[0]
			)
			db.session.add(new_wu)
			db.session.commit()

		os.system("node visit.js '{}'".format(url.encode("utf-8").hex()))
		flash("Nice, let us check the writeup", "success")
		return redirect(url_for("index"))

class WriteupView(TemplateView):
	template_name = "writeup.html"
	decorators = [login_required]

	def get(self):
		writeup_list = Writeup.query.order_by(Writeup.id.desc()).limit(25).all()
		return render_template(self.template_name, writeups=writeup_list)


class FlagView(TemplateView):
	decorators = [login_required]
	template_name = "FL4GGG.html"

	def get(self):
		# wkwk yang penting bisa crlf 
		fake_flag = "{%s}" % os.urandom(16).hex()
		final_resp = make_response(render_template(self.template_name, fake_flag=fake_flag))
		if request.args.get("user"):
			init_header = "X-Client-Id嘺" + request.args.get("user")[:150]
			normalize_header = ""
			for kar in init_header:
				if ord(kar) > 127:
					normalize_header += chr(ord(kar) & 127)
				else:
					normalize_header += urllib.parse.quote(kar)
			final_header = normalize_header.split("\r\n")
			for data in final_header:
				if not data:
					continue
				per_line = data.find(":")
				value = data[per_line+1:]
				if per_line != -1:
					final_resp.headers[data[:per_line]] = value
				else:
					final_resp.headers["X"] = value
		return final_resp




app.add_url_rule('/', view_func=HomeView.as_view('index'))
app.add_url_rule('/profile', view_func=ProfileView.as_view('profile'))
app.add_url_rule('/submit', view_func=SubmitView.as_view('submit'))
app.add_url_rule('/writeup', view_func=WriteupView.as_view('writeup'))
app.add_url_rule('/flag', view_func=FlagView.as_view('flag'))
