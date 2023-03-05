from typing import List

from pydantic import BaseModel

from state_container_py.reducer import Reducer


class TodoItem(BaseModel):
    name: str
    thing_to_do: str


class TodoState(BaseModel):
    todo_items: List[TodoItem] = []


class TodoReducer(Reducer):
    @property
    def state_key(self):
        return "todos"

    @property
    def type(self):
        return TodoState

    def respond_to_action(self, state: TodoState, action):
        if action.type == 'NEW_TODO':
            state.todo_items.append(action.payload)
            return state

        return state
