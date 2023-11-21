from pydantic import BaseModel
#from typing import Optional

class User(BaseModel):
    id: str | None
    name: str
    corp: str
    capital: str
    



