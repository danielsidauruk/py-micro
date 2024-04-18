from flask import Flask, render_template, request
import redis
import os

app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_client = redis.StrictRedis(host=redis_host, port=6379, db=0)
channel_name = 'messages'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    redis_client.publish(channel_name, message)
    return 'Message sent successfully', 204

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

