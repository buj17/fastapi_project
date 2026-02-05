from typing import Annotated, Literal

import fastapi
from fastapi import FastAPI
from pydantic import BaseModel, Field, ConfigDict

app = FastAPI()


class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal['created_at', 'updated_at'] = 'created_at'
    tags: list[str] = []

    model_config = ConfigDict(
        extra='forbid',
    )


@app.get('/items/')
async def read_items(filter_query: Annotated[FilterParams, fastapi.Query()]):
    return filter_query
