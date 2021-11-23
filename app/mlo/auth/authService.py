from __future__ import annotations
from abc import ABC, abstractmethod
from .basicUserdata import BasicUSerData

class AuthService(ABC):

    @abstractmethod
    def login(self, email:str, password:str) -> bool:
        pass

    @abstractmethod
    def signUp(self, password1:str, password2:str, minimumAge:str, isProtector:bool, userData:BasicUSerData) -> bool:
        pass

    @abstractmethod
    def getUserID(self) -> str:
        pass