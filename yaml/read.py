# Read yaml
import json
import yaml
import ruamel.yaml

def usePyYaml(baseConfigString):
    baseConfigDict = yaml.safe_load(baseConfigString)
    print("Base config dict")
    print(baseConfigDict)

    dump = yaml.dump(baseConfigDict,
                     default_flow_style=False,
                     default_style='"',
                     indent=2,
                     width=50)
    print()
    print("Base config String after updates")
    print(dump)
    return dump


def usingRuamel(baseConfigString):

    return dump


def main():
    baseConfigKey = "base-config.yaml"
    configmapPostFile = "resources/configmap_post.json"
    configmapOutput = "resources/configmap_output.json"

    with open(configmapPostFile, "r") as jsonFile:
        configmap = json.load(jsonFile)
    print(configmap)

    baseConfigString = configmap["data"][baseConfigKey]
    print("Base config file String: ")
    print(baseConfigString)

    # Using pyyaml
    dump = usePyYaml(baseConfigString)

    configmap["data"][baseConfigKey] = dump

    print()
    print("Configmap after updates")
    print(configmap)

    with open(configmapOutput, "w") as jsonFile:
        json.dump(configmap, jsonFile)

main()