from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm
from .watson import getTones
from flask import jsonify

@main.route('/', methods=['GET', 'POST'])
def index():
    """Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('index.html', form=form)

@main.route('/join', methods = ['POST'])
def join():
    """Join form to enter a room."""
    session['name'] = request.form.get('name')
    session['room'] = request.form.get('room')
    return redirect(url_for('.chat'))


@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('name', '')
    room = session.get('room', '')
    return render_template('chat.html', name=name, room=room)

@main.route('/tone', methods = ['POST'])
def tones():
    data = request.form
    sent = False if int(data.get('sentence')) == 0 else True
    tones = getTones({'text':data.get('text')}, sent)
    return jsonify(tones)

@main.route('/big-picture')
def bigpicture():
    return render_template('big-picture.html')

@main.route('/sean')
def sean():
    return render_template('sean.html')