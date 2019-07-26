import os

os.chdir("/Users/patrick/")
result = os.listdir(".")
print(result)
print(type(result))

print(os.path.exists("/Users/patrick"))
os.system("touch test.md")
# os.system("rm test.md")