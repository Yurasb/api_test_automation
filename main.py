# -*- coding: utf-8 -*-
import yaml


with open('../config.yaml', 'r') as stream:
    configuration = yaml.load(stream)

url = '{}://{}:{}/api/{}/map?bbox='.format(
      configuration['protocol'], configuration['hostname'],
      configuration['port'], configuration['api_version']
)
