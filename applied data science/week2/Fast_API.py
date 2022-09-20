# Framework
# Django, Flask, fastAPI

from fastapi import FastAPI

app = FastAPI()  # app is a convention name


@app.get('/')  # application/path/function   or method/path/functioncd
async def root():
    return {'message': 'welcome to tehran'}

# https://github.com/OAI/OpenAPI-Specification

# Concurrency: threading, multi processing, asyncio

# Coroutine ---> async ---> await
