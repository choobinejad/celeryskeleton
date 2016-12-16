from celery import Celery
import time
import random

app = Celery('tasks')
app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.result_backend = 'redis://localhost:6379/0'

@app.task
def adding(x, y):
    time.sleep(random.randint(1,3))
    return x + y

@app.task
def multiplying(x, y):
    time.sleep(random.randint(1,3))
    for n in range(random.randint(1,10)):
        x = x*x
        return x * y