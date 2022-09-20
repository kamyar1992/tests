from fastapi import FastAPI
from typing import Union  # for optional parameters in python 3.6 to 3.9

app = FastAPI()


@app.get('/user_pass/{userId}')  # userId is a path value
async def user_pass(userId: int, user_name: str, password: str):  # user_name and password are query parameters and
    # fastapi handel them automatically
    item = f'userid is {userId}, username is {user_name}, password is {password}'
    return item


@app.get('/user/user_pass/location/{id}')  # optional parameters for version 3.6 to 3.9
async def user_pass_location(id: int, user_name: str, password: str, location: Union[str, None] = None):  # do not
    # forget = Note in python 3.10 do not use Union just use str | None = None
    item = {'id': id,
            'user_name': user_name,
            'password': password}
    if location:
        item.update({'lacation': location})
    return item
