# coding:utf-8
from captcha.image import ImageCaptcha
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random,time

# 验证码中的字符, 就不用汉字了
number = ['0','1','2','3','4','5','6','7','8','9']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# 验证码一般都无视大小写；验证码长度4个字符
def random_captcha_text(char_set=number+alphabet+ALPHABET, captcha_size=4):
    captcha_text = []
    for i in range(captcha_size):
        c = random.choice(char_set)
        captcha_text.append(c)
    return captcha_text

# 生成字符对应的验证码
def gen_captcha_text_and_image():
    image = ImageCaptcha()

    captcha_text = random_captcha_text()
    captcha_text = ''.join(captcha_text)

    captcha = image.generate(captcha_text)
    image.write(captcha_text, captcha_text + '.jpg')  # 写到文件

    captcha_image = Image.open(captcha)
    captcha_image = np.array(captcha_image)
    return captcha_text, captcha_image


class Captcha(ImageCaptcha):
    def __init__(self, charset, captcha_size=4, width=160, height=60, fonts=None, font_sizes=None):
        super(Captcha, self).__init__(width=width, height=height, fonts=fonts, font_sizes=font_sizes)
        self.charset = charset
        self.captcha_size = captcha_size

    @property
    def text(self):
        captcha_text = []
        for i in range(self.captcha_size):
            c = random.choice(self.charset)
            captcha_text.append(c)
        return ''.join(captcha_text)

    def generate_and_save_image(self):
        captcha = self.generate(self.text)
        self.write(self.text, self.text + '.jpg')
        return captcha

    def process_captcha(self, captcha):
        captcha_image = Image.open(captcha)
        captcha_image = np.array(captcha_image)
        f = plt.figure()
        ax = f.add_subplot(111)
        ax.text(0.1, 0.9, self.text, ha='center', va='center', transform=ax.transAxes)
        plt.imshow(captcha_image)

if __name__ == '__main__':
    # while True:
    #     text, image = gen_captcha_text_and_image()
    #     print('begin ',time.ctime(),type(image))
    #     f = plt.figure()
    #     ax = f.add_subplot(111)
    #     ax.text(0.1, 0.9,text, ha='center', va='center', transform=ax.transAxes)
    #     plt.imshow(image)

        # plt.show()
        # print('end ',time.ctime())
    captcha = Captcha(['0', '1', '2', '3'])
    _captcha = captcha.generate_and_save_image()
    captcha.process_captcha(_captcha)