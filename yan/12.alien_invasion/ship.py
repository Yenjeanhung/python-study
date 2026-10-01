import pygame
import os

class Ship:
    """ 管理飞船的类 """
    def __init__(self, ai_game):
        """ 初始化飞船并设置其初始位置 """
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.screen_rect = self.screen.get_rect()

        # 获取当前脚本所在目录的绝对路径
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # 构建图像文件的完整路径
        image_path = os.path.join(current_dir, 'images', 'ship.bmp')
        # 使用绝对路径加载图像
        self.image = pygame.image.load(image_path)
        
        self.rect = self.image.get_rect()
        # 将每艘新飞船放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 控制飞船移动的像素点
        self.x = float(self.rect.x)
        
        # 移动标志，飞船刚开始时不移动
        self.moving_right = False
        self.moving_left = False

        # 移动标志，飞船刚开始时不移动
    def update(self):
        """ 根据移动标志调整飞船的位置, 并确保飞船不会超出屏幕边界 """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """ 在指定位置绘制飞船 """
        self.screen.blit(self.image, self.rect)