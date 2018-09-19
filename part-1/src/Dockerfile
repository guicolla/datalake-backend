FROM debian

USER root

RUN apt-get update && apt-get install g++ wget python python-dev python-pip default-jre default-jdk vim curl -y

RUN pip install flask flask_pymongo pymongo python-dateutil

ADD api_mongo.py /root

ADD api.sh /root

RUN chmod 777 /root/api.sh

EXPOSE 5000

CMD ["/root/api.sh"]
