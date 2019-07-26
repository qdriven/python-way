# -*- coding:utf-8 -*-
import abc


class PluginBase(metaclass=abc.ABCMeta):
    # class PluginBase(abc.ABC):

    @abc.abstractmethod
    def load(self, input):
        """
        retrieve data from the input source
        :param input:
        :return:
        """
        # pass

    @abc.abstractmethod
    def save(self, output, data):
        """save the data object to the output"""
        # pass


class ABCWithConcreteImplementation(abc.ABC):
    @abc.abstractmethod
    def retrieve_values(self, input):
        print('base class reading data')
        return input.read()


