from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Pitch,User
from .forms import PitchForm,UpdateProfile
from flask_login import login_required,current_user
from .. import db,photos





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
    pitches = Pitch.get_pitches(category)
    
    return render_template('pitch.html',pitches = pitches)

@main.route('/pitch/new/<category>', methods = ['GET','POST'])
@login_required
def new_pitch(category):
    form = PitchForm()
    
    if form.validate_on_submit():
        pitch = form.pitch.data
        author = form.author.data 
        category = form.category.data
        
        new_pitch = Pitch(category=category,pitch=pitch,author=author,user=current_user)
        
        new_pitch.save_pitch()
        return redirect(url_for('.pitch',category = category))
    
    return render_template('new_pitch.html',pitch_form = form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    
    if user is None:
        abort(404)
        
    return render_template('profile/profile.html',user = user)

@main.route('/user/<uname>/update',methods =['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
        
    form = UpdateProfile()
    
    if form.validate_on_submit():
        user.bio = form.bio.data
        
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('.profile',uname=user.username))
    
    return render_template('profile/update.html',form = form)

@main.route('/user/<uname>/update/pic',methods = ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname = uname))

@main.route('/business/category')
def business():
    
    pitch = Pitch.query.filter_by(category = 'business').all()
    
    return render_template('business.html',pitches = pitch)
    