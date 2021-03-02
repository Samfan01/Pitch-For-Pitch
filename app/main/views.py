from flask import render_template
from . import main
from ..models import Pitch
from ..forms import PitchForm
from flask_login import login_required





#Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page
    and its data
    '''
    title = 'Welcome to the first ever Pitch 4 Pitch app!'
    return render_template('index.html',title = title)

@main.route('/pitch/<category>')
def pitch(category):
    '''
    View pitch page function that returns the pitches and the data
    '''
    pitches = Pitch.get_pitches()
    
    return render_template('pitch.html',pitches = pitches)

@main.route('/pitch/new/<category>', methods = ['GET','POST'])
@login_required
def new_pitch(category):
    form = PitchForm()
    
    if form.validate_on_submit():
        pitch = form.pitch.data
        author = form.author.data
        category = form.category.data
        new_pitch = Pitch(pitch,author,category)
        
        new_pitch.save_pitch()
        #return redirect(url_for('pitch',category = pitch.category))
    
    return render_template('new_pitch.html',pitch_form = form)
