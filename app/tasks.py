from celery import Celery


#celery worker in docker-compose  cant connect to "localhost" or "hostname" in dockercompose.yml

#app = Celery(backend='amqp', broker='amqp://guest:guest@localhost:5672/')


# can work both from docker container or host
# HOST_IP = '192.168.239.129' # ip of host(run docker-compose) 
# app = Celery(backend = 'rpc://', broker = 'amqp://taiga:taiga@{0}:5672/'.format(HOST_IP))

# SERVICE_NAME is not the SERVICE's hostname
#  can work in docker but not work_from host
SERVICE_NAME = 'myrabbit' 
app = Celery(backend = 'rpc://', broker = 'amqp://taiga:taiga@{0}:5672/'.format(SERVICE_NAME))



@app.task
def add(x, y):
    return x + y
