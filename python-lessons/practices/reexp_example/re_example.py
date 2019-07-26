import re

text = "the quick brown fox jumps over the lazy dog"

result = re.findall(".o.", text)
print(result)

# search for three letter words enclosed by whitespace
result = re.findall("\s(\wo\w)\s*", text)
print(result)

# substitue andy of **** by a w
print(re.sub("[dflj]", "w", text))
print(text)

result = re.search('jump|swims',text)
print(result)