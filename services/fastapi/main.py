from typing import Annotated

import fastapi
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put('/items/{item_id}')
async def update_item(
        item_id: Annotated[
            int,
            fastapi.Path(
                title='The ID of the item to get',
                ge=0,
                le=1000,
            ),
        ],
        item: Item,
        user: User,
):
    results: dict[str, ...] = {'item_id': item_id}

    if item:
        results['item'] = item

    if user:
        results['user'] = user

    return results
