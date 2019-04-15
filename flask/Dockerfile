FROM python:2.7
EXPOSE 5004
COPY . /api
WORKDIR /api
RUN pip install -r requirements.txt  -i https://pypi.tuna.tsinghua.edu.cn/simple
# set timezone
RUN echo  Asia/Shanghai > /etc/timezone & ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
CMD ["gunicorn", "--bind", "0.0.0.0:5004", "--workers", "3", "manage:app"]