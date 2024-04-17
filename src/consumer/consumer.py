import redis

# Connect to Redis
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

# Channel name
channel_name = 'messages'


def main():
    pubsub = redis_client.pubsub()
    pubsub.subscribe(channel_name)

    print(f"Listening for messages on channel '{channel_name}'...")

    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Received message: {message['data'].decode('utf-8')}")


if __name__ == "__main__":
    main()
