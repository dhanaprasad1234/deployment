FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
#ENV PIP_DISABLE_PIP_VERSION_CHECK = 1
#ENV MYSQLCLIENT_CFLAGS="-I/usr/include/mysql"
#ENV MYSQLCLIENT_LDFLAGS="-L/usr/lib/x86_64-linux-gnu"

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc\
    default-libmysqlclient-dev \
     libmariadb-dev-compat \
     libmariadb-dev \
     libjpeg-dev \
     zlib1g-dev \
     pkg-config \
     && apt-get clean \
     && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/


EXPOSE 8000


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "assign.wsgi:application"]