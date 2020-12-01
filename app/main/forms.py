from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category = SelectField('Category', choices=[('Language','Language'),('Family','Family'),('Education','Education'),('Friends','Friends'),('Favorite','Favorite')],validators =[Required()])
    pitch = TextAreaField('Your Pitch....', validators=[Required()])
    submit = SubmitField('Save')

class CommentForm(FlaskForm):
    comment = TextAreaField('Your Comment....',validators=[Required()])
    submit = SubmitField('Comment')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Share with us about you...',validators = [Required()])
    submit = SubmitField('Submit')