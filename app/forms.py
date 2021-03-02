from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class PitchForm(FlaskForm):
    pitch_category = StringField('Pitch Category',validators=[Required()])
    pitch = TextAreaField('Personal Pitch',validators=[Required()])
    author = StringField('Pitch Author',validators=[Required()])
    
    submit = SubmitField('Submit')
    