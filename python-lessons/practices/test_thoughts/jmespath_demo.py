# -*- coding: utf-8 -*-

# http://jmespath.org/libraries.html
# pip install jmespath
import jmespath
# use path
path = jmespath.search('foo.bar', {'foo': {'bar': 'baz'}})
print(path)

# use expression
expression = jmespath.compile('foo.bar')
result = expression.search({'foo': {'bar': 'baz'}})
print(result)

## Basic Expressions

source={"a": "foo", "b": "bar", "c": "baz"}
result = jmespath.search("a",source)
print(result)

## Subexpression
source_1={"a": {"b": {"c": {"d": "value"}}}}
sub_result = jmespath.search("a.b.c",source_1)
print(sub_result)

## index expression
source_2 = ["a", "b", "c", "d", "e", "f"]
index_result = jmespath.search("[1]",source_2)
print(index_result)

## composite expression

composite_exp = "a.b.c[0].d[1][0]"
source_3= {"a": {
  "b": {
    "c": [
      {"d": [0, [1, 2]]},
      {"d": [3, 4]}
    ]
  }
}}

composite_result = jmespath.search(composite_exp,source_3)

print(composite_result)

## slicing

source_4=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
slicing_exp = "[0:5]"
slicing_result = jmespath.search(slicing_exp,source_4)
print(slicing_result)

## projections:
list_exp="people[*].first"
source_5 = {
  "people": [
    {"first": "James", "last": "d"},
    {"first": "Jacob", "last": "e"},
    {"first": "Jayden", "last": "f"},
    {"missing": "different"}
  ],
  "foo": {"bar": "baz"}
}

proj_result1= jmespath.search(list_exp,source_5)
print(proj_result1) # ['James', 'Jacob', 'Jayden']


obj_exp ="reservations[*].instances[*].state"
source_6= {
  "reservations": [
    {
      "instances": [
        {"state": "running"},
        {"state": "stopped"}
      ]
    },
    {
      "instances": [
        {"state": "terminated"},
        {"state": "runnning"}
      ]
    }
  ]
}

proj_result2=jmespath.search(obj_exp,source_6)
print(proj_result2) #[['running', 'stopped'], ['terminated', 'runnning']]

# Flatten projections

source_7=[
  [0, 1],
  2,
  [3],
  4,
  [5, [6, 7]]
]
flat_exp ="[]"
flat_result = jmespath.search(flat_exp,source_7)
print(flat_result) # [0, 1, 2, 3, 4, 5, [6, 7]]

# filter

filter_exp="machines[?state=='running'].name"
filter_source ={
  "machines": [
    {"name": "a", "state": "running"},
    {"name": "b", "state": "stopped"},
    {"name": "b", "state": "running"}
  ]
}
filter_result = jmespath.search(filter_exp,filter_source)
print(filter_result)

# pipe expression

pipe_exp= "people[*].first | [0]"
pipe_source= {
  "people": [
    {"first": "James", "last": "d"},
    {"first": "Jacob", "last": "e"},
    {"first": "Jayden", "last": "f"},
    {"missing": "different"}
  ],
  "foo": {"bar": "baz"}
}

pipe_result = jmespath.search(pipe_exp,pipe_source)
print(pipe_result)  # James

# multiselect
multi_exp="people[].[first,last]"
multiselect_result = jmespath.search(multi_exp,pipe_source)
print(multiselect_result) # [['James', 'd'], ['Jacob', 'e'], ['Jayden', 'f'], [None, None]]