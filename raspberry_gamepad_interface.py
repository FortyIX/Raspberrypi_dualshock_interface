## Code by Fu Zhang 



import pprint
import pygame
from pynput.keyboard import Key,Controller





class PS4Interface(object):
	controller = None 
	keyboard = None

	def __init__(self):
		pygame.init()
		pygame.joystick.init()
		self.controller = pygame.joystick.Joystick(0)
		self.controller.init()
		self.keyboard = Controller()
		
	
	def listener(self):
		while True: 
			for e in pygame.event.get():
				if e.type == pygame.JOYHATMOTION:
						self.ArrowButtonEventHandler(e.value)
               
		    			






	def AxisEventHandler(self, axis, degree):
		if(axis == 0):
			if(degree == 1.00):
				self.keyboard.press(Key.right)
				self.keyboard.release(Key.right)
			elif(degree == -1.00):
				self.keyboard.press(Key.left)
				self.keyboard.release(Key.left)
		if(axis == 1):
			if(degree == 1.00):
				self.keyboard.press(Key.down)
				self.keyboard.release(Key.down)
			elif(degree == -1.00):
				self.keyboard.press(Key.up)
				self.keyboard.release(Key.up)
		    	
		pass

	def ArrowButtonEventHandler(self,button):
		if(button[0] == 1):
				self.keyboard.press(Key.right)
				self.keyboard.release(Key.right)
		elif(button[1] == -1):
				self.keyboard.press(Key.down)
				self.keyboard.release(Key.down)
		elif(button[0] == -1):
				self.keyboard.press(Key.left)
				self.keyboard.release(Key.left)
		elif(button[1]== 1):
				self.keyboard.press(Key.up)
				self.keyboard.release(Key.up)
		    	
		pass



pass

if __name__ == "__main__":
	con = PS4Interface()
	con.listener()
