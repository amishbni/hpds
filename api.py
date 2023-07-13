import os
from typing import List, Annotated
from functools import lru_cache
from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from report import ram_usage_instance
from serializers import RamUsage
from dotenv import load_dotenv


app = FastAPI()
security = HTTPBasic()


@lru_cache()
def get_settings():
    load_dotenv()
    return {
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD"),
    }


def authenticated(
        credentials: Annotated[HTTPBasicCredentials, Depends(security)],
        settings: dict = Depends(get_settings),
):
    username = settings["username"]
    password = settings["password"]

    if not (
        username == credentials.username and
        password == credentials.password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    return username


@app.get("/ram_usage/", response_model=List[RamUsage])
async def ram_usage(
        request: Request,
        _username: str = Depends(authenticated),
):
    params = request.query_params
    limit = params.get("limit", ram_usage_instance.DEFAULT_LIMIT)
    stats = ram_usage_instance.get_ram_stats(limit=limit)
    result = [
        RamUsage.model_validate(
            {
                "id": stat[0],
                "used": stat[1],
                "free": stat[2],
                "total": stat[3],
                "created": stat[4],
            }
        ) for stat in stats
    ]

    return result
