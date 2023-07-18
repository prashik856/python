import json
import yaml

tenants_file = "tenant.json"
configmap_file = "configmap.json"

live_tenants = []
with open(tenants_file, "r") as tf:
    file_data = json.load(tf)

    for i in range(len(file_data)):
        namespace: str = file_data[i]["namespace"]
        tenant = namespace.split("-")[0] + "_" + namespace.split("-")[1]
        live_tenants.append(tenant)

print("Live Tenants: " + str(live_tenants))

with open(configmap_file, "r") as cf:
    configmap = json.load(cf)
# print(configmap)

baseconfig_file = configmap["data"]["base-config.yaml"]

baseconfig = yaml.safe_load(baseconfig_file)
# print(baseconfig)

all_tenants_in_cm = list(baseconfig["tenant"].keys())

for i in range(len(all_tenants_in_cm)):
    cm_tenant: str = all_tenants_in_cm[i]
    if cm_tenant not in live_tenants:
        baseconfig["tenant"].pop(cm_tenant)

print(baseconfig)

baseconfig_string = yaml.dump(baseconfig)
configmap["data"]["base-config.yaml"] = baseconfig_string
configmap["metadata"].pop("annotations")
configmap["metadata"].pop("creationTimestamp")
configmap["metadata"].pop("uid")

with open("configmap-out.json", "w") as outfile:
    json.dump(configmap, outfile, indent=4)
