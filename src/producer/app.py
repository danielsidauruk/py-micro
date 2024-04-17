from flask import Flask, render_template, request
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
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
    app.run(debug=True, port=5001)
