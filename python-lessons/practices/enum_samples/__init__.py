# -*- coding:utf-8 -*-
import enum


@enum.unique
class BugStatus(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


print('Member name: {},Member value: {}'.format(BugStatus.wont_fix, BugStatus.wont_fix.value))

for status in BugStatus:
    print("{:15}={}".format(status.name, status.value))

actual_state = BugStatus.wont_fix
desired_state = BugStatus.fix_released

print('Equality:',
      actual_state == desired_state,
      actual_state == BugStatus.wont_fix)
print('Identity:',
      actual_state is desired_state,
      actual_state is BugStatus.wont_fix)
print('Ordered by value:')
print('Ordered by value:')
try:
    print('\n'.join('  ' + s.name for s in sorted(BugStatus)))
except TypeError as err:
    print('  Cannot sort: {}'.format(err))

## enum_programatic
BugStatusP = enum.Enum(
    value="BugStatusP",
    names=('a b c d e')
)

for status in BugStatusP:
    print("{:15}={}".format(status.name, status.value))


# complex value

class BugStatusC(enum.Enum):
    new = {
        'num': 7,
        'transitions': [
            'incomplete',
            'invalid',
            'wont_fix',
            'in_progress',
        ],
    }
    incomplete = {
        'num': 6,
        'transitions': ['new', 'wont_fix'],
    }
    invalid = {
        'num': 5,
        'transitions': ['new'],
    }
    wont_fix = {
        'num': 4,
        'transitions': ['new'],
    }
    in_progress = {
        'num': 3,
        'transitions': ['new', 'fix_committed'],
    }
    fix_committed = {
        'num': 2,
        'transitions': ['in_progress', 'fix_released'],
    }
    fix_released = {
        'num': 1,
        'transitions': ['new'],
    }

    def __init__(self, vals):
        self.num = vals['num']
        self.transitions = vals['transitions']

    def can_transition(self, new_state):
        return new_state.name in self.transitions


print('Name:', BugStatusC.in_progress)
print('Value:', BugStatusC.in_progress.value)
print('Custom attribute:', BugStatusC.in_progress.transitions)
print('Using attribute:',
      BugStatusC.in_progress.can_transition(BugStatus.new))
