from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()

def create_app():
	app = Flask(__name__, instance_relative_config=False)
	app.config.from_object('config.Config')
	db.init_app(app)
	login_manager = LoginManager()
	login_manager.login_view = 'login'
	login_manager.init_app(app)

	from .models import User

	@login_manager.user_loader
	def load_user(user_id):
		# since the user_id is just the primary key of our user table, use it in the query for the user
		return User.query.get(int(user_id))

	with app.app_context():
		# blueprint for auth routes in our app
		from .auth import auth as auth_blueprint
		app.register_blueprint(auth_blueprint)

		# blueprint for non-auth parts of app
		from .main import main as main_blueprint
		app.register_blueprint(main_blueprint)
		
		db.create_all()

		return app