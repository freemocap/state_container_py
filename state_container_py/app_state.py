from pydantic import BaseModel, Extra


class ApplicationState(BaseModel):
    class Config:
        extra = Extra.allow
