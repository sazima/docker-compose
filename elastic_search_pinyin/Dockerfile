FROM docker.elastic.co/elasticsearch/elasticsearch:6.7.2
# COPY elasticsearch-analysis-ik-6.7.2.zip  /elasticsearch-analysis-ik-6.7.2.zip
# RUN elasticsearch-plugin install -b file:///elasticsearch-analysis-ik-6.7.2.zip
RUN elasticsearch-plugin install -b https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v6.7.2/elasticsearch-analysis-ik-6.7.2.zip
# COPY  elasticsearch-analysis-pinyin-6.7.2.zip  /elasticsearch-analysis-pinyin-6.7.2.zip
# RUN elasticsearch-plugin install -b file:///elasticsearch-analysis-pinyin-6.7.2.zip
RUN elasticsearch-plugin install -b https://github.com/medcl/elasticsearch-analysis-pinyin/releases/download/v6.7.2/elasticsearch-analysis-pinyin-6.7.2.zip
