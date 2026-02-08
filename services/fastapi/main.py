from typing import Annotated

import fastapi
from fastapi import FastAPI
from pydantic import (
    BaseModel,
    Field, HttpUrl,
)

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: Annotated[
        str,
        Field(
            max_length=200
        )
    ]
    description: Annotated[
        str | None,
        Field(
            title='Item description',
            max_length=300
        )
    ] = None
    price: Annotated[
        float,
        Field(
            gt=0,
            description='The price must not be greater than zero'
        )
    ]
    tax: float | None = None
    tags: list[str] = []
    images: list[Image] | None = None


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
