# coding:utf-8

import os
import yaml


class Confiig(object):

    def __init__(self):
        # todo 改为定时加载
        try:
            with open(os.path.abspath('config.yaml')) as f:
                self.config = yaml.load(f)
        except FileNotFoundError:
            raise

    @property
    def captcha(self):
        return self.config['captcha_generator']

    @property
    def captcha_size(self):
        return self.captcha['captcha_size']

    @property
    def path(self):
        return self.captcha['path']

    @property
    def image_type(self):
        return self.captcha['image_type']

    @property
    def text(self):
        return self.captcha['text']


config = Confiig()