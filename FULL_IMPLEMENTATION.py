import pkg_resources
pkg_resources.require("pygame==2.0.0")
import pygame
import time

import random
from copy import deepcopy


list_for_sorting = []
len_of_sorting_list = 100

WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

size_x = 1600
size_y = 350
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((size_x,size_y))
pygame.display.set_caption("Sorting")


for i in range(1,len_of_sorting_list+1):
    list_for_sorting.append(i)

random.shuffle(list_for_sorting)

class Selection_Sort():
    def __init__(self,list):
        self.list_for_sorting = deepcopy(list)
        self.star_position_x = 10
        self.star_position_y = 10
        self.text = "Selection Sort"
        self.size_x = 520
        self.size_y = 320
        self.is_solved = False
        self.surface = pygame.Surface([530,330])
        self.frames = []
        self.current_i = 0
        self.current_j = 0
        self.current_frame = 0
        self.current_min = 0

    def draw_panel(self):
        pygame.draw.rect(self.surface,WHITE,[self.star_position_x,self.star_position_y,self.size_x,self.size_y],2)
        font = pygame.font.Font('freesansbold.ttf', 15)
        render_text = font.render(self.text, 1, WHITE)
        size_for_text_x, size_for_text_y = font.size(self.text)
        pygame.draw.rect(self.surface,BLACK,(self.star_position_x + self.size_x // 2 - size_for_text_x // 2 - 10,self.star_position_y - 6, size_for_text_x + 20,size_for_text_y + 6))
        self.surface.blit(render_text, (self.star_position_x + self.size_x // 2 - size_for_text_x // 2, self.star_position_y - 4 ))

    def visualize_sorting(self):
        if not self.is_solved:
            if self.current_j == 0 and self.current_i == 0:
                self.current_min = self.current_i
            elif self.current_j == len(self.list_for_sorting):
                self.current_i += 1
                self.current_j = self.current_i + 1
                self.current_min = self.current_i

            self.surface.fill(BLACK)
            self.draw_panel()
            pygame.draw.rect(self.surface, BLUE,[self.star_position_x + self.current_j * 2 + 10 + self.current_j * 3, self.size_y + self.star_position_y - 5, 4, - self.list_for_sorting[self.current_j] * 3])
            if self.list_for_sorting[self.current_min] > self.list_for_sorting[self.current_j]:
                self.current_min = self.current_j
            for x in range(len(self.list_for_sorting)):
                if x < self.current_i:
                    pygame.draw.rect(self.surface, GREEN,[self.star_position_x + x * 2 + 10 + x * 3, self.size_y + self.star_position_y - 5, 4, - self.list_for_sorting[x] * 3])
                elif x >= self.current_i and x != self.current_min and x != self.current_j:
                    pygame.draw.rect(self.surface, WHITE, [self.star_position_x + x * 2 + 10 + x * 3,self.size_y + self.star_position_y - 5, 4, - self.list_for_sorting[x] * 3])
                elif x == self.current_min:
                    pygame.draw.rect(self.surface, RED,[self.star_position_x + x * 2 + 10 + x * 3, self.size_y + self.star_position_y - 5, 4, - self.list_for_sorting[x] * 3])
            screen.blit(self.surface,(0,0))

            self.current_j += 1
            if self.current_j == len(self.list_for_sorting):
                self.list_for_sorting[self.current_i], self.list_for_sorting[self.current_min] = self.list_for_sorting[self.current_min], self.list_for_sorting[self.current_i]

            if self.current_i == (len(self.list_for_sorting) - 2):
                self.surface.fill(BLACK)
                self.draw_panel()
                for x in range(len(self.list_for_sorting)):
                    pygame.draw.rect(self.surface, GREEN,[self.star_position_x + x * 2 + 10 + x * 3, self.size_y + self.star_position_y - 5, 4,- self.list_for_sorting[x] * 3])
                screen.blit(self.surface, (0, 0))
                self.is_solved = True
        else:
            self.surface.fill(BLACK)
            self.draw_panel()
            for x in range(len(self.list_for_sorting)):
                pygame.draw.rect(self.surface, GREEN,[self.star_position_x + x * 2 + 10 + x * 3, self.size_y + self.star_position_y - 5, 4,- self.list_for_sorting[x] * 3])
            screen.blit(self.surface, (0, 0))

class Bubble_Sort():
    def __init__(self,list):
        self.list_for_sorting = deepcopy(list)
        self.star_position_x = 0
        self.star_position_y = 10
        self.text = "Bubble Sort"
        self.size_x = 520
        self.size_y = 320
        self.is_solved = False
        self.current_i = 0
        self.current_j = 0
        self.bubble_surface = pygame.Surface([530, 330])


    def draw_panel(self):
        pygame.draw.rect(self.bubble_surface, WHITE, [self.star_position_x, self.star_position_y, self.size_x, self.size_y], 2)
        font = pygame.font.Font('freesansbold.ttf', 15)
        render_text = font.render(self.text, 1, WHITE)
        size_for_text_x, size_for_text_y = font.size(self.text)
        pygame.draw.rect(self.bubble_surface, BLACK, (self.star_position_x + self.size_x // 2 - size_for_text_x // 2 - 10, self.star_position_y - 6,size_for_text_x + 20, size_for_text_y + 6))
        self.bubble_surface.blit(render_text,(self.star_position_x + self.size_x // 2 - size_for_text_x // 2, self.star_position_y - 4))

    def visualize_sort(self):
        if not self.is_solved:
            if self.current_j == (len(self.list_for_sorting) - self.current_i - 1):
                self.current_i += 1
                self.current_j = 0

            self.bubble_surface.fill(BLACK)
            self.draw_panel()
            pygame.draw.rect(self.bubble_surface, BLUE,[self.star_position_x + self.current_j * 2 + 10 + self.current_j * 3, self.size_y + self.star_position_y - 5,4, - self.list_for_sorting[self.current_j] * 3])
            pygame.draw.rect(self.bubble_surface, BLUE,[self.star_position_x + (self.current_j+1) * 2 + 10 + (self.current_j+1) * 3, self.size_y + self.star_position_y - 5,4, - self.list_for_sorting[self.current_j+1] * 3])
            if self.list_for_sorting[self.current_j] > self.list_for_sorting[self.current_j + 1]:
                self.list_for_sorting[self.current_j], self.list_for_sorting[self.current_j + 1] = self.list_for_sorting[self.current_j + 1],self.list_for_sorting[self.current_j]
                pygame.draw.rect(self.bubble_surface, RED, [self.star_position_x + (self.current_j+1) * 2 + 10 + (self.current_j+1) * 3,self.size_y + self.star_position_y - 5, 4,- self.list_for_sorting[self.current_j+1] * 3])
            for x in range(len(self.list_for_sorting)):
                if x != (self.current_j+1) and x < (len(self.list_for_sorting) - self.current_i):
                    pygame.draw.rect(self.bubble_surface, WHITE, [self.star_position_x + x * 2 + 10 + x * 3,self.size_y + self.star_position_y - 5, 4,- self.list_for_sorting[x] * 3])
                elif x >= (len(self.list_for_sorting) - self.current_i):
                    pygame.draw.rect(self.bubble_surface, GREEN, [self.star_position_x + x * 2 + 10 + x * 3,self.size_y + self.star_position_y - 5, 4,- self.list_for_sorting[x] * 3])

            screen.blit(self.bubble_surface, (540, 0))
            self.current_j += 1

            if self.current_i == (len(self.list_for_sorting) - 2):
                self.bubble_surface.fill(BLACK)
                self.draw_panel()
                for x in range(len(self.list_for_sorting)):
                    pygame.draw.rect(self.bubble_surface, GREEN,
                                     [self.star_position_x + x * 2 + 10 + x * 3, self.size_y + self.star_position_y - 5,
                                      4, - self.list_for_sorting[x] * 3])
                screen.blit(self.bubble_surface, (540, 0))
                self.is_solved = True
        else:
            self.bubble_surface.fill(BLACK)
            self.draw_panel()
            for x in range(len(self.list_for_sorting)):
                pygame.draw.rect(self.bubble_surface, GREEN,[self.star_position_x + x * 2 + 10 + x * 3, self.size_y + self.star_position_y - 5, 4,- self.list_for_sorting[x] * 3])
            screen.blit(self.bubble_surface, (540, 0))

class Insertion_Sort():
    def __init__(self,list):
        self.list_for_sorting = deepcopy(list)
        self.star_position_x = 0
        #1070 start position x
        self.star_position_y = 10
        self.text = "Insertion Sort"
        self.size_x = 520
        self.size_y = 320
        self.is_solved = False
        self.current_i = 0
        self.current_j = self.current_i - 1
        self.key = self.list_for_sorting[self.current_i]
        self.insertion_sort_surface = pygame.Surface([530, 330])

    def draw_panel(self):
        pygame.draw.rect(self.insertion_sort_surface, WHITE, [self.star_position_x, self.star_position_y, self.size_x, self.size_y], 2)
        font = pygame.font.Font('freesansbold.ttf', 15)
        render_text = font.render(self.text, 1, WHITE)
        size_for_text_x, size_for_text_y = font.size(self.text)
        pygame.draw.rect(self.insertion_sort_surface, BLACK, (
        self.star_position_x + self.size_x // 2 - size_for_text_x // 2 - 10, self.star_position_y - 6,
        size_for_text_x + 20, size_for_text_y + 6))
        self.insertion_sort_surface.blit(render_text,(self.star_position_x + self.size_x // 2 - size_for_text_x // 2, self.star_position_y - 4))

    def visualize_sort(self):
        if not self.is_solved:
            if self.current_i < len(self.list_for_sorting):
                if self.current_j >= 0 and self.key < self.list_for_sorting[self.current_j]:
                    self.list_for_sorting[self.current_j + 1] = self.list_for_sorting[self.current_j]
                    self.insertion_sort_surface.fill(BLACK)
                    self.draw_panel()
                    for x in range(len(self.list_for_sorting)):
                        if x != self.current_j and x != self.current_i and x > self.current_i:
                            pygame.draw.rect(self.insertion_sort_surface, WHITE, [self.star_position_x + x * 2 + 10 + x * 3,
                                                             self.size_y + self.star_position_y - 5, 4,
                                                             - self.list_for_sorting[x] * 3])
                        elif x != self.current_j and x != self.current_i and x < self.current_i:
                            pygame.draw.rect(self.insertion_sort_surface, GREEN, [self.star_position_x + x * 2 + 10 + x * 3,
                                                             self.size_y + self.star_position_y - 5, 4,
                                                             - self.list_for_sorting[x] * 3])
                        elif x == self.current_j:
                            pygame.draw.rect(self.insertion_sort_surface, RED, [self.star_position_x + x * 2 + 10 + x * 3,
                                                           self.size_y + self.star_position_y - 5, 4,
                                                           - self.list_for_sorting[x] * 3])
                        elif x == self.current_i:
                            pygame.draw.rect(self.insertion_sort_surface, BLUE, [self.star_position_x + x * 2 + 10 + x * 3,
                                                            self.size_y + self.star_position_y - 5, 4,
                                                            - self.list_for_sorting[x] * 3])
                    screen.blit(self.insertion_sort_surface,(1070,0))
                    self.current_j = self.current_j - 1
                else:
                    if self.current_i < (len(self.list_for_sorting)-1):
                        self.current_i += 1
                        self.list_for_sorting[self.current_j + 1] = self.key
                        self.key = self.list_for_sorting[self.current_i]
                        self.current_j = self.current_i - 1
                    else:
                        self.list_for_sorting[self.current_j + 1] = self.key
                        self.is_solved = True

                screen.blit(self.insertion_sort_surface,(1070,0))

        else:
            self.insertion_sort_surface.fill(BLACK)
            self.draw_panel()
            for x in range(len(self.list_for_sorting)):
                pygame.draw.rect(self.insertion_sort_surface, GREEN,
                                 [self.star_position_x + x * 2 + 10 + x * 3, self.size_y + self.star_position_y - 5, 4,
                                  - self.list_for_sorting[x] * 3])
            screen.blit(self.insertion_sort_surface, (1070, 0))

Selection_Sort = Selection_Sort(list_for_sorting)
Bubble_Sort = Bubble_Sort(list_for_sorting)
Insertion_Sort = Insertion_Sort(list_for_sorting)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Selection_Sort.visualize_sorting()
    Bubble_Sort.visualize_sort()
    Insertion_Sort.visualize_sort()
    pygame.display.update()
    clock.tick(120)
