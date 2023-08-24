import json
import yaml
import sys
import base64

tenants_file = sys.argv[1]
secret_file = sys.argv[2]
outfile = secret_file.replace('.json', '-out.json')
secrets_key = "secrets.yaml"

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
print()

with open(secret_file, "r") as cf:
    secret = json.load(cf)
#print(secret)

secret_yaml_file_encoded: str = secret["data"][secrets_key]

# decode
secret_yaml_string: str = str(base64.b64decode(secret_yaml_file_encoded).decode("utf-8"))

# read yaml file
secret_yaml: dict = yaml.safe_load(secret_yaml_string)
#print(secret_yaml)

# Get all tenants
all_tenants_in_secret = list(secret_yaml["tenant"].keys())
#print(all_tenants_in_secret)

for i in range(len(all_tenants_in_secret)):
    secret_tenant: str = all_tenants_in_secret[i]
    if secret_tenant not in live_tenants:
        secret_yaml["tenant"].pop(secret_tenant)

print("Updated secrets.yaml file: ")
print(secret_yaml)

# dump into string
dump_string = yaml.dump(secret_yaml)

# encode before write
dump_encoded = str(base64.b64encode(dump_string.encode('utf-8')).decode('utf-8'))

# Update secret
secret["data"][secrets_key] = dump_encoded
secret["metadata"].pop("annotations")
secret["metadata"].pop("creationTimestamp")
secret["metadata"].pop("uid")

#print(secret)
with open(outfile, "w") as outfile:
    json.dump(secret, outfile, indent=4)
