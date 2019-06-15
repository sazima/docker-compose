# usage

```
docker-compose up -d
```

# 添加管理员的方法

1. 使用普通方式注册后进入容器:

```bash
 docker exec -it yapi_mongodb_1 mongo yapi
```

2. 更新用户角色为管理员

以注册邮箱your@email.com为例.

```
db.user.update({"email": "your@email.com"}, {$set: {"role": "admin"}})
```
使用exit退出容器

