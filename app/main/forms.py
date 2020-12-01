from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category = SelectField('Category', choices=[('language','language'),('family','family'),('education','education'),('friends','friends'),('favorite','favorite')],validators =[Required()])
    pitch = TextAreaField('Your Pitch....', validators=[Required()])
    submit = SubmitField('Save')

class CommentForm(FlaskForm):
    comment = TextAreaField('Your Comment....',validators=[Required()])
    submit = SubmitField('Comment')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Share with us about you...',validators = [Required()])
    submit = SubmitField('Submit')