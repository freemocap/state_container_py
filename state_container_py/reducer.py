from abc import ABC, abstractmethod

from pydantic import typing

from state_container_py.action import Action


class Reducer(ABC):

    @property
    @abstractmethod
    def state_key(self):
        pass

    @property
    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def respond_to_action(self, state: typing.Any, action: Action):
        pass

