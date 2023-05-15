from abc import ABCMeta, abstractmethod

from system.application.dto.output import Output


class UseCase(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, input_usecase) -> Output:  # type: ignore[no-untyped-def]
        """
        Sync UseCase method that has a input object and returns a output
        """
        raise NotImplementedError()
