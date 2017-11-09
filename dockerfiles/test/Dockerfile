FROM python:3.5.4
COPY test-srv/requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
ADD app-srv /app-srv
ADD test-srv /test-srv
WORKDIR /test-srv
CMD ["bash", "cli/test.sh"]
