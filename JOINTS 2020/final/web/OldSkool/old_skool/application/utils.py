from wtforms import Form, StringField, PasswordField, validators, TextAreaField

class RegisterForm(Form):
	username = StringField('Username',[validators.Length(min=3,max=30,message="Name length min 3 max 30"),
													validators.DataRequired(message="This section is required"),
													validators.Regexp(r"^[a-zA-Z0-9_?!:)(-]*$",message="Only alnum and ?!_:)(- are allowed")])
	password = PasswordField('Password',[validators.Length(min=3,max=30,message="Password length min 3 max 30"),
													validators.DataRequired(message="This section is required"),
													validators.Regexp(r"^[a-zA-Z0-9_?!:)(-]*$",message="Only alnum and ?!_:)(- are allowed")])
	motto = StringField('Motto',[validators.length(min=0,max=130,message="Motto max 130")])
	bio = StringField('Bio',[validators.length(min=0,max=130,message="Bio max 130")])

class CurhatForm(Form):
	body = TextAreaField('Isi Curhat',[validators.Length(min=1,max=130,message="Body length min 1 max 130"),
												validators.DataRequired(message="This section is required")])

class ProfileForm(Form):
	username = StringField('Username (Gabisa Diganti)',[validators.length(min=0,max=30,message="")])
	motto = StringField('Motto',[validators.length(min=0,max=130,message="Motto max 130")])
	bio = StringField('Bio',[validators.length(min=0,max=130,message="Bio max 130")])

