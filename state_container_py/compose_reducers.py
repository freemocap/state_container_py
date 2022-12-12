from functools import partial, reduce
from typing import Callable

from state_container_py.action import Action
from state_container_py.base_state import BaseState
from state_container_py.reducer import Reducer


def compose_reducers(reducer_instances: [Reducer]):
    reduce_methods = _get_reduce_methods(reducer_instances)
    return reduce(_compose_update_for_two_reducers, reduce_methods)


def _get_reduce_methods(reducer_instances: [Reducer]):
    reduce_methods = []
    for inst in reducer_instances:
        partial_reduce = partial(_update_state_for_reducer, inst)
        reduce_methods.append(partial_reduce)
    return reduce_methods


def _update_state_for_reducer(reducer: Reducer, state: BaseState, action: Action):
    # TODO: add new_state object
    state.__dict__[reducer.state_key()] = reducer.respond_to_action(state[reducer.state_key()], action)
    return state


def _compose_update_for_two_reducers(func1: Callable, func2: Callable):
    return lambda a, b: func2(func1(a, b), b)
