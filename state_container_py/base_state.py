from pydantic import BaseModel


class BaseState(BaseModel):

    def __getitem__(self, item):
        return getattr(self, item)

