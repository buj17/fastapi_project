import datetime
from typing import Annotated
from uuid import UUID

import fastapi
from fastapi import FastAPI

app = FastAPI()

@app.get('/items/')
async def read_items(
    ads_id: Annotated[
        str | None,
        fastapi.Cookie()
    ] = None,
):
    return {'ads_id': ads_id}
