FROM python:3.5.4
COPY app-srv/requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
ADD app-srv /app-srv
WORKDIR /app-srv
CMD ["bash", "cli/run.sh"]
