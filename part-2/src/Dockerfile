FROM debian

USER root

RUN apt-get update && apt-get install g++ wget python python-dev python-pip default-jre default-jdk vim ruby -y

RUN pip install requests

RUN gem install sinatra

ADD api_url.py /root

ADD input-dump /root

ADD api.sh /root

ADD url-aggregator-api.rb /root

RUN chmod 755 /root/api.sh

CMD ["/root/api.sh"]
