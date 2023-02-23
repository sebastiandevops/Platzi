#!/usr/bin/env python3

# Python
from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr
# from pydantic import HttpUrl

# FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import HTTPException
from fastapi import Body, Query, Path, Form, Header, Cookie, UploadFile, File

app = FastAPI()


# Models

class HeirColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"


class Location(BaseModel):
    city: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="In"
        )
    state: str = Field(
        min_length=1,
        max_length=50,
        example="MiddeOf"
        )
    country: str = Field(
        min_length=1,
        max_length=50,
        example="Nowhere"
        )


class PersonBase(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Piter"
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Toro"
        )
    age: int = Field(
        ...,
        gt=0,
        le=115,
        example=25
        )
    hair_color: Optional[HeirColor] = Field(default=None, example="black")
    is_married: Optional[bool] = Field(default=None)
    email: EmailStr = Field(
        ...,
        example="pitertoro@example.com"
        )
    password: str = Field(
        ...,
        min_length=8
        )


class Person(PersonBase):
    password: str = Field(
        ...,
        min_length=8
        )


class PersonOut(PersonBase):
    pass


class LoginOut(BaseModel):
    username: str = Field(
        ...,
        max_length=20,
        example="miguel2021",
        )
    # password: str = Field(
    #     ...,
    #     min_length=8,
    #     max_length=12,
    #     example="miguel20"
    #     )
    message: str = Field(
        default="Login Successfully!"
        )


@app.get(
    path="/",
    status_code=status.HTTP_200_OK
)
def home():
    return {"Hello": "World"}


# Request and Response Body
@app.post(
    path="/person/new",
    response_model=Person,
    status_code=status.HTTP_201_CREATED
)
def create_person(person: Person = Body(...)):
    return person


# Validations: Query parameters
@app.get(
    path="/person/detail",
    status_code=status.HTTP_200_OK,
)
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title="Person Name",
        description="This is the person name."
        "It's between 1 and 50 characters.",
        example="Rocío"
    ),
    age: str = Query(
        ...,
        title="Person Age",
        description="This is the person age. It's required.",
        example=25
    )
):
    return {name: age}


persons = [1, 2, 3, 4, 5]


# Validations: Path Parameters
@app.get(
    path="/person/detail/{person_id}",
    status_code=status.HTTP_200_OK
)
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Person Id",
        description="This is the person identification. It's required.",
        example=12345
    )
):
    if person_id not in persons:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="¡This person ddoes not exist!"
        )
    return {person_id: "It exists!"}


# Validations: Request Body
@app.put(
    path="/person/{person_id}",
    status_code=status.HTTP_202_ACCEPTED
)
def update_person(
    person_id: int = Path(
        ...,
        title="Person Id",
        description="This is the person id.",
        gt=0,
        example=12345
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return results
    # return person


@app.post(
    path="/login",
    response_model=LoginOut,
    status_code=status.HTTP_200_OK,
    response_model_exclude={'password'}
)
def login(
    username: str = Form(...),
    password: str = Form(...)
):
    return LoginOut(username=username)


# Cookies and headers Parameters.
@app.post(
    path="/contact",
    status_code=status.HTTP_200_OK
)
def contact(
    first_name: str = Form(
        ...,
        max_length=20,
        min_length=1,
    ),
    last_name: str = Form(
        ...,
        max_length=20,
        min_length=1,
    ),
    email: EmailStr = Form(...),
    message: str = Form(
        ...,
        min_length=20,
    ),
    user_agent: Optional[str] = Header(default=None),
    ads: Optional[str] = Cookie(default=None)
):
    return user_agent


# Files
@app.post(
    path="/post-image"
)
def post_image(
    image: UploadFile = File(...)
):
    return {
            "Filename": image.filename,
            "Format": image.content_type,
            "Size(kb)": round(len(image.file.read()) / 1024, ndigits=2)
    }
