import os
import shutil

def printMessage(directory, message):
    print(message + directory)


def list_files(directory):
    file_list = []
    all_files = os.listdir(directory)
    for i in range(len(all_files)):
        file_dict = {}
        file_dict["name"] = all_files[i]
        file_list.append(file_dict)
    return file_list


def directory_exists(directory, message, log=True):
    if os.path.isdir(directory):
        if log:
            printMessage(directory, message)
        return True
    else:
        if log:
            raise FileNotFoundError
    return False


def file_exists(path):
    if os.path.isfile(path):
        return True
    return False


def create_directory(path):
    if not directory_exists(path, '', False):
        os.makedirs(path)


def copy_file(src, dest):
    if not file_exists(dest):
        shutil.copyfile(src, dest)


def main():
    home_directory = os.environ["HOME"]
    print("Home directory: " + home_directory)

    grade_directory = home_directory + "/.gradle"
    directory_exists(grade_directory, "Gradle directory: ")

    cache_directory = grade_directory + "/caches"
    directory_exists(cache_directory, "Cache directory : ")

    modules_directory = cache_directory + "/modules-2"
    directory_exists(modules_directory, "Modules Directory: ")

    files_directory = modules_directory + "/files-2.1"
    directory_exists(files_directory, "Files Directory: ")

    maven_home = home_directory + "/.m2"
    directory_exists(maven_home, "Maven Home Directory: ")

    repository_directory = maven_home + "/repository"
    directory_exists(repository_directory, "Maven Repository Directory: ")

    # Get all Group IDs
    artifacts = {}
    group_ids_key = "group_ids"
    artifacts[group_ids_key] = list_files(files_directory)
    print("Number of group ids: " + str(len(artifacts[group_ids_key])))

    print("Copying all dependencies.")
    for i in range(len(artifacts[group_ids_key])):
        group_id_directory = files_directory + "/" + artifacts[group_ids_key][i]["name"]
        if directory_exists(group_id_directory, "", False):
#             printMessage(artifacts[group_ids_key][i]["name"], "Group id exists: ")
            repo_group_id_directory = repository_directory + "/" + artifacts[group_ids_key][i]["name"].replace('.', '/')
#             print("Directory to create: " + repo_group_id_directory)
            create_directory(repo_group_id_directory)

            # Time to get artifacts
            all_artifacts_in_group = list_files(group_id_directory)
            for j in range(len(all_artifacts_in_group)):
                artifact_directory = group_id_directory + "/" + all_artifacts_in_group[j]["name"]
                if directory_exists(artifact_directory, '', False):
#                     printMessage(all_artifacts_in_group[j]['name'], "\tArtifact exists: ")
                    repo_artifact_id_directory = repo_group_id_directory + "/" + all_artifacts_in_group[j]['name']
#                     print("\tDirectory to create: " + repo_artifact_id_directory)
                    create_directory(repo_artifact_id_directory)

                    # Time to get versions
                    all_versions_in_artifact = list_files(artifact_directory)
                    for k in range(len(all_versions_in_artifact)):
                        version_directory = artifact_directory + "/" + all_versions_in_artifact[k]["name"]
                        if directory_exists(version_directory, '', False):
#                             printMessage(all_versions_in_artifact[k]["name"], "\t\tVersion Exists: ")
                            repo_version_directory = repo_artifact_id_directory + "/" + all_versions_in_artifact[k]["name"]
#                             print("\t\tDirectory to create: " + repo_version_directory)
                            create_directory(repo_version_directory)

                            # Time to get hash
                            all_hash_in_version = list_files(version_directory)
                            for l in range(len(all_hash_in_version)):
                                hash_directory = version_directory + "/" + all_hash_in_version[l]["name"]
                                if directory_exists(hash_directory, '', False):
#                                     printMessage(all_hash_in_version[l]["name"], "\t\t\tHash Exists: ")

                                    all_files_in_hash = list_files(hash_directory)
                                    for m in range(len(all_files_in_hash)):
                                        repository_file = hash_directory + "/" + all_files_in_hash[m]["name"]
                                        if file_exists(repository_file):
#                                             printMessage(all_files_in_hash[m]["name"], "\t\t\t\tFile Exists: ")
                                            repo_file_path = repo_version_directory + "/" + all_files_in_hash[m]["name"]
#                                             print("\t\t\t\tFile copy to: " + repo_file_path)
#                                             print("\t\t\t\tFile copy from: " + repository_file)
                                            copy_file(repository_file, repo_file_path)
#         print()
    print("Done.")

main()
