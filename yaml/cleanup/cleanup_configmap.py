import json
import yaml
import sys

tenants_file = sys.argv[1]
configmap_file = sys.argv[2]
outfile = configmap_file.replace('.json', '-out.json')
base_config_key = "base-config.yaml"

live_tenants = []
with open(tenants_file, "r") as tf:
    file_data = json.load(tf)

    for i in range(len(file_data)):
        namespace: str = file_data[i]["namespace"]
        if namespace.split("-")[1] == "prod":
            tenant: str = namespace.split("-")[0]
        else:
            tenant: str = namespace.split("-")[0] + "_" + namespace.split("-")[1]
        live_tenants.append(tenant)

print("Live Tenants: " + str(live_tenants))

with open(configmap_file, "r") as cf:
    configmap = json.load(cf)
# print(configmap)

baseconfig_file = configmap["data"][base_config_key]

baseconfig = yaml.safe_load(baseconfig_file)
# print(baseconfig)

all_tenants_in_cm = list(baseconfig["tenant"].keys())

for i in range(len(all_tenants_in_cm)):
    cm_tenant: str = all_tenants_in_cm[i]
    if cm_tenant not in live_tenants:
        baseconfig["tenant"].pop(cm_tenant)

print(baseconfig)

baseconfig_string = yaml.dump(baseconfig)
configmap["data"][base_config_key] = baseconfig_string
configmap["metadata"].pop("annotations")
configmap["metadata"].pop("creationTimestamp")
configmap["metadata"].pop("uid")

with open(outfile, "w") as outfile:
    json.dump(configmap, outfile, indent=4)
