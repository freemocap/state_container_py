from state_container_py.base_state import BaseState
from state_container_py.reducer import Reducer


# TODO: Deal with defaults
class TodoState(BaseState):
    name: str = ""
    completed: bool = False


class TodoReducer(Reducer):
    def state_key(self):
        return "todos"

    def type(self):
        return TodoState

    def respond_to_action(self, state: TodoState, action):
        if action.type == 'UPDATE':
            state.name = action.payload
            return state
        return state
