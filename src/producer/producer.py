import redis

# Connect to Redis
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

# Channel name
channel_name = 'messages'


def main():
    while True:
        message = input("Enter a message (or type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        redis_client.publish(channel_name, message)


if __name__ == "__main__":
    main()
