from __future__ import annotations
from abc import ABC, abstractmethod

class AuthService(ABC):

    @abstractmethod
    def login(self, email:str, password:str) -> bool:
        pass

    @abstractmethod
    def signUp(self, email:str, password:str) -> bool:
        pass