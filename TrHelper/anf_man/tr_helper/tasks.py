from celery import shared_task
from .toolbox import FlowListener, Manager


@shared_task
def check_if_new():
    listener = FlowListener()
    listener.start()

@shared_task
def clear_log():
    #at 5 a.m every day delete all except today or last 3
    pass

@shared_task
def check_user_add(url):
    return Manager.manual_check(url)
