from state_container_py.action import Action
from state_container_py.examples.reducer import TodoReducer
from state_container_py.store import Store

action1 = Action(
    type='Test1',
    payload='Some shit'
)

reducers = [TodoReducer, ]
# TODO: Combine reducers using class-based version

store = Store(reducer)
store.dispatch(action1)
