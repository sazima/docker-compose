1. edit `config.json` for ss and `haproxy.cfg` for haproxy

2. run
```
docker build -t ss:v1 .
docker stack deploy -c docker-compose.yml ss
```

3. enjoy