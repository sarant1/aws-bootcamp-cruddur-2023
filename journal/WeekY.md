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