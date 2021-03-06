# -*- coding: utf-8 -*-


import yaml


with open('../config.yaml', 'r') as stream:
    configuration = yaml.load(stream)

url = configuration['protocol'] +\
      '://' +\
      configuration['hostname'] +\
      ':' +\
      configuration['port'] +\
      '/api/' + \
      configuration['api_version']
