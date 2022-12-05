from state_container_py.action import Action
from state_container_py.app_state import ApplicationState


class Store:

    def __init__(self, reducers):
        # TODO: Deal with defaults
        self._current_state = ApplicationState()

        self._inputReducers = reducers
        self._reducer_instances = self._construct_instance(reducers)

    def dispatch(self, action: Action):
        for inst in self._reducer_instances:
            new_state = inst.respond_to_action({}, action)
            self._current_state = new_state

    def _construct_instance(self, reducer_constructors):
        return [constructor() for constructor in reducer_constructors]