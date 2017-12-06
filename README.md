# celery-with-docker-compose
run celery 4.1 worker and rabbitmq with docker-compose v3

sovle the problem:

celeryworker_1  | [2017-12-06 08:55:43,666: ERROR/MainProcess] consumer: Cannot connect to amqp://guest:**@127.0.0.1:5672//: [Errno 104] Connection reset by peer.
celeryworker_1  | Trying again in 4.00 seconds...



create celery with host IP instead of "localhost" or "rabbitmq's hostname" in docker-compose.yml


```
from celery import Celery

#celery worker in docker-compose  cant connect to "localhost" or "hostname" in dockercompose.yml

#app = Celery(backend='amqp', broker='amqp://guest:guest@localhost:5672/')


HOST_IP = '192.168.239.129' # ip of host(run docker-compose) 
app = Celery(backend = 'rpc://', broker = 'amqp://guest:guest@{0}:5672/'.format(HOST_IP))

#app = Celery(backend='amqp', broker='amqp://guest:guest@localhost:5672/')
# app = Celery('tasks', backend = 'amqp', broker = 'pyamqp://guest:guest@localhost//')


@app.task
def add(x, y):
    return x + y
```

rabbitmq_1      | connection <0.570.0> (172.21.0.1:58434 -> 172.21.0.3:5672): user 'guest' authenticated and granted access to vhost '/'
celeryworker_1  | [2017-12-06 08:55:48,799: INFO/MainProcess] mingle: all alone
celeryworker_1  | [2017-12-06 08:55:48,856: INFO/MainProcess] celery@4a0fc24604d0 ready.



test.py  can run both in host or in docker container:

cd ./app
python3 test.py

