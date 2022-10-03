import os

from celery import Celery
from celery.utils.log import get_task_logger

celery_log = get_task_logger(__name__)

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379')
celery.conf.result_backend = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')


@celery.task(name='create_task')
def create_task(account_number, secret_code):
    # display log
    celery_log.info(f"Connect to account {account_number} with secret code {secret_code}")
