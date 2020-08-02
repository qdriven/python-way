from dataclasses import dataclass


## 1. What is Data Class

@dataclass
class GithubRepo:
    name: str
    url: str
    stars: int
    labels: [str]
    desc: str

github = GithubRepo(
    name="name",url="url",stars=12,labels=[],desc="desc"
)

print(github)
