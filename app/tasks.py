from celery import Celery


#celery worker in docker-compose  cant connect to "localhost" or "hostname" in dockercompose.yml

#app = Celery(backend='amqp', broker='amqp://guest:guest@localhost:5672/')


HOST_IP = '192.168.239.129' # ip of host(run docker-compose) 
app = Celery(backend = 'rpc://', broker = 'amqp://taiga:taiga@{0}:5672/'.format(HOST_IP))

# cant work from docker
# HOST_NAME = 'rabbit-taiga' 
# app = Celery(backend = 'rpc://', broker = 'amqp://taiga:taiga@{0}:5672/'.format(HOST_NAME))


#app = Celery(backend='amqp', broker='amqp://guest:guest@localhost:5672/')
# app = Celery('tasks', backend = 'amqp', broker = 'pyamqp://guest:guest@localhost//')


@app.task
def add(x, y):
    return x + y
