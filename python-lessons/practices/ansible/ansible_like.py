# -*- coding:utf-8 -*-

def copy(args={}):
    for kwarg, v in args.items():
        print("{key}={value}".format(key=kwarg, value=v))


def print_kv(args={}):
    for kwarg, v in args.items():
        print("{key}={value}".format(key=kwarg, value=v))


module_mapping = {
    "copy": copy,
    "test": print_kv
}


def ansible(module, module_args):
    func = module_mapping.get(module)
    parsed = module_args.split(" ")
    args = {}
    for module_arg in parsed:
        kv = module_arg.split("=")
        args[kv[0]] = kv[1]
    func(args)


if __name__ == '__main__':
    ansible(module='copy', module_args="name=name test=test")
