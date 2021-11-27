import sys
import pygame

class ColoredScreen():
	#Класс для получения окна с возможной регулировкой цвета

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((1200, 800))
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

	def run_program(self):
		#Запуск основной программы
		while True:
			self._check_events()
			self._update_color()
			self._update_screen()

	def _update_color(self):
		#Обновляет цвет при нажатии соответствующих клавиш
		if self.red_more_flag and self.red < 255:
			self.red += 1
		if self.red_less_flag and self.red > 0:
			self.red -= 1
		if self.green_more_flag and self.green < 255:
			self.green += 1
		if self.green_less_flag and self.green > 0:
			self.green -= 1
		if self.blue_more_flag and self.blue < 255:
			self.blue += 1
		if self.blue_less_flag and self.blue > 0:
			self.blue -= 1

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
		pygame.display.flip()

if __name__ == '__main__':
	#создание экземпляра и запуск игры
	Colors = ColoredScreen()
	Colors.run_program()


