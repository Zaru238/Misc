import os
import shutil
import sys
import subprocess

import docker
import json
import tarfile


HOST_WORKSPACE="/home/kziabrev/workspace"
DOCKER_WORKSPACE="/workspace"

CONTAINER_NAME = "container_name"

BUILD_DIR = "build"

PROJECT_NAME="favorites"

DOCKER_INCLUDE_DIR = "/usr/include"
HOST_INCLUDE_DIR = f"{HOST_WORKSPACE}/docker_include"


def perform_docker_project_command(command):
    _, stream = container.exec_run(command, workdir=f"{DOCKER_WORKSPACE}/{PROJECT_NAME}/{BUILD_DIR}", stream=True)

    for line in stream:
        print(line.decode('utf-8').replace(DOCKER_WORKSPACE, HOST_WORKSPACE), end="")


def default():
    if not os.path.exists(BUILD_DIR):
        os.mkdir(BUILD_DIR)

    perform_docker_project_command("cmake ..")
    perform_docker_project_command("make")


def test():
    default()

    perform_docker_project_command("make test")


def component_test():
    default()

    perform_docker_project_command("make component-test")


def codeformat():
    perform_docker_project_command("cmake ..")
    perform_docker_project_command("make codeformat")


def clean():
    perform_docker_project_command(f"rm -rf {DOCKER_WORKSPACE}/{PROJECT_NAME}/{BUILD_DIR}")
    print("Done!")


def update_headers():
    TEMP_TAR_FILE = "/tmp/include.tar"

    print("Fetching header files from docker")

    with open(TEMP_TAR_FILE, "wb") as tar_file:
        tar, _ = container.get_archive(f"{DOCKER_INCLUDE_DIR}/.")
        for chunk in tar:
            tar_file.write(chunk)

    if os.path.isdir(HOST_INCLUDE_DIR):
        shutil.rmtree(HOST_INCLUDE_DIR)

    with tarfile.open(TEMP_TAR_FILE, "r") as tar_file:
        tar_file.extractall(f"{HOST_INCLUDE_DIR}/usr/include")

    os.remove(TEMP_TAR_FILE)

    print("Done!")


def generate_compile_commands():
    COMPILE_COMMAND_FILE = "compile_commands.json"

    BUILD_COMMAND_FILE_LOCATION = f"{HOST_WORKSPACE}/{PROJECT_NAME}/{BUILD_DIR}/{COMPILE_COMMAND_FILE}"
    PROJECT_COMMAND_FILE_LOCATION = f"{HOST_WORKSPACE}/{PROJECT_NAME}/{COMPILE_COMMAND_FILE}"

    REPLACE_TABLE = ((DOCKER_WORKSPACE, HOST_WORKSPACE),
            ("/usr", f"{HOST_INCLUDE_DIR}/usr"))

    if not os.path.exists(BUILD_DIR):
        os.mkdir(BUILD_DIR)

    perform_docker_project_command("cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON ..")

    shutil.copyfile(BUILD_COMMAND_FILE_LOCATION, PROJECT_COMMAND_FILE_LOCATION)

    with open(PROJECT_COMMAND_FILE_LOCATION, "r") as file:
        content = file.read()

    for pair in REPLACE_TABLE:
        content = content.replace(pair[0], pair[1])

    json_content = json.loads(content)

    EXTRA_ARGUMENTS = f" --sysroot={HOST_INCLUDE_DIR} \
-isystem {HOST_INCLUDE_DIR}/usr/include/c++/10.1.0/some_path \
-isystem {HOST_INCLUDE_DIR}/usr/include/c++/10.1.0"

    for tr_unit in json_content:
        tr_unit["command"] += EXTRA_ARGUMENTS

    with open(PROJECT_COMMAND_FILE_LOCATION, "w") as file:
        json.dump(json_content, file, indent=2)

    print("Done!")


client = docker.from_env()
container = client.containers.get(CONTAINER_NAME)

if len(sys.argv) == 1:
    default()
else:
    locals()[sys.argv[1]](*sys.argv[2:])
