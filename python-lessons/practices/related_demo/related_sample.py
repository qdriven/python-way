# encoding: utf-8
"https://github.com/genomoncology/related"

import related


@related.immutable
class Person(object):
    first_name = related.StringField()
    second_name = related.StringField()

@related.immutable
class RoleModels(object):
    scientists = related.SetField(Person)

people =[Person("f","l"),Person('n','z')]
print(related.to_yaml(RoleModels(scientists=people)))

""" docker compose sample
version: '2'
services:
  web:
    build: .
    ports:
    - 5000:5000
    volumes:
    - .:/code
  redis:
    image: redis
"""

@related.immutable
class Service(object):
    name = related.StringField()
    image = related.StringField(required=False)
    build = related.StringField(required=False)
    ports = related.SequenceField(str, required=False)
    volumes = related.SequenceField(str, required=False)
    command = related.StringField(required=False)


@related.immutable
class Compose(object):
    version = related.StringField(required=False, default=None)
    services = related.MappingField(Service, "name", required=False)


from os.path import join, dirname

from related import to_yaml, from_yaml, to_model

YML_FILE = join(dirname(__file__), "docker-compose.yml")


def test_compose_from_yml():
    original_yaml = open(YML_FILE).read().strip()
    yml_dict = from_yaml(original_yaml)
    compose = to_model(Compose, yml_dict)

    assert compose.version == '2'
    assert compose.services['web'].ports == ["5000:5000"]
    assert compose.services['redis'].image == "redis"

    generated_yaml = to_yaml(compose,
                             suppress_empty_values=True,
                             suppress_map_key_values=True).strip()

    assert original_yaml == generated_yaml

if __name__ == '__main__':
    test_compose_from_yml()