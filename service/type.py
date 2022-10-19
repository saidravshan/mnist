from typing import List
from pydantic import BaseModel, Field


class Image(BaseModel):
    data: List[float] = Field(..., min_items=784, max_items=784)
