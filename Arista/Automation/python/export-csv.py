import csv
import json

# 1. Load the JSON data
with open("device_data.json", "r") as f:
    data = json.load(f)

# 2. First Pass: Scan the data to find all unique VLAN IDs
unique_vlans = set()
devices = data.get("device", {})

for device_name, interfaces in devices.items():
    for intf_name, intf_data in interfaces.items():
        if "tagged_vlan" in intf_data and intf_data["tagged_vlan"]:
            unique_vlans.add(intf_data["tagged_vlan"])
        if "untagged_vlan" in intf_data and intf_data["untagged_vlan"]:
            unique_vlans.add(intf_data["untagged_vlan"])

# Sort the VLAN columns numerically (e.g., VLAN 5, VLAN 100)
sorted_vlans = sorted(list(unique_vlans))

# 3. Define the base headers and append the dynamic VLAN columns
base_headers = [
    "Device Name",
    "Interface",
    "Speed",
    "Capable Speed",
    "Pluggable",
    "Description",
]
vlan_headers = [f"VLAN {vlan}" for vlan in sorted_vlans]
all_headers = base_headers + vlan_headers

# 4. Second Pass: Build rows and fill with 'T' or 'U' where applicable
csv_rows = []

for device_name, interfaces in devices.items():
    for intf_name, intf_data in interfaces.items():
        # Build the static columns
        # (.get() handles cases where a key like 'pluggable' might be missing)
        row = {
            "Device Name": device_name,
            "Interface": intf_name,
            "Speed": intf_data.get("speed", ""),
            "Capable Speed": intf_data.get("capable_speed", ""),
            "Pluggable": intf_data.get("pluggable", ""),
            "Description": intf_data.get("description", ""),
        }

        # Check for tagged/untagged matches against our global VLAN list
        t_vlan = intf_data.get("tagged_vlan")
        u_vlan = intf_data.get("untagged_vlan")

        for vlan in sorted_vlans:
            header_name = f"VLAN {vlan}"
            if vlan == t_vlan:
                row[header_name] = "T"
            elif vlan == u_vlan:
                row[header_name] = "U"
            else:
                row[header_name] = ""  # Leaves cell blank if not in this VLAN

        csv_rows.append(row)

# 5. Write the mapped data to an Excel-friendly CSV
with open("excel_import.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=all_headers)
    writer.writeheader()
    writer.writerows(csv_rows)

print("CSV conversion complete! Open 'excel_import.csv' in Excel.")
