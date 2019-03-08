#!/usr/bin/python3.5

import os
import yaml


def get_download_content():
    full_path = str(os.getcwd())
    user_dir, a, b = full_path.rsplit("/", maxsplit=2)
    os.chdir(user_dir+"/Downloads")
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime, reverse=True)
    return files


def get_desired_yml(files):
    for file in files:
        if str(file).endswith(("yaml", "yml")) is True:
            break
    return file


def open_file(file):
    with open(file) as opf:
        yml_file = yaml.load(opf)
        for main_cat in yml_file:
            senzors, fmc = create_device_list(main_cat, yml_file)
        print(fmc)
        print(senzors)


def create_device_list(devises, yml_file):
    senzors = []
    fmc =[]
    for device in yml_file[devises]:
        if device.startswith("sen") is True:
            senzors.append(yml_file[devises][device])
        elif device.startswith("fm") is True:
            fmc.append(yml_file[devises][device])
    return senzors, fmc




def execute_scr():
    files = get_download_content()
    file = get_desired_yml(files)
    open_file(file)


execute_scr()