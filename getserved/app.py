"""Just a silly little guy."""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def home() -> str:
    """Greet us little guy"""
    return "hullo"


# BaseModel magically turns things into json objects for us
class GetRequest(BaseModel):
    """Take a number"""

    number: int


class GetResponse(BaseModel):
    """Give a string"""

    response: str


@app.post("/fortune")
def fortune(user_data: GetRequest) -> GetResponse:
    """Return a lil guy"""
    return GetResponse(response=f"Your special lil number is: {user_data.number}")
