FROM python:3.14.3-trixie

RUN apt-get update
RUN apt-get install -y libsass-dev build-essential libcairo2 git libpango-1.0-0 libpangoft2-1.0-0 pangocairo-1.0 pngquant

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
