from typing import Any

from pydantic import BaseModel


class Action(BaseModel):
    type: str
    payload: Any
