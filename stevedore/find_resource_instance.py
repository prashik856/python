import json

with open("resources.json", "r") as jf:
    data = json.load(jf)

#print(data)
tenancy = "iotdev"
compartment = "InfraDevelopment"
region = "us-ashburn-1"
plane = "dp"
microservice = "microservice-iot-sample"
# deploy.json file from dev-env-config directory.

ms_schema = microservice.replace("-", "_")

print("MS Service : " + ms_schema)

flyway_table_name = ms_schema + "_flyway_schema_history"
print("Flyway schema history: " + flyway_table_name)

resource = {}
for i in range(len(data)):
    if data[i]["type"] == "atp" and "plane" in data[i]["properties"]:
        if (data[i]["properties"]["tenancy"] == tenancy 
            and data[i]["properties"]["compartment"] == compartment 
            and data[i]["properties"]["region"] == region
            and data[i]["properties"]["plane"] == plane):
                resource = data[i]
                break

#print(resource)

print("Admin Password: " + str(resource["properties"]["adminPassword"]))
print("Wallet: " + str(resource["properties"]["wallet"]))
print("Service: " + str(resource["properties"]["service"]))
