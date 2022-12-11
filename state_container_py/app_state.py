from pydantic import Extra

from state_container_py.base_state import BaseState


class ApplicationState(BaseState):
    class Config:
        extra = Extra.allow
