import pygame
import os
from pygame.sprite import Sprite

class Alien(Sprite):
    """ 表示单个外星人的类 """
    def __init__(self, ai_game):
        """ 初始化外星人并设置其初始位置 """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 获取当前脚本所在目录的绝对路径
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # 构建图像文件的完整路径
        image_path = os.path.join(current_dir, 'images', 'alien.bmp')
        # 使用绝对路径加载图像
        self.image = pygame.image.load(image_path)

        self.rect = self.image.get_rect()