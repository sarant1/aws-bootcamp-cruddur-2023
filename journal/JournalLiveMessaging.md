# Adding real time messaging socket io

## Flask - SocketIO

First I had to install flask-socketio

```bash
pip install flask-socketio
```

After some research I found out that the default Werkzeug server for flask does not support websockets so I set up flask to use eventlet as recommended in the docs.

```bash
pip install eventlet
```

I initialized socket io like so

```python
socketio = SocketIO(app, cors_allowed_origins=['*', 'http://localhost:3000'], pingTimeout=60000)

# This is how initialize the app so that that it can run websockets
if __name__ == "__main__":
  socketio.run(app, debug=True, host='0.0.0.0', port=4567)

```

And then in my docker file I fixed it so that it does not use flask run which would default to Werkzeug

```docker
FROM 049843000081.dkr.ecr.us-east-1.amazonaws.com/cruddur-python:3.10-slim-buster

WORKDIR /backend-flask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# ENV PYTHONBUFFERED=1

EXPOSE ${PORT}


# Notice how I am running the app now
CMD ["python3", "app.py"]

# This is how we normally ran the app 
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567", "--debug"]
```


## The Code

In my backend app.py I set up a websocket to accept a message from the front end

```py
@socketio.on('new message')
def new_message(data):

    recieved_message = {
        'display_name': data['display_name'],
        'message': data['message'],
        'handle': data['handle'],
        'key': generate_random_string(10),
        'created_at': 'now'
    }
    socketio.emit('new message', recieved_message, to=data['room'], include_self=False)
```

I also set up rooms that when a user loaded a specific message group, that is the room they join so that only they recieve messages from eacother.

```py
# Joining a room
@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    print(f"User {username} has joined room {room}", flush=True)
    socketio.send(username + ' has entered the room.', to=room)
```

In the frontend I set up the request for a websocket in the MEssageGroupPage.js so that once a user clicks on a message group, it will initiate the websocket handshake.

```js
// var socket has to be defined outside component to be passed to child components.  
var socket;


React.useEffect( () => {
    checkAuth(setUser)
    socket = io(`${process.env.REACT_APP_BACKEND_URL}`)
    socket.on('connect',  () => {
      console.log("Connected to websocket server")

      socket.on('new message', (data) => {
        console.log('new message:',data)
        setMessages(current => [...current, data])
      })
    })
  // empty brackets means this will run once when component is loaded
  }, [])

```

I also passed the socket variable to the MessageForm so that once a message is sent, it can emit a message to the server.

```js
// We must do checkAuth before sending message so the user is set
    await checkAuth(props.setUser)
    .then(() => {
      const socket_message_data = {
        "display_name": props.user.display_name,
        "handle": props.user.handle,
        "message": message,
        "room": params.message_group_uuid
      }
      props.socket.emit('new message', socket_message_data)
    })
```