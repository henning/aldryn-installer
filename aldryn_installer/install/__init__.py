# -*- coding: utf-8 -*-
import pip


def parse(config_data):
    pass


def requirements(requirements, is_file=False):
    if is_file:
        args = ['install', '-r', requirements]
    else:
        args = ['install', requirements]
    command = pip.main(args)