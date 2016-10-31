import logging
import redis
import time
import json
logger = logging.getLogger("publisher")

queue = redis.StrictRedis(host='redis', port=6379, db=0)
channel = queue.pubsub()

for i in range(20):
    print "sending: test" + str(i)
    queue.publish("my-test-redis-channel", json.dumps({"my": "object", "count": i}))
    time.sleep(1)
