# -*- coding: utf-8 -*-

import yaml


with open('../config.yaml', 'r') as stream:
    configuration = yaml.load(stream)

url = '{protocol}://{hostname}:{port}/api/{api_version}/map?bbox='.format(**configuration)
