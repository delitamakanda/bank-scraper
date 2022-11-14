from celery.result import AsyncResult
from fastapi import Body, FastAPI, Form, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from worker import create_task

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.post('/connect', status_code=200)
def run_task(payload = Body()):
    account_number = payload['account_number']
    secret_code = payload['secret_code']
    source = payload['source']
    headless = payload['headless']
    task = create_task.delay(account_number, secret_code, source, headless)
    print(task)

    return JSONResponse({'task': task.id})
