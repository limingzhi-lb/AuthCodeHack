# coding:utf-8
import random
from captcha.image import ImageCaptcha

from config import config


class Captcha(ImageCaptcha):
    """
    用于生成验证码
    """
    def __init__(self, charset, captcha_size=config.captcha_size, width=160, height=60, fonts=None, font_sizes=None):
        """

        :param charset: 参与生成验证码的字符列表, [1, 2, 3, 'a', 'c']
        :param captcha_size:
        :param width:
        :param height:
        :param fonts:
        :param font_sizes:
        """
        super(Captcha, self).__init__(width=width, height=height, fonts=fonts, font_sizes=font_sizes)
        self.charset = charset
        self.captcha_size = captcha_size

    def generate_text(self):
        captcha_text = []
        for _ in range(self.captcha_size):
            c = random.choice(self.charset)
            captcha_text.append(str(c))
        return ''.join(captcha_text)

    def generate_and_save_image(self, num=1, path=config.path):
        for _ in range(num):
            text = self.generate_text()
            self.write(text, '{}/{}.jpg'.format(path, text))
            yield self.generate(text)



if __name__ == '__main__':
    captcha = Captcha(config.text['number'])
    captcha.generate_and_save_image(num=1)
