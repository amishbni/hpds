## Usage

Make sure to install [docker](https://docs.docker.com/get-docker) and [docker compose](https://docs.docker.com/compose/install).
Create a `.env` file at the root of the project and fill it with this content:

```
USERNAME=username
PASSWORD=password
```

Then, you can bring up the services with this command:

```shell
docker compose up
```

And after that, you can use the API. For example,

```shell
curl -X GET "http://localhost:8000/ram_usage/?limit=5" \
-H "accept: application/json" -u username:password
```