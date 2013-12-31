
import pygame as pg

class AIPaddle:
    def __init__(self, screen_rect, ball_rect):
        self.difficulty = 'medium'
        self.screen_rect = screen_rect
        self.ball_Rect = ball_rect
        self.move_up = False
        self.move_down = False
        self.screen_response_area_rect = self.screen_rect
        
        if self.difficulty == 'hard':
            num = 1
        elif self.difficulty == 'medium':
            num = 2
        elif self.difficulty == 'easy':
            num = 3
            
        surf = pg.Surface([self.screen_rect.width / num, self.screen_rect.height])
        self.screen_response_area_rect = surf.get_rect()
        
    def update(self, ball_rect, paddle_rect):
        if self.screen_response_area_rect.colliderect(ball_rect):
            if ball_rect.y < paddle_rect.y:
                self.move_up = True
            elif ball_rect.y > paddle_rect.y:
                self.move_down = True
            
    def reset(self):
        '''reset upon each iteration of update'''
        self.move_up = False
        self.move_down = False
