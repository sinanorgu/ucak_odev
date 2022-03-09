import pygame
import sys
import math
from color import *
class car():
    ivme = 0.2
    surtunme=0.05
    def __init__(self):
        self.x = 0
        self.y = 0
        self.acı = 0
        self.hız = 0
        self.max_hız = 15
        self.visible=False
    def draw_car(self, pencere , renk=color.kırmızı):
        if self.visible:
            boyut=20
            nokta1 = (self.x + boyut * math.cos(math.radians(self.acı + 30)), self.y - boyut * math.sin(math.radians(self.acı + 30)))
            nokta2 = (self.x + boyut * math.cos(math.radians(self.acı + 150)), self.y - boyut * math.sin(math.radians(self.acı + 150)))
            nokta3 = (self.x + boyut * math.cos(math.radians(self.acı + 210)), self.y - boyut * math.sin(math.radians(self.acı + 210)))
            nokta4 = (self.x + boyut * math.cos(math.radians(self.acı + 330)), self.y - boyut * math.sin(math.radians(self.acı + 330)))


            pygame.draw.line(pencere, color.yeşil, nokta2, nokta1, 2)
            pygame.draw.line(pencere, color.yeşil, nokta2, nokta3, 2)
            pygame.draw.line(pencere, color.yeşil, nokta3, nokta4, 2)
            pygame.draw.line(pencere, renk, nokta4, nokta1, 2)

            self.x += self.hız * math.cos(math.radians(self.acı))
            self.y -= self.hız * math.sin(math.radians(self.acı))


            if self.hız >= 0:
                self.hız -= self.surtunme
                if self.hız < 0:
                    self.hız = 0
            if self.hız <= 0:
                self.hız += self.surtunme
                if self.hız > 0:
                    self.hız = 0
            ###########################################
            if self.x > pygame.display.get_window_size()[0]:
                self.x = 0
            if self.x < 0:
                self.x = pygame.display.get_window_size()[0]
            if self.y > pygame.display.get_window_size()[1]:
                self.y = 0
            if self.y < 0:
                self.y = pygame.display.get_window_size()[1]
            ##################################################
            if self.hız > 0 and self.hız > self.max_hız:
                self.hız = self.max_hız
            elif self.hız < 0 and abs(self.hız) > self.max_hız:
                self.hız = -self.max_hız
            ###################################################
    def sur(self):
        if self.visible:
            tuslar = pygame.key.get_pressed()
            if tuslar[pygame.K_RIGHT] and self.hız:
                self.acı -= 0.8*self.hız

            elif tuslar[pygame.K_LEFT] and self.hız:
                self.acı += 0.8 * self.hız

            if tuslar[pygame.K_UP]:
                if self.hız >= 0:
                    self.hız += self.ivme
                else:
                    self.hız += 2 * self.ivme

            if tuslar[pygame.K_DOWN]:
                if self.hız <= 0:
                    self.hız -= self.ivme
                else:
                    self.hız -= 2 * self.ivme

