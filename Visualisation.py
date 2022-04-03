import pygame
import time
import multiprocessing
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
size_y = 1000
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

    def draw_panel(self):
        pygame.draw.rect(screen,WHITE,[self.star_position_x,self.star_position_y,self.size_x,self.size_y],2)
        font = pygame.font.Font('freesansbold.ttf', 15)
        render_text = font.render(self.text, 1, WHITE)
        size_for_text_x, size_for_text_y = font.size(self.text)
        pygame.draw.rect(screen,BLACK,(self.star_position_x + self.size_x // 2 - size_for_text_x // 2 - 10,self.star_position_y - 6, size_for_text_x + 20,size_for_text_y + 6))
        screen.blit(render_text, (self.star_position_x + self.size_x // 2 - size_for_text_x // 2, self.star_position_y - 4 ))

    def visualize_sorting(self):
        if not self.is_solved:
            for i in range(len(self.list_for_sorting)):

                min = i
                for j in range(i + 1, len(self.list_for_sorting)):
                    screen.fill(BLACK)
                    self.draw_panel()
                    pygame.draw.rect(screen, BLUE,[self.star_position_x + j * 2 + 10 + j * 3, self.size_y + self.star_position_y - 5, 4, - self.list_for_sorting[j] * 3])
                    if self.list_for_sorting[min] > self.list_for_sorting[j]:
                        min = j
                    for x in range(len(self.list_for_sorting)):
                        if x < i:
                            pygame.draw.rect(screen, GREEN,[self.star_position_x + x * 2 + 10 + x * 3, self.size_y + self.star_position_y - 5, 4, - self.list_for_sorting[x] * 3])
                        elif x >= i and x != min and x != j:
                            pygame.draw.rect(screen, WHITE, [self.star_position_x + x * 2 + 10 + x * 3,self.size_y + self.star_position_y - 5, 4, - self.list_for_sorting[x] * 3])
                        elif x == min:
                            pygame.draw.rect(screen, RED,[self.star_position_x + x * 2 + 10 + x * 3, self.size_y + self.star_position_y - 5, 4, - self.list_for_sorting[x] * 3])
                    clock.tick(60)
                    pygame.display.update()
                self.list_for_sorting[i], self.list_for_sorting[min] = self.list_for_sorting[min], self.list_for_sorting[i]
            screen.fill(BLACK)
            self.draw_panel()
            for x in range(len(self.list_for_sorting)):
                 pygame.draw.rect(screen, GREEN,[self.star_position_x + x * 2 + 10 + x * 3, self.size_y + self.star_position_y - 5, 4,- self.list_for_sorting[x] * 3])
            pygame.display.update()
            self.is_solved = True
        else:
            screen.fill(BLACK)
            self.draw_panel()
            for x in range(len(self.list_for_sorting)):
                pygame.draw.rect(screen, GREEN,[self.star_position_x + x * 2 + 10 + x * 3, self.size_y + self.star_position_y - 5, 4,- self.list_for_sorting[x] * 3])
            pygame.display.update()

class Bubble_Sort():
    def __init__(self,list):
        self.list_for_sorting = deepcopy(list)
        self.star_position_x = 540
        self.star_position_y = 10
        self.text = "Bubble Sort"
        self.size_x = 520
        self.size_y = 320
        self.is_solved = False

    def draw_panel(self):
        pygame.draw.rect(screen, WHITE, [self.star_position_x, self.star_position_y, self.size_x, self.size_y], 2)
        font = pygame.font.Font('freesansbold.ttf', 15)
        render_text = font.render(self.text, 1, WHITE)
        size_for_text_x, size_for_text_y = font.size(self.text)
        pygame.draw.rect(screen, BLACK, (
        self.star_position_x + self.size_x // 2 - size_for_text_x // 2 - 10, self.star_position_y - 6,
        size_for_text_x + 20, size_for_text_y + 6))
        screen.blit(render_text,(self.star_position_x + self.size_x // 2 - size_for_text_x // 2, self.star_position_y - 4))

    def visualize_sort(self):
        if not self.is_solved:
            for i in range(len(self.list_for_sorting)):
                for j in range(0, len(self.list_for_sorting) - i - 1):
                    screen.fill(BLACK)
                    self.draw_panel()
                    pygame.draw.rect(screen, BLUE,[self.star_position_x + j * 2 + 10 + j * 3, self.size_y + self.star_position_y - 5,4, - self.list_for_sorting[j] * 3])
                    pygame.draw.rect(screen, BLUE,[self.star_position_x + (j+1) * 2 + 10 + (j+1) * 3, self.size_y + self.star_position_y - 5,4, - self.list_for_sorting[j+1] * 3])
                    if self.list_for_sorting[j] > self.list_for_sorting[j + 1]:
                        self.list_for_sorting[j], self.list_for_sorting[j + 1] = self.list_for_sorting[j + 1],self.list_for_sorting[j]
                        pygame.draw.rect(screen, RED, [self.star_position_x + (j+1) * 2 + 10 + (j+1) * 3,self.size_y + self.star_position_y - 5, 4,- self.list_for_sorting[j+1] * 3])
                    for x in range(len(self.list_for_sorting)):
                        if x != (j+1) and x < (len(self.list_for_sorting) - i):
                            pygame.draw.rect(screen, WHITE, [self.star_position_x + x * 2 + 10 + x * 3,self.size_y + self.star_position_y - 5, 4,- self.list_for_sorting[x] * 3])
                        elif x >= (len(self.list_for_sorting) - i):
                            pygame.draw.rect(screen, GREEN, [self.star_position_x + x * 2 + 10 + x * 3,self.size_y + self.star_position_y - 5, 4,- self.list_for_sorting[x] * 3])
                    clock.tick(60)
                    pygame.display.update()
            screen.fill(BLACK)
            self.draw_panel()
            for x in range(len(self.list_for_sorting)):
                pygame.draw.rect(screen, GREEN,[self.star_position_x + x * 2 + 10 + x * 3, self.size_y + self.star_position_y - 5, 4,- self.list_for_sorting[x] * 3])
            pygame.display.update()
            self.is_solved = True
        else:
            screen.fill(BLACK)
            self.draw_panel()
            for x in range(len(self.list_for_sorting)):
                pygame.draw.rect(screen, GREEN,[self.star_position_x + x * 2 + 10 + x * 3, self.size_y + self.star_position_y - 5, 4,- self.list_for_sorting[x] * 3])
            pygame.display.update()

class Insertion_sort():
    def __init__(self,list):
        self.list_for_sorting = deepcopy(list)
        self.star_position_x = 1070
        self.star_position_y = 10
        self.text = "Insertion Sort"
        self.size_x = 520
        self.size_y = 320
        self.is_solved = False

    def draw_panel(self):
        pygame.draw.rect(screen, WHITE, [self.star_position_x, self.star_position_y, self.size_x, self.size_y], 2)
        font = pygame.font.Font('freesansbold.ttf', 15)
        render_text = font.render(self.text, 1, WHITE)
        size_for_text_x, size_for_text_y = font.size(self.text)
        pygame.draw.rect(screen, BLACK, (
        self.star_position_x + self.size_x // 2 - size_for_text_x // 2 - 10, self.star_position_y - 6,
        size_for_text_x + 20, size_for_text_y + 6))
        screen.blit(render_text,(self.star_position_x + self.size_x // 2 - size_for_text_x // 2, self.star_position_y - 4))

    def visualize_sort(self):
        if not self.is_solved:
            for i in range(len(self.list_for_sorting)):
                key = self.list_for_sorting[i]
                #pygame.draw.rect(screen,RED,[self.star_position_x + i * 2 + 10 + i * 3,self.size_y + self.star_position_y - 5, 4,- self.list_for_sorting[i] * 3])
                j = i - 1
                while j >= 0 and key < self.list_for_sorting[j]:
                    self.list_for_sorting[j + 1] = self.list_for_sorting[j]
                    screen.fill(BLACK)
                    self.draw_panel()
                    for x in range(len(self.list_for_sorting)):
                        if x != j and x != i and x > i:
                            pygame.draw.rect(screen, WHITE, [self.star_position_x + x * 2 + 10 + x * 3,self.size_y + self.star_position_y - 5, 4,- self.list_for_sorting[x] * 3])
                        elif x != j and x != i and x < i:
                            pygame.draw.rect(screen, GREEN, [self.star_position_x + x * 2 + 10 + x * 3,self.size_y + self.star_position_y - 5, 4,- self.list_for_sorting[x] * 3])
                        elif x == j:
                            pygame.draw.rect(screen, RED, [self.star_position_x + x * 2 + 10 + x * 3,self.size_y + self.star_position_y - 5, 4,- self.list_for_sorting[x] * 3])
                        elif x == i:
                            pygame.draw.rect(screen, BLUE, [self.star_position_x + x * 2 + 10 + x * 3,self.size_y + self.star_position_y - 5, 4,- self.list_for_sorting[x] * 3])
                    clock.tick(60)
                    pygame.display.update()
                    j = j - 1
                self.list_for_sorting[j + 1] = key
            screen.fill(BLACK)
            self.draw_panel()
            for x in range(len(self.list_for_sorting)):
                pygame.draw.rect(screen, GREEN, [self.star_position_x + x * 2 + 10 + x * 3,self.size_y + self.star_position_y - 5, 4,- self.list_for_sorting[x] * 3])
            pygame.display.update()
            self.is_solved = True
        else:
            screen.fill(BLACK)
            self.draw_panel()
            for x in range(len(self.list_for_sorting)):
                pygame.draw.rect(screen, GREEN,[self.star_position_x + x * 2 + 10 + x * 3, self.size_y + self.star_position_y - 5, 4,- self.list_for_sorting[x] * 3])
            pygame.display.update()



Selection_Sort = Selection_Sort(list_for_sorting)
Bubble_Sort = Bubble_Sort(list_for_sorting)
Insertion_sort = Insertion_sort(list_for_sorting)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    Insertion_sort.visualize_sort()
