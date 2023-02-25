#!/usr/bin/env python3

# Python
from uuid import UUID

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI

app = FastAPI()


# Models
class User():
    user_id = UUID


class Tweet():
    pass


@app.get(path="/")
def home():
    return {"TwitterAPI": "Working!"}
