from typing import Annotated

import fastapi
from fastapi import FastAPI
from pydantic import PositiveInt

app = FastAPI()


@app.get('/items/{item_id}')
async def items(
        item_id: Annotated[
            PositiveInt,
            fastapi.Path(
                title='The ID of the item to get',
                ge=1,
            )
        ],
        size: Annotated[
            float,
            fastapi.Query(
                gt=0,
                lt=10.5,
            )
        ],
        q: Annotated[
            str | None,
            fastapi.Query(alias='item-query'),
        ] = None,

):
    results: dict[str, ...] = {'item_id': item_id}
    if q:
        results['q'] = q

    results['size'] = size

    return results
