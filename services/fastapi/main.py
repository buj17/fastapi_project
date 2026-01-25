from enum import Enum

from fastapi import FastAPI


class MyModel(str, Enum):
    val_1 = 'val_1'
    val_2 = 'val_2'
    val_3 = 'val_3'


app = FastAPI()


@app.get('/models/{model_name}')
def get_model(model_name: MyModel):
    if model_name is MyModel.val_1:
        return {'model_name': model_name, 'message': 'Chosen 1'}

    if model_name == 'val_2':
        return {'model_name': model_name, 'message': 'Chosen 2 string literals'}

    return {'model_name': model_name, 'message': 'Chosen 3 no variants'}


@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {'file_path': file_path}
