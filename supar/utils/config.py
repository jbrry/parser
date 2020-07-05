# -*- coding: utf-8 -*-


class Config(object):

    def __init__(self, **kwargs):
        self.update(kwargs)

    def __repr__(self):
        s = line = "-" * 15 + "-+-" + "-" * 25 + "\n"
        s += f"{'Param':15} | {'Value':^25}\n" + line
        for name, value in vars(self).items():
            s += f"{name:15} | {str(value):^25}\n"
        s += line

        return s

    def __getitem__(self, key):
        return getattr(self, key)

    def __getstate__(self):
        return vars(self)

    def __setstate__(self, state):
        self.__dict__.update(state)

    def keys(self):
        return vars(self).keys()

    def items(self):
        return vars(self).items()

    def update(self, kwargs):
        for key in ('self', 'cls', '__class__'):
            kwargs.pop(key, None)
        kwargs.update(kwargs.pop('kwargs', dict()))
        for name, value in kwargs.items():
            setattr(self, name, value)

        return self

    def pop(self, key, val=None):
        return self.__dict__.pop(key, val)
