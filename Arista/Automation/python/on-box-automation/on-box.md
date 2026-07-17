## Enter Bash on EOS
```conf
bash
```

## Now enter python interpreter
```bash
python
```

## Python Commands for on-box automation
```python
from EapiClientLib import EapiClient
from pprint import pprint   # Outputs nice json
switch = EapiClient(disableAaa=True, privLevel=15)
response = switch.runCmds(1, ['show version'])
pprint(response)
print('The switch system MAC address is', response['result'][0]['systemMacAddress'])
result = switch.runCmds(version=1,cmds=["sh ver"], format='json', autoComplete=True)
model_name = result["result"][0]["modelName"]
print(model_name)


commands_list = ["sh ip int br", "sh ver"]
result = switch.runCmds(version=1,cmds=commands_list, format='json', autoComplete=true)
pprint(result)

conf = ["enable", "configure", "vlan 10", "name ten"]
conf_vlan_10 = switch.runCmds(version=1,cmds=conf)
result = switch.runCmds(version=1,cmds=["show vlan"])
pprint(result)

vlan10_name = result["result"][0]["vlans"]["10"]["name"]
print(vlan10_name)