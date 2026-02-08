import datetime
from typing import Annotated
from uuid import UUID

import fastapi
from fastapi import FastAPI

app = FastAPI()


@app.put('/items/{item_id}')
async def read_items(
    item_id: UUID,
    start_datetime: Annotated[datetime.datetime, fastapi.Body()],
    end_datetime: Annotated[datetime.datetime, fastapi.Body()],
    process_after: Annotated[datetime.timedelta, fastapi.Body()],
    repeat_at: Annotated[datetime.time | None, fastapi.Body()] = None
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        'item_id': item_id,
        'start_datetime': start_datetime,
        'end_datetime': end_datetime,
        'process_after': process_after,
        'repeat_at': repeat_at,
        'start_process': start_process,
        'duration': duration,
    }
