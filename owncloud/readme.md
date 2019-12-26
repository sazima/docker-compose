```bash
# Create the environment configuration file
cat << EOF > .env
OWNCLOUD_VERSION=10.3
OWNCLOUD_DOMAIN=localhost
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin
HTTP_PORT=8080
EOF

# Build and start the container
docker-compose up -d

```
via: https://doc.owncloud.com/server/admin_manual/installation/docker/
