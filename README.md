# tstpw
TST PW Test the password

# Wordlist sources
## Lang FI
```
https://kotus.fi/sanakirjat/kielitoimiston-sanakirja/nykysuomen-sana-aineistot/nykysuomen-sanalista/
```

## Firstnames both men and women FI
```
https://www.avoindata.fi/data/fi/dataset/none
```


## Surnames FI
```
https://www.avoindata.fi/data/fi/dataset/none
```

# Example docker-compose.yml
```
services:
  redis:
    build:
      context: .
      dockerfile: redis.Dockerfile
    container_name: tstpw_redis
    secrets:
      - redis_password
    restart: unless-stopped
    command: sh -c "redis-server --requirepass $(cat /run/secrets/redis_password)"
    ports:
      - '6379:6379'
    networks:
      - tstpw_network

networks:
  tstpw_network:

secrets:
  redis_password:
    file: ./secret_redis_password.txt
```