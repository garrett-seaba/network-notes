# Off-Box Automation

# Python Libraries

## PyEAPI Library
This library is created by Arista, and is the easiest way to use the API on Arista devices. This approach is declaritive.  

Example:
```python
import pyeapi

node = pyeapi.connect(host='192.168.0.2',username='arista',password='password',return_node=True)

vlans = node.api('vlans')
result = vlans.create('50')
```

## jsonrpclib Library
This removes much of the manual work that would be required in the requests library method.  

Example:
```python
from jsonrpclib import Server
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

switch = Server("https://arista:password@192.168.0.2/command-api")

response = switch.runCmds( 1, ["show version"] )

print(response)
```

## Requests Library
This is the most low-level library in python. Engineers get high control and flexibility, but requires more configuration and maintenance.  

Example:
```python
import requests
import json
import urllibs

urllib3.disable_warnings()

username = "arista"
password = "password"
device = "leaf1"

json_payload = {
    "jsonrpc": "2.0",
    "method": "runCmds",
    "params": {
        "version": 1,
        "cmds": [
            "show version"
        ],
        "format": "json",
        "timestamps": False,
        "autoComplete": False,
        "expandAliases": False,
        "stopOnError": True,
        "streaming": False,
        "includeErrorDetail": False
    },
    "id": "EapiExplorer-1"
}

response = request.post(
    url,
    data=json.dumps(json_payload),
    auth=(username, password),
    verify=False,
    headers={"Content-Type": "application/json"}
)

print(json.dumps(response.json(), indent=2))
```