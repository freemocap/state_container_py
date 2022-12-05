from state_container_py.reducer import Reducer


# TODO: Deal with defaults
class TodoState:
    name: str
    thing_to_do: str


class TodoReducer(Reducer):
    def state_key(self):
        return "todos"

    def type(self):
        return TodoState

    def respond_to_action(self, state: TodoState, action):
        if action.type == 'UPDATE':
            return {
                **state,
                **action.payload,
            }

        return state
