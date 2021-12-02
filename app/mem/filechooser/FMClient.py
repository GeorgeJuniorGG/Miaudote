from __future__ import annotations
from abc import ABC, abstractmethod

class FMClient(ABC):

    @abstractmethod
    def receiveFile(self, file:str, path:str):
        pass

    @abstractmethod
    def registreFM(self, FM):
        pass

    @abstractmethod
    def callFileManager(self):
        pass

    @abstractmethod
    def getCurrentPath(self) -> str:
        pass