from state_container_py.action import Action
from state_container_py.examples.reducer import TodoReducer
from state_container_py.store import Store

action1 = Action(
    type='UPDATE',
    payload='record some motion capture'
)

reducers = [TodoReducer, ]
# TODO: Combine reducers using class-based version

store = Store(reducers)
store.dispatch(action1)
print(store.get_state())
