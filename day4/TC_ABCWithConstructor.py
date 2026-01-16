from abc import ABC, abstractmethod

class Employee:
    def __init__(self, name):
        self.name=name
    @abstractmethod
    def salary(self):
        pass