from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass

# abstract base class


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError('Stream is already opened')
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError('Stream is already closed')
        self.opened = False

    @abstractmethod  # common interface for other classes in the future, other classes MUST implement a read method of their OWN
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print('Reading data from file')


class NetworkStream(Stream):
    def read(self):
        print('Reading data from a network')


class MemoryStream(Stream):
    def read(self):
        print('Reading data from a memory stream')


stream = Stream()
stream.open()

mStream = MemoryStream()
