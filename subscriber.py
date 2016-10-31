import logging
import redis
import json
logger = logging.getLogger("subscriber")

r = redis.StrictRedis(host='redis', port=6379, db=0)
p = r.pubsub()
p.subscribe('my-test-redis-channel')

while True:
    for m in p.listen():
        if isinstance(m['data'], str):
            m['data'] = json.loads(m['data'])
        print m
        logger.info(m)
