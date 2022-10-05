# bank-scraper


create an virtual env for python application

```bash
python3 -m venv bankscraper

source bankscraper/bin/activate
```

scrape fortuneo.fr

```bash
python3 scrapers/scraper.py <client_secret> <secret_code> headless # mode debug
```

```bash
uvicorn main:app --host 0.0.0.0 --reload # goto 0.0.0.0:8000 in the browser
```

```bash
celery -A worker.celery worker --logfile=logs/celery.log
```

test app with pytest

```bash
python -m pytest
```