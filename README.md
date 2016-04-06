to run container:

```bash
docker run -d --name ftpd_server -p 21:21 -p 30000-30009:30000-30009 -e "PUBLICHOST=localhost" nikkor/pure-ftpd-with-user
```

user: joe / 123456
