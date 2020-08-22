from flask import Flask, render_template, session, make_response, \
	request, Response, redirect, url_for, flash, current_app as app, Blueprint
from flask_generic_views import TemplateView, MethodView
from flask_login import login_required, current_user
import urllib.parse
import random, time
import os
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
		return render_template(self.template_name)

class FeedbackView(TemplateView):
	template_name = "feedback.html"
	decorators = [login_required]

	def get(self):
		return render_template(self.template_name)

	def post(self):
		url = request.form["feedback"]
		os.system("node visit.js '{}'".format(url.encode("utf-8").hex()))
		flash("Okay, we will check that link !", "success")
		return redirect(url_for("index"))

class NotesView(TemplateView):
	decorators = [login_required]

	def get(self):
		# Iseng aja bikin vuln
		feed_url = request.url.split("/notes")[1]
		filtered_url = re.sub(r"script|SCRIPT|get|post|POST|ajax|put|PUT", "", feed_url)
		rendered = render_template("bruh.html", feed_url=request.host_url[:-1]+urllib.parse.unquote(filtered_url))
		resp = make_response(rendered)
		resp.status_code = 200
		resp.headers["Content-Length"] = len(rendered)											
		return resp


class FlagView(TemplateView):
	decorators = [login_required]
	template_name = "FL4GGG.html"

	def get(self):
		if current_user.admin:
			return render_template(self.template_name)
		else:
			flash("Bruh, Please Don't Even Try You Low Tier Account", "danger")
			return redirect(url_for("index"))


app.add_url_rule('/', view_func=HomeView.as_view('index'))
app.add_url_rule('/profile', view_func=ProfileView.as_view('profile'))
app.add_url_rule('/feedback', view_func=FeedbackView.as_view('feedback'))
app.add_url_rule('/notes/', view_func=NotesView.as_view('notes'), strict_slashes=False)
app.add_url_rule('/flag', view_func=FlagView.as_view('flag'))
