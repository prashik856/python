import json 

with open("input.json", "r") as inputfile:
    job = json.load(inputfile)

#print(job)

# Remove unnecessary data
metadata = "metadata"
if metadata in job:
    if "creationTimestamp" in job[metadata]:
        job[metadata].pop("creationTimestamp")
    if "generation" in job[metadata]:
        job[metadata].pop("generation")
    if "labels" in job[metadata]:
        if "controller-uid" in job[metadata]["labels"]:
            job[metadata]["labels"].pop("controller-uid")
    if "resourceVersion" in job[metadata]:
        job[metadata].pop("resourceVersion")
    if "uid" in job[metadata]:
        job[metadata].pop("uid")

spec = "spec"
if spec in job:
    if "completionMode" in job[spec]:
        job[spec].pop("completionMode")
    if "selector" in job[spec]:
        job[spec].pop("selector")
    if "suspend" in job[spec]:
        job[spec].pop("suspend")
    
    template = "template"
    if template in job[spec]:
        if metadata in job[spec][template]:
            if "creationTimestamp" in job[spec][template][metadata]:
                job[spec][template][metadata].pop("creationTimestamp")
            if "labels" in job[spec][template][metadata]:
                if "controller-uid" in job[spec][template][metadata]["labels"]:
                    job[spec][template][metadata]["labels"].pop("controller-uid")

if "status" in job:
    job.pop("status")

with open("output.json", "w") as outfile:
    json.dump(job, outfile, indent=4)