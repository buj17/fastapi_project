import re
from typing import Annotated, Pattern

from fastapi import FastAPI
from fastapi.params import Query

app = FastAPI()

pattern: Pattern[str] | str = re.compile(r'^fixedquery$')


@app.get('/items/')
async def read_items(
        q: Annotated[
            str | None,
            Query(
                alias='item-query',
                title='Query string',
                description='Query string for the items to search in the database that have a good match',
                min_length=3,
                pattern=pattern,
            ),
        ] = None,
):
    results: dict[str, ...] = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results['q'] = q

    return results
