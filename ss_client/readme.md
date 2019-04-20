# ss-client load balancing


## change config.json and haproxy.cfg

config.json

```angular2
[
  {
    "server": "your server ip",
    "local_address": "0.0.0.0",
    "local_port": "1085",  
    "server_port": "2400",
    "password": "your password",
    "method": "aes-256-cfb",
    "protocol": "origin",
    "obfs": "plain"
  },
  #...
  ]
```

```angular2
# ...
    server ss-1081 ss:1081 weight 10 check
    server ss-1082 ss:1082 weight 10 check
    server ss-1083 ss:1083 weight 10 check
    server ss-1084 ss:1084 weight 10 check
    server ss-1085 ss:1085 weight 10 check
    server bad-1 ss:1080 weight 10 check
```

## build and run

```angular2
docker build -t haproxy:v1 haproxy/
docker build -t sslocal:v1 client/
docker-compose up
```
