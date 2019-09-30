from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio
import json
from .watson import getTones
import os


@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    join_room(room)
    chat_file = f'app/chats/{room}.json'
    if (os.path.isfile(chat_file)):
        with open(chat_file, 'r') as json_file:
            data = json.load(json_file)
            emit('status', data, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    tone = getTones({"text": message['msg']})
    print('THESE ARE THE TONES:', tone, '\n')
    chat_file = f'app/chats/{room}.json'

    writeToJSON(chat_file, session, tone, message, load_file=os.path.isfile(chat_file))
    print(tone)
    if len(tone['document_tone']['tones']) > 0:
        emit('message', {'usr': session.get('name'),
                        'msg' : message['msg'], 'score':f"Overall Tone: {tone['document_tone']['tones'][0]['tone_name']} | Score: {tone['document_tone']['tones'][0]['score']}"}, room=room)
    else:
        emit('message', {'usr': session.get('name'),
                        'msg' : message['msg'], 'score':f"Not enough information"}, room=room)

def writeToJSON(chat_file, session, tone, message, load_file):
    oc = 'r+' if load_file else 'w'
    with open(chat_file, oc) as outfile:
        data = {}
        msg = {
            "usr": session.get("name"),
            "msg": message['msg'],
            "tones": tone
            }
        if load_file:
            data = json.load(outfile)
            print("LOAD FILE", data)
            data['chat'].append(msg)
            outfile.seek(0)
        else:
            data['chat'] = [msg]
        print('XXXXXX',data)
        json.dump(data, outfile)
            


@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') +
                    ' has left the room.'}, room=room)
