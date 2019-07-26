# Python Module - yaml

yaml使用虽然不如json广泛，但是依然有很大的使用量，
比如配置文件，比如ansible的任务描述，使用实际上和json有很多类似的地方
 
 - dumps
 - loads
 
 但是由于yaml不是python的标准库需要安装，最简单的安装方法是：
 
```bash
pip instll pyaml
```
 
详细参考信息请移步[pyaml wiki](http://pyyaml.org/wiki/PyYAML)

## YAML 格式：
 
YAML的格式如下：

```
http_protocol:
- schema: http,https
- method: GET/POST/PUT/DELETE/OPTION
- headers:
  - content-type: application/json
  - accept: application/json
  - auth:
    - username: user_name
    - password: password
    - access_key: access_key
- base_url: host_port
- context_url: context_url
```

从上面格式中基本可以看出yaml和json比较类似，也是key-value这种形式，
允许嵌套来表达层级关系.

为了更好的实验，将以上内容放到yaml_sample.yml文件中


## YAML loads
 
loads就是把yaml文件内容，转化为python的数据类型，一般为dict
 
```python
import yaml
with open('yml_sample.yml', 'r') as f:
    result = yaml.load(f)
    print(result)
    print(type(result))

```

结果如下：

```python
{'http_protocol': [{'schema': 'http,https'}, {'method': 'GET/POST/PUT/DELETE/OPTION'}, {'headers': [{'content-type': 'application/json'}, {'accept': 'application/json'}, {'auth': [{'username': 'user_name'}, {'password': 'password'}, {'access_key': 'access_key'}]}]}, {'base_url': 'host_port'}, {'context_url': 'context_url'}]}
<class 'dict'>
```

# yaml dumps

dumps 方法把yaml字符串写入到文件或者其他输入输出中

```python
import yaml
with open('yml_dump.yml', 'w') as f:
    yaml.dump(result, f, allow_unicode=True, default_flow_style=False)
```

运行的结果是：

会把从yaml_sample.yml 中的内容写到yml_dump.xml文件中

