from pydantic import BaseModel


class RamUsage(BaseModel):
    id: int
    used: int
    free: int
    total: int
    created: str
