# -*- coding: utf-8 -*-
## http://pyyaml.org/wiki/PyYAMLDocumentation
## pip install pyaml


import yaml


# def represent_ordereddict(dumper, data):
#     value = []
#
#     for item_key, item_value in data.items():
#         node_key = dumper.represent_data(item_key)
#         node_value = dumper.represent_data(item_value)
#         value.append((node_key, node_value))
#
#     return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', value)
#
#
# yaml.add_representer(OrderedDict, represent_ordereddict)
print(yaml.load("""
name: Vorlin Laruknuzum
sex: Male
class: Priest
title: Acolyte
hp: [32, 71]
sp: [1, 13]
gold: 423
inventory:
- a Holy Book of Prayers (Words of Wisdom)
- an Azure Potion of Cure Light Wounds
- a Silver Wand of Wonder
"""))

with open('yml_sample.yml', 'r') as f:
    result = yaml.load(f)
    print(result)
    print(type(result))

with open('yml_dump.yml', 'w') as f:
    yaml.dump(result, f, allow_unicode=True, default_flow_style=False)
