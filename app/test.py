import time
from tasks import add
# celery -A tasks worker -c 4 --loglevel=info


t1 = time.time()
result = add.delay(1, 2)
print(result.get())
 
print(time.time() - t1)
