from copy import deepcopy
from functools import partial, reduce

from state_container_py.action import Action
from state_container_py.app_state import ApplicationState


class Store:

    def __init__(self, reducers):
        self._inputReducers = reducers
        self._reducer_instances = self._construct_instance(reducers)
        self._current_state = self._get_initial_state()
        self._reduce_method = self._get_reduce_method()

    def get_state(self):
        return self._current_state

    def dispatch(self, action: Action):
        # TODO: Create a copy of the object in a non mutable way (deep clone)
        new_state = deepcopy(self._current_state)
        new_state = self._reduce_method(new_state, action)
        self._current_state = new_state

    def _construct_instance(self, reducer_constructors):
        return [constructor() for constructor in reducer_constructors]

    def _get_initial_state(self):
        state = ApplicationState()
        for reducer in self._reducer_instances:
            reducer_state = reducer.type()()
            state.__dict__[reducer.state_key()] = reducer_state
        return state

    def _get_reduce_method(self):
        reduce_methods = self._get_reduce_methods()
        return reduce(self._compose_update_for_two_reducers, reduce_methods)

    def _get_reduce_methods(self):
        reduce_methods = []
        for inst in self._reducer_instances:
            partial_reduce = partial(self._update_state_for_reducer, inst)
            reduce_methods.append(partial_reduce)
        return reduce_methods

    @staticmethod
    def _update_state_for_reducer(reducer, state, action):
        # TODO: add new_state object
        state.__dict__[reducer.state_key()] = reducer.respond_to_action(state[reducer.state_key()], action)
        return state

    @staticmethod
    def _compose_update_for_two_reducers(func1, func2):
        return lambda a, b: func2(func1(a, b), b)
