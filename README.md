# Redis Pubsub Over Docker
A simple Redis PubSub client/server bsaed on docker
the project creates 3 containers:
* Redis server
* Publisher ( python )
* subscriber ( python )

the messages are passed through redis.


how to run:

docker-compose -f dev.yml up

Ctrl+C to break.
