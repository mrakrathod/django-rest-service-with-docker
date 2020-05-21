# Rest Service Application

#### Start the application.
1. Build the docker image.
```
 docker-compose -f docker-compose.yml build
```
2. Up docker image(run the application).
```
docker-compose -f docker-compose.yml up --no-build -d
```
3. Run test case.
```
docker exec -it api /bin/bash -c "python manage.py test"
```
