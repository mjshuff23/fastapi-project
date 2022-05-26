from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    signup_ts: Optional[datetime] = None
    email: str


external_data = {
    "id": 123,
    "signup_ts": datetime.now(),
    "username": "mjshuff23",
    "first_name": "Michael",
    "last_name": "Shuff",
    "email": "mjshuff23@gmail.com",
}
