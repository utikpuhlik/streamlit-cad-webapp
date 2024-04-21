from pydantic import BaseModel, HttpUrl


class URL(BaseModel):
    url: HttpUrl