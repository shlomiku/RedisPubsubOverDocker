FROM sebp/elk:es241_l240_k461


ENV ES_HOME /usr/share/elasticsearch
WORKDIR ${ES_HOME}

RUN gosu elasticsearch bin/plugin install royrusso/elasticsearch-HQ
# http://<your-host>:9200/_plugin/hq/
RUN gosu elasticsearch bin/plugin install mobz/elasticsearch-head --verbose
# http://<your-host>:9200/_plugin/head/
#RUN gosu elasticsearch bin/plugin install lukas-vlcek/bigdesk
# http://<your-host>:9200/_plugin/bigdesk/

#ENV KIBANA_HOME /usr/share/kibana
WORKDIR ${KIBANA_HOME}
RUN gosu kibana bin/kibana plugin -i elastic/sense
# http://<your-host>:5601/apss/sense