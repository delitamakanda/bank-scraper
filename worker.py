import os
import sys
from celery import Celery
from celery.utils.log import get_task_logger

celery_log = get_task_logger(__name__)

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
celery.conf.result_backend = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')


@celery.task(name='create_task')
def create_task(account_number, secret_code, source, headless):
    # display log
    celery_log.info(
        'create_task: account_number=%s, secret_code=%s, source=%s, headless=%s' % (
            account_number, secret_code, source, headless
        )
    )
    # run scraper
    os.system('python3 scrapers/scraper.py %s %s %s %s' % (account_number, secret_code, source, headless))
