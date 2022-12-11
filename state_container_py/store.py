from copy import deepcopy
from typing import Type

from state_container_py.action import Action
from state_container_py.app_state import ApplicationState
from state_container_py.reducer import Reducer
from state_container_py.utils import compose_reducers


class Store:

    def __init__(self, reducers):
        self._inputReducers = reducers
        self._reducer_instances = self._construct_instance(reducers)
        self._current_state = self._get_initial_state(self._reducer_instances)
        self._reduce_method = compose_reducers(self._reducer_instances)

    def get_state(self):
        return self._current_state

    def dispatch(self, action: Action):
        new_state = deepcopy(self._current_state)
        new_state = self._reduce_method(new_state, action)
        self._current_state = new_state

    @staticmethod
    def _construct_instance(reducer_constructors: [Type[Reducer]]):
        return [constructor() for constructor in reducer_constructors]

    @staticmethod
    def _get_initial_state(reducer_instances: [Reducer]):
        state = ApplicationState()
        for reducer in reducer_instances:
            reducer_state = reducer.type()()
            state.__dict__[reducer.state_key()] = reducer_state
        return state
