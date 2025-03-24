from abc import ABC, abstractmethod


class Figure(ABC):
    @property
    @abstractmethod
    def get_area(self):
        pass

    @property
    @abstractmethod
    def get_perimeter(self):
        pass

    @property
    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Должна быть фигура!")
        return self.get_area + other_figure.get_area
