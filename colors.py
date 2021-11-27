import sys
import pygame

class Instructions():
	#Класс для отображения инструкций по управлению на экране

	def __init__(self, colors):
		self.screen = colors.screen
		self.screen_rect = colors.screen.get_rect()
		self.message = "Instructions"
		self.font = pygame.font.Font(None, 30)
		self.text_color = (230, 230, 230)
		self.text = self.font.render(self.message, 1, self.text_color)
		self.rect = self.text.get_rect()
		self.rect.topleft = (100, 50)
		
	def blitme(self):
		self.screen.blit(self.text, self.rect)

	def update(self):
		x = colors.red + colors.green + colors.blue
		if x > 350:
			self.text_color = (30, 30, 30)
		else:
			self.text_color = (230, 230, 230)
		self.text = self.font.render(self.message, 1, self.text_color)

class ColoredScreen():
	#Класс для получения окна с возможной регулировкой цвета

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.screen_rect = self.screen.get_rect()
		pygame.display.set_caption('Colors')

		self.red = 0
		self.green = 0
		self.blue = 0
		self.red_more_flag = False
		self.green_more_flag = False
		self.blue_more_flag = False
		self.red_less_flag = False
		self.green_less_flag = False
		self.blue_less_flag = False
		self.i_flag = True

		self.instruct = Instructions(self)

	def run_program(self):
		#Запуск основной программы
		while True:
			self._check_events()
			self._update_color()
			self.instruct.update()
			self._update_screen()

	def _update_color(self):
		#Обновляет цвет при нажатии соответствующих клавиш
		speed = 0.5
		if self.red_more_flag and self.red < 255:
			self.red += speed
		if self.red_less_flag and self.red > 0:
			self.red -= speed
		if self.green_more_flag and self.green < 255:
			self.green += speed
		if self.green_less_flag and self.green > 0:
			self.green -= speed
		if self.blue_more_flag and self.blue < 255:
			self.blue += speed
		if self.blue_less_flag and self.blue > 0:
			self.blue -= speed

	def _check_events(self):
		#Обрабатывает нажатия клавиш
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		#Реакция на нажатие клавиш
		if event.key == 27:
			sys.exit()
		elif event.key == pygame.K_q:
			self.red_more_flag = True
		elif event.key == pygame.K_a:
			self.red_less_flag = True
		elif event.key == pygame.K_w:
			self.green_more_flag = True
		elif event.key == pygame.K_s:
			self.green_less_flag = True
		elif event.key == pygame.K_e:
			self.blue_more_flag = True
		elif event.key == pygame.K_d:
			self.blue_less_flag = True
		elif event.key == pygame.K_i:
			self.i_flag = not self.i_flag


	def _check_keyup_events(self, event):
		#Реакция на отпускание клавиш
		if event.key == pygame.K_q:
			self.red_more_flag = False
		elif event.key == pygame.K_a:
			self.red_less_flag = False
		elif event.key == pygame.K_w:
			self.green_more_flag = False
		elif event.key == pygame.K_s:
			self.green_less_flag = False
		elif event.key == pygame.K_e:
			self.blue_more_flag = False
		elif event.key == pygame.K_d:
			self.blue_less_flag = False

	def _update_screen(self):
		#Обновляет изображения на экране и отображает новый экран
		self.screen.fill((self.red, self.green, self.blue))
		if self.i_flag:
			self.instruct.blitme()
		pygame.display.flip()

if __name__ == '__main__':
	#создание экземпляра и запуск игры
	colors = ColoredScreen()
	colors.run_program()


