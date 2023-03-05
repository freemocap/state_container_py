from pydantic import BaseModel

from state_container_py.action import Action
from state_container_py.app_state import ApplicationState
from state_container_py.examples.todo_reducer import TodoItem, TodoReducer, TodoState
from state_container_py.store import Store


class TodoAppState(ApplicationState):
    todos: TodoState


action1 = Action(
    type='NEW_TODO',
    payload=TodoItem(
        name="1",
        thing_to_do="testing"
    )
)

reducers = [TodoReducer, ]

store = Store(TodoAppState.construct(), reducers)
store.dispatch(action1)

print(store.state())
