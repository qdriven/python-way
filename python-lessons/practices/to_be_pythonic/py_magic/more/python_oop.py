# -*- coding: utf-8 -*-

class MyClass:
    i = 3

    def my_func(self):
        self.name = 'name'

    def __myPrivate(self):
        print("this is private")

    @staticmethod
    def the_static_method(x):
        print(x)


class NewClass(MyClass):
    def __init__(self):
        super(NewClass, self).__init__()
        self.i = 5


print(MyClass.i)
my_class = MyClass()
print(my_class.i)  ## very interesting
MyClass.the_static_method(12)
my_class.the_static_method(12)
print(dir(my_class))
my_class._MyClass__myPrivate()


# my_class.__myPrivate() //get error

# class Factory:
#     def register(self,methodName,constructor,*args,**kwargs):
#         _args=[constructor]
#         _args.extend(args)
#         setattr(self,methodName,apply(Functor,_args,kwargs))
#
#
# class Functor:
#     def __init__(self, function, *args, **kargs):
#         assert callable(function), "function should be a callable obj"
#         self._function = function
#         self._args = args
#         self._kargs = kargs
#
#     def __call__(self, *args, **kargs):
#         """call function"""
#         _args = list(self._args)
#         _args.extend(args)
#         _kargs = self._kargs.copy()
#         _kargs.update(kargs)
#         return apply(self._function, _args, _kargs)
