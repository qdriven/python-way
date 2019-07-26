# -*- coding:utf-8 -*-
from pprint import pprint


class TestNode:
    def __init__(self, name, contents=[]):
        self.name = name
        self.contents = contents

    def __repr__(self):
        return (
            'node(' + repr(self.name) + ', ' +
            repr(self.contents) + ')'
        )


class TestNoReprNode:
    def __init__(self, name):
        self.name = name


node = TestNoReprNode(name="NO-REPR")
pprint(node)

trees = [
    TestNode('node-1'),
    TestNode('node-2', [TestNode('node-3-1')]),
    TestNode('node-3', [TestNode('node-3-1'), TestNode('node-3-2')]),
]

pprint(trees)
