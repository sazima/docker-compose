# usage

1. Running 


```
docker build -t web_app  .
docker stack deploy -c docker-compose.yml web
```
or

```
docker-compose up 
```

2. Open http://localhost:5004/ in your browser, and voilà.