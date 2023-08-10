import sys
import glob
import json

def main():
    if len(sys.argv) < 1:
        raise Exception("Input Error. Script expects search_directory as an argument.")
    search_directory: str = sys.argv[1]

    relative_path_files: list = glob.glob(search_directory + '/**/*.sql', recursive=True)
    #print(relative_path_files)

    file_names: list = []
    for i in range(len(relative_path_files)):
        name: str = relative_path_files[i]
        file_names.append(name.split("/")[-1])
    #print(file_names)

    versions: list = []
    for i in range(len(file_names)):
        name: str = file_names[i]
        # Get the V1_num_num part
        temp_version: str = name.split('__')[0]

        # Get the 1_num_num part
        temp_version: str = temp_version.split('V')[1]
        
        # Get only the numbers
        temp_version_split: list = temp_version.split('_')

        # Join the numbers with .
        versions.append('.'.join(temp_version_split))

    # Now, we cannot just sort the versions, we will have to preprocess it and sort it.
    max_length_split: int = 0
    max_length_version: int = 0
    for i in range(len(versions)):
        version_split: list = versions[i].split('.')
        if len(version_split) > max_length_split:
            max_length_split = len(version_split)

        # Every major or minor version
        for j in range(len(version_split)):
            minor_version: str = version_split[j]
            if len(minor_version) > max_length_version:
                max_length_version = len(minor_version)

    # print(max_length_split)
    # print(max_length_version)
    # print(versions)

    # To get original values
    versions_dict: dict = {}
    temp_version_array: list = []
    for i in range(len(versions)):
        # Update temp_version
        temp_version: str = versions[i]
        current_length: int = len(temp_version.split('.'))
        while current_length < max_length_split:
            temp_version += ".0"
            current_length += 1
        
        # Now temp_version and verions are of same length
        temp_version_split: list = temp_version.split('.')
        for j in range(len(temp_version_split)):
            temp_minor_version: str = temp_version_split[j]
            current_length: int = len(temp_minor_version)
            while current_length < max_length_version:
                temp_minor_version = "0" + temp_minor_version
                current_length += 1
            temp_version_split[j] = temp_minor_version
            
        temp_version = str("").join(temp_version_split)
        versions_dict[temp_version] = versions[i]
        temp_version_array.append(temp_version)
    
    # print(versions)
    # print(versions_dict)

    temp_version_array.sort()
    # print(temp_version_array)

    data: dict = {}
    data["schemaVersion"] = versions_dict[temp_version_array[-1]]
    print(data)


main()