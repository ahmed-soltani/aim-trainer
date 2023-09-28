import math
import random
import time
import pygame
pygame.init()

WIDTH, HEIGHT= 600, 400 #might use 800 x 600 for bigger screens

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer") #name of the window

def main():
	run = True

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				break

	pygame.quit()

if __name__ == "__main__":
	main()