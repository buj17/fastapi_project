from typing import Annotated

import fastapi
from fastapi import FastAPI
from pydantic import (
    BaseModel,
    Field,
)

app = FastAPI()


class Item(
    BaseModel,
):
    name: str = Field(
        max_length=200,
    )
    description: str | None = Field(
        default=None,
        title='Item description',
        max_length=300,
    )
    price: float = Field(
        gt=0,
        description='The price must be grater than zero',
    )
    tax: float | None = None


@app.put(
    '/items/{item_id}',
)
async def update_item(
    item_id: int,
    item: Annotated[
        Item,
        fastapi.Body(
            embed=True,
        ),
    ],
):
    results = {'item_id': item_id, 'item': item}
    return results
