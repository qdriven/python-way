# -*- coding:utf-8 -*-
from pymodules.abs.abs_base import PluginBase


class LocalBaseClass:
    pass

@PluginBase.register
class RegisteredImplementation(LocalBaseClass):

    def load(self,input):
        return input.read()

    def save(self,output,data):
        return output.write(data)

class SubclassImplementation(PluginBase):

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)
# incomplete implementation

if __name__ == '__main__':
    print('Subclass:', issubclass(RegisteredImplementation,
                                  PluginBase))
    print('Instance:', isinstance(RegisteredImplementation(),
                                  PluginBase))
    print('Subclass:', issubclass(SubclassImplementation,
                                  PluginBase))
    print('Instance:', isinstance(SubclassImplementation(),
                                  PluginBase))

    for sc in PluginBase.__subclasses__():
        print(sc.__name__)