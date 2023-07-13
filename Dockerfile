FROM python:3.11.4

WORKDIR $HOME/src

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . $HOME/src/
