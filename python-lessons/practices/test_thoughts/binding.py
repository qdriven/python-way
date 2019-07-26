# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger('binding')


class Context(object):
    variables = dict()
    generators = dict()

    def __init__(self):
        self.variables = dict()
        self.generators = dict()


    def bind_variable(self,name,value):
        """
        bind key to a value
        :param name:
        :param value:
        :return:
        """
        pass

    def add_generator(self,name,generator):
        self.generators[name]=generator