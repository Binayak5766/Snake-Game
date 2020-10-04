import pygame, time, random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
blue = (50, 153, 213)
red = (213, 50, 80)
black = (0, 0, 0)
green = (0, 255, 0)

dis_width = 600
dis_height = 400
movement = [" "]

dis = pygame.display.set_mode((dis_width,dis_height))          #Creates the play area
pygame.display.set_caption("Snake Game developed with Edureka")

clock = pygame.time.Clock()

snake_speed = 25
snake_block = 10

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
	value = score_font.render("Your Score: " + str(score), True, yellow)
	dis.blit(value, [0, 0])

def our_snake(snake_block, snake_List):
	for x in snake_List:
		pygame.draw.rect(dis, black, [int(x[0]), int(x[1]), snake_block, snake_block])

def message(msg, color):                   #This function displays the message on the screen.
	mesg = font_style.render(msg, True, color)
	dis.blit(mesg, [int(dis_width/6), int(dis_height/3)])


def gameloop():
	game_over = False
	game_close = False

	x1 = dis_width / 2
	y1 = dis_height / 2

	snake_List = []
	Length_of_snake = 1

	x1_change = 0
	y1_change = 0

	foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
	foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

	foodx_special = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
	foody_special = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

	while not game_over:                        #This is the game loop.

		while game_close == True:
			dis.fill(blue)
			message("You lost! Press Q-Quit or C-Play again", red)
			your_score(Length_of_snake - 1)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						game_over = True
						game_close = False
					if event.key == pygame.K_c:
						gameloop()


		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:                #To stop the movement in opposite direction directly.
				if event.key == pygame.K_LEFT:
					movement.append("left")
				elif event.key == pygame.K_RIGHT:
					movement.append("right")
				elif event.key == pygame.K_UP:
					movement.append("top")
				elif event.key == pygame.K_DOWN:
					movement.append("down")

			if event.type == pygame.QUIT:
				game_over = True                      #Sets the game_over variable to True and quits the screen when button is pressed.

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					if movement[-2] == "right":
						pass
					else:
						x1_change = -snake_block
						y1_change = 0

				elif event.key == pygame.K_RIGHT:
					if movement[-2] == "left":
						pass
					else:
						x1_change = snake_block
						y1_change = 0

				elif event.key == pygame.K_UP:
					if movement[-2] == "down":
						pass
					else:
						x1_change = 0
						y1_change = -snake_block

				elif event.key == pygame.K_DOWN:
					if movement[-2] == "top":
						pass
					else:
						x1_change = 0
						y1_change = snake_block

		if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
			game_close = True

		x1 += x1_change
		y1 += y1_change
		dis.fill(blue)

		pygame.draw.rect(dis, green, [int(foodx), int(foody), snake_block, snake_block])         #Creating the food
		if (Length_of_snake - 1) % 5 == 0 and (Length_of_snake - 1) > 0:
			pygame.draw.ellipse(dis, white, [int(foodx_special), int(foody_special), snake_block, snake_block])


		snake_Head = []
		snake_Head.append(x1)
		snake_Head.append(y1)
		snake_List.append(snake_Head)

		if len(snake_List) > Length_of_snake:
			del snake_List[0]

		for x in snake_List[:-1]:
			if x == snake_Head:
				game_close = True

		our_snake(snake_block, snake_List)
		your_score(Length_of_snake-1)

		pygame.display.update()

		if x1 == foodx and y1 == foody:
			foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
			foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
			Length_of_snake += 1
		clock.tick(snake_speed)

		if x1 == foodx_special and y1 == foody_special:
			foodx_special = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
			foody_special = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
			Length_of_snake += 3
		clock.tick(snake_speed)

	pygame.quit()
	quit()

gameloop()
