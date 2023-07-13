from typing import List
from fastapi import FastAPI
from report import ram_usage_instance
from serializers import RamUsage


app = FastAPI()


@app.get("/ram_usage/", response_model=List[RamUsage])
async def ram_usage():
    stats = ram_usage_instance.get_ram_stats()
    result = [
        RamUsage.model_validate(
            {
                "id": stat[0],
                "used": stat[1],
                "free": stat[2],
                "total": stat[3],
            }
        ) for stat in stats
    ]

    return result
