# -*- coding:utf-8 -*-

class Filter(object):
    def init(self):
        self.blocks = []

    def filter(self, seq):
        return [ele for ele in seq if ele > 10]


class SpamFilter(Filter):
    def init(self):
        self.blocks = ["SPAM"]


print(SpamFilter.__bases__)
print(Filter.__bases__)


# print(Filter.__metaclass__) # ERROR

# issubclass()
# isinstance()

class Calculator:
    def calulate(self, expression):
        self.value = eval(expression)
        return self.value

class Talker:
    def talk(self):
        print("Hello World!")

class TalkingCalculator(Calculator,Talker):
    pass


talkCalculator = TalkingCalculator()
talkCalculator.talk()
result = talkCalculator.calulate("1+1")
print(result)

## MRO todo:MRO to understand

print(TalkingCalculator.__bases__)