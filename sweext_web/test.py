from celery import Celery
import requests

app = Celery('test', broker='pyamqp://guest@192.168.1.75//')

offset = 0


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(5.0, you.s('hello'), name='add every 10')


@app.task
def you(arg):
    get_msg_url = 'https://api.telegram.org/bot553736396:AAGb5lQsi4dcqcMU97JAOWpUE7F_oPjlTyE/getUpdates'
    response = requests.get(get_msg_url)
    print(response.json())
