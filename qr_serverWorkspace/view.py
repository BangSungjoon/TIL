from abc import ABCMeta, abstractmethod

class ViewResolver:
    @staticmethod
    def static_view(path):
        return ViewResolver.read_view(path)

    @staticmethod
    def dynamic_view(path):
        path = 'templates/' + path
        return ViewResolver.read_view(path)

    @staticmethod
    def read_view(path):
        f = open(path, 'rb')
        bytes = f.read()
        return bytes
