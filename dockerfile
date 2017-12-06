FROM python
LABEL author="xuqinghan"
LABEL purpose = ''


RUN apt update
RUN pip3 install setuptools

ENV PYTHONIOENCODING=utf-8

# Build folder
RUN mkdir -p /deploy/app
WORKDIR /deploy/app
#only copy requirements.txt.  othors will be mounted by -v
#COPY app/requirements.txt /deploy/app/requirements.txt
#RUN pip3 install -r /deploy/app/requirements.txt
RUN pip3 install celery

# run sh. Start processes in docker-compose.yml
#CMD ["/usr/bin/supervisord"]
CMD ["/bin/bash"]
