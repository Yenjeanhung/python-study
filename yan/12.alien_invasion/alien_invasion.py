import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

""" 创建一个空的Pygame窗口 """
class AlienInvasion:
    
    def __init__(self):
        """ 初始化游戏，创建游戏资源 """
        pygame.init()
        self.clock = pygame.time.Clock()

        # 设置背景的宽高
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # 创建一艘飞船
        self.ship = Ship(self)

        # 创建子弹
        self.bullets = pygame.sprite.Group()

        # 创建外星人
        self.aliens = pygame.sprite.Group()
        self._create_fleet()


        # 设置背景色
        self.bg_color = (230, 230, 230)

    """ 开始游戏的主循环 """
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            self.clock.tick(60)

    """ 响应按键和鼠标事件 """
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # 响应按键事件
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_up_events(event)

 
        
    # 键盘按下事件
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # 按Q退出游戏
        elif event.key == pygame.K_q:
            sys.exit()
        # 按空格发送子弹
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            


    # 键盘释放事件
    def _check_up_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
                    
    """ 更新屏幕上的图像，并切换到新屏幕 """
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        # 绘制飞船
        self.ship.blitme()
        # 绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 绘制外星人
        self.aliens.draw(self.screen)
        
        # 让最近绘制的屏幕可见
        pygame.display.flip()     

    def _fire_bullet(self):
        """ 创建子弹 """
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
        
    """ 创建外星人群 """
    def _create_fleet(self):
        # 创建一个外星人,并计算一行可以容纳多少个外星人
        alien = Alien(self)
        alien.width = alien.rect.width
        current_x = alien.width

        # 一起加到容纳不下一个外星人
        while current_x < (self.settings.screen_width - 2 * alien.width):
            self._create_alien(current_x)
            # 每个外星人之间的间距为一个外星人的宽度
            current_x += 2 * alien.width

    """ 创建外星人 """
    def _create_alien(self, x_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        self.aliens.add(new_alien)



if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()