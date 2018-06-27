import requests
import json

import time

data = {
    "query": {
        "query_string":
            {
                "query": "logstash*"
            }
    }
}
while 1:
    print requests.post('http://192.168.99.100:9200/_search',
                        data=json.dumps(data)).json()['hits']['total']
    for l in requests.post('http://192.168.99.100:9200/_search',
                        data=json.dumps(data)).json()['hits']['hits']:
        print l
    time.sleep(2)


# {u'_score': 2.4790761, u'_type': u'logstash', u'_id': u'AVi5zpFZjeS9SyqAobz7', u'_source': {u'tags': [], u'@version': u'1', u'@timestamp': u'2016-12-01T09:54:31.552Z', u'level': u'INFO', u'host': u'9aae2ddaeb62', u'logger_name': u'subscriber', u'path': u'subscriber.py', u'message': u'logstash- wtf!', u'type': u'logstash'}, u'_index': u'logstash-2016.12.01'}