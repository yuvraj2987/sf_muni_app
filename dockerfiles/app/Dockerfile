FROM python:3.5.4
ADD app-srv /app-srv
WORKDIR /app-srv
RUN pip install -r requirements.txt
CMD ["bash", "cli/run.sh"]
