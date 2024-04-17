from flask import Flask, render_template, Response
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
channel_name = 'messages'

@app.route('/')
def index():
    return render_template('index.html')

def stream_messages():
    pubsub = redis_client.pubsub()
    pubsub.subscribe(channel_name)
    for message in pubsub.listen():
        if message['type'] == 'message':
            yield f"data: {message['data'].decode('utf-8')}\n\n"

@app.route('/messages')
def messages():
    return Response(stream_messages(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
