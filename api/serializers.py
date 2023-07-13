from pydantic import BaseModel


class RamUsageSerializer(BaseModel):
    id: int
    used: int
    free: int
    total: int
    created: str
