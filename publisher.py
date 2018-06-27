import logging
import redis
import time
import json
import requests
logger = logging.getLogger("publisher")

queue = redis.StrictRedis(host='redis', port=6379, db=0)
channel = queue.pubsub()

time.sleep(40)
while 1:
    # print "sending: test" + str(i)
    # print requests.get("http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1").json()[
    #     0]['content']
    try:
        queue.publish("my-test-redis-channel", json.dumps({"quote":
                                                               requests.get(
                                                                   "http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1").json()[
                                                                   0]['content']}))
    except:
        pass # don't care
    time.sleep(1)
