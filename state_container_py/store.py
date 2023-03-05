from copy import deepcopy
from typing import List, Type

from pydash import get, set_

from state_container_py.action import Action
from state_container_py.app_state import ApplicationState
from state_container_py.reducer import Reducer


class Store:

    def __init__(self, app_state: ApplicationState, reducers: List[Type[Reducer]]):
        self._current_state = app_state
        self._inputReducers = reducers
        self._reducer_instances = self._construct_instance(reducers)

    def dispatch(self, action: Action):
        current = deepcopy(self._current_state)

        for inst in self._reducer_instances:
            state_at_key = get(current, inst.state_key, inst.type.construct())
            new_state = inst.respond_to_action(state_at_key, action)
            set_(current, inst.state_key, new_state)

        self._current_state = current

    def state(self):
        return self._current_state

    def _construct_instance(self, reducer_constructors: List[Type[Reducer]]):
        return [constructor() for constructor in reducer_constructors]
