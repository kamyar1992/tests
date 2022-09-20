# Framework
# Django, Flask, fastAPI

from fastapi import FastAPI
from enum import Enum  # this class is used to restrict input in and api method
app = FastAPI()  # app is a convention name


@app.get('/')  # application/path/function   or method/path/functioncd
async def root():
    return {'message': 'welcome to tehran'}

# https://github.com/OAI/OpenAPI-Specification

# Concurrency: threading, multi processing, asyncio

# Coroutine ---> async ---> await


@app.get('/v1/users/{user}')  # *important: do not forget first / in the path
async def hello_user(user):
    return {'hello': '{}'.format(user)}
    # return f'hello {user}'


# annotation: in fastapp make it compulsory for method that get the exact type of input
@app.get('/v1/user/annotated_method/{user}')
async def hello_annotation(user: int) -> dict:
    return {'hello': f'{user}'}


class Models(str, Enum):  # in this class the input that user can choose is identified
    vggnet = 'vggnet'
    resent = 'resent'
    alexnet = 'alexnet'
    googlenet = 'googlenet'
    lenet = 'lenet'


@ app.get('/v1/models/{model}')
async def models(model: Models):
    if model == 'veggnet':
        return {'model': model}
    if model == 'resent':
        return {'model': model}
    if model == 'alexnet':
        return {'model': model}
    if model == 'googlenet':
        return {'model': model}
    if model == 'lenet':
        return {'model': model}




























