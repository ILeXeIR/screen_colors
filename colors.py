import sys
import pygame
import random

class Instructions():
	#Класс для отображения инструкций по управлению на экране

	def __init__(self, colors):
		self.screen = colors.screen
		self.screen_rect = colors.screen.get_rect()
		self.message = self._read_instruction()
		self.font = pygame.font.SysFont('arial', 30)
		self.text_color = (230, 230, 230)
				
	def blitme(self):
		x = (100, 50)
		for line in self.message:
			text = self.font.render(line.rstrip(), 1, self.text_color)
			rect = text.get_rect()
			rect.topleft = x
			self.screen.blit(text, rect)
			x = rect.bottomleft

	def update(self):
		x = colors.red + colors.green + colors.blue
		if x > 350:
			self.text_color = (30, 30, 30)
		else:
			self.text_color = (230, 230, 230)

	def _read_instruction(self):
		filename = 'instruction.txt'
		with open(filename) as file_object:
			return file_object.readlines()


class RGB():
	#Класс для отображения уровней RGB на экране

	def __init__(self, colors):
		self.screen = colors.screen
		self.screen_rect = colors.screen.get_rect()
		self.font = pygame.font.Font(None, 50)
		self.text_color = (230, 230, 230)
				
	def blitme(self):
		message = 'R {:.2f} / G {:.2f} / B {:.2f}'.format(colors.red, colors.green, colors.blue)
		text = self.font.render(message, 1, self.text_color)
		rect = text.get_rect()
		rect.midbottom = self.screen_rect.midbottom
		self.screen.blit(text, rect)

		if colors.c_flag:
			#При включении смены цветов отображает целевой цвет, к которому стремятся значения RGB
			message_c = 'Target: R {:.2f} / G {:.2f} / B {:.2f}'.format(
				colors.new_red, colors.new_green, colors.new_blue)
			text_c = self.font.render(message_c, 1, self.text_color)
			rect_c = text_c.get_rect()
			rect_c.midbottom = rect.midtop
			rect_c.y -= 20
			self.screen.blit(text_c, rect_c)

	def update(self):
		x = colors.red + colors.green + colors.blue
		if x > 350:
			self.text_color = (30, 30, 30)
		else:
			self.text_color = (230, 230, 230)


class ColoredScreen():
	#Класс для получения окна с возможной регулировкой цвета

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.screen_rect = self.screen.get_rect()
		pygame.display.set_caption('Colors')
		self.clock = pygame.time.Clock()

		self.red = 0
		self.green = 0
		self.blue = 0
		self.red_more_flag = False
		self.green_more_flag = False
		self.blue_more_flag = False
		self.red_less_flag = False
		self.green_less_flag = False
		self.blue_less_flag = False
		self.i_flag = True #Отображение инструкции
		self.k_flag = False #Отображение служебной информации
		self.c_flag = False #Запуск плавной смены цветов

		self.instruct = Instructions(self)
		self.rgb_levels = RGB(self)

	def run_program(self):
		#Запуск основной программы
		while True:
			self._check_events()
			if self.c_flag:
				self._changing_colors()
			else:
				self._update_color()
			self.instruct.update()
			self.rgb_levels.update()
			pygame.mouse.set_visible(False)
			self._update_screen()

	def _update_color(self):
		#Обновляет цвет при нажатии соответствующих клавиш
		speed = 7.5
		if self.red_more_flag and self.red < 255:
			self.red += speed
			if self.red > 255:
				self.red = 255
		if self.red_less_flag and self.red > 0:
			self.red -= speed
			if self.red < 0:
				self.red = 0
		if self.green_more_flag and self.green < 255:
			self.green += speed
			if self.green > 255:
				self.green = 255
		if self.green_less_flag and self.green > 0:
			self.green -= speed
			if self.green < 0:
				self.green = 0
		if self.blue_more_flag and self.blue < 255:
			self.blue += speed
			if self.blue > 255:
				self.blue = 255
		if self.blue_less_flag and self.blue > 0:
			self.blue -= speed
			if self.blue < 0:
				self.blue = 0

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
		if event.key == pygame.K_ESCAPE:
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
		elif event.key == pygame.K_k:
			self.k_flag = not self.k_flag
		elif event.key == pygame.K_r and not self.c_flag:
			self._random_color()
		elif event.key == pygame.K_c:
			self.c_flag = not self.c_flag
			if self.c_flag:
				self.new_random_flag = True #Флаг для функции _changing_colors


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

	def _random_color(self):
		#Выбрать рандомный цвет
		self.red = random.uniform(0, 255)
		self.green = random.uniform(0, 255)
		self.blue = random.uniform(0, 255)

	def _changing_colors(self):
		#Плавная смена цветов до рандомного.
		changing_speed = 2
		if self.new_random_flag:
			self.new_red = random.uniform(0, 255)
			self.new_green = random.uniform(0, 255)
			self.new_blue = random.uniform(0, 255)
			self.red_step = (self.new_red - self.red)/1000
			self.green_step = (self.new_green - self.green)/1000
			self.blue_step = (self.new_blue - self.blue)/1000
			self.new_random_flag = False
		self.red += self.red_step * changing_speed
		self.green += self.green_step * changing_speed
		self.blue += self.blue_step * changing_speed
		if ((self.red_step > 0 and self.red >= self.new_red) or
					(self.red_step < 0 and self.red <= self.new_red)):
			self.new_random_flag = True

	def _update_screen(self):
		#Обновляет изображения на экране и отображает новый экран
		self.screen.fill((self.red, self.green, self.blue))
		if self.i_flag:
			self.instruct.blitme()
		if self.k_flag:
			self.rgb_levels.blitme()
		pygame.display.flip()
		self.clock.tick(30)

if __name__ == '__main__':
	#создание экземпляра и запуск игры
	colors = ColoredScreen()
	colors.run_program()


