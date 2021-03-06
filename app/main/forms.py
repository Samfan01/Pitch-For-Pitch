from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required


class PitchForm(FlaskForm):
    category = SelectField('Choose Category', choices = [('Social','Social'),('Business','Business'),('Spiritual','Spiritual'),('Pick_Up_Lines','Pick_Up_Lines'),('Motivational','Motivational'),('Mood_lifting','Mood_lifting')]) 
    pitch = TextAreaField('Personal Pitch',validators=[Required()])
    author = StringField('Pitch Author',validators=[Required()])
    
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    
class LeaveComment(FlaskForm):
    comment = TextAreaField('Write your comment here.',validators = [Required()])
    submit = SubmitField('Submit')