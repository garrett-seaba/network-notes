import requests
import json
import urllib3

urllib3.disable_warnings() # Self-signed certificate

username = "arista"
password = "password"
device_list = ["leaf1", "leaf2", "leaf3", "leaf4", "spine1", "spine2", "spine3", "spine4"]

save_dir = "backups"

for device in device_list:

    url = f"https://{device}/command-api"

    json_payload = {
        "jsonrpc": "2.0",
        "method": "runCmds",
        "params": {
            "version": 1,
            "cmds": [
                "show running-config",
            ],
            "format": "text",
            "timestamps": False,
            "autoComplete": False,
            "stopOnError": True,
            "streaming": False,
            "includeErrorDetail": False
        },
        "id": "EapiExplorer-1"
    }

    response = requests.post(
        url,
        data=json.dumps(json_payload),
        auth=(username, password),
        verify=False,
        headers={"Content-Type": "application/json"}
    )

    result = response.json()

    running_config = result["result"][0]["output"]
    with open(f"{save_dir}/{device}.cfg", "w") as fh:
        fh.write(running_config)