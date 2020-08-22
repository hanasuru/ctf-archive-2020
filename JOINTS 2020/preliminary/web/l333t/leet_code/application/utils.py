from wtforms import Form, StringField, PasswordField, validators

class RegisterForm(Form):
	username = StringField('Username',[validators.Length(min=3,max=30,message="Name length min 3 max 30"),
													validators.DataRequired(message="This section is required"),
													validators.Regexp(r"^[a-zA-Z0-9_?!:)(-]*$",message="Only alnum and ?!_:)(- are allowed")])
	password = PasswordField('Password',[validators.Length(min=3,max=30,message="Password length min 3 max 30"),
													validators.DataRequired(message="This section is required"),
													validators.Regexp(r"^[a-zA-Z0-9_?!:)(-]*$",message="Only alnum and ?!_:)(- are allowed")])
	bio = StringField('Bio',[validators.length(min=3,max=100,message="Bio length min 3 max 100"),
												validators.DataRequired(message="This section is required")])
