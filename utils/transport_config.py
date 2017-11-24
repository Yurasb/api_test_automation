# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from utils.config_loader import ConfigLoader


# noinspection PyClassHasNoInit
class AbstractConfig:
    __metaclass__ = ABCMeta

    @abstractmethod
    def base_url(self):
        raise NotImplementedError('You should implement this!')


# noinspection PyClassHasNoInit
class HttpConfig(AbstractConfig):
    def base_url(self):
        loaded_config = ConfigLoader('HTTP')
        configuration = loaded_config.load_config()
        base_url = '{protocol}://{hostname}:{port}/api/{api_version}/map?bbox='.format(**configuration)
        return base_url


# noinspection PyClassHasNoInit
class ConfigFactory:
    def get_config(self, transport):
        if transport == 'http':
            return HttpConfig()
        else:
            raise NotImplementedError('Unknown transport')
