# -*- coding: utf-8 -*-

import yaml


class ConfigLoader:
    def __init__(self, protocol):
        self.protocol = protocol

    def load_config(self):
        with open('./config.yaml', 'r') as stream:
            configuration = yaml.load(stream)
            return configuration[self.protocol]
