from kivy.graphics.texture import Texture




class gradient():
	def __init__(self):
		self.texture = Texture.create(size=(2, 2), colorfmt='rgba')
		
		
	def create(self, colorlist, direction = 'Top-Bottom'):
		Left_Bottom = colorlist[0]
		Right_Bottom = colorlist[1]
		Left_Top = colorlist[2]
		Right_Top = colorlist[3]
		
		if direction == 'Left-Right':
			Color = Left_Bottom + Left_Top + Right_Bottom + Right_Top
		
		elif direction == 'Right-Left':
			Color = Right_Bottom + Right_Top + Left_Bottom + Left_Top
		
		elif direction == 'Top-Bottom':
			Color = Left_Top + Right_Top + Left_Bottom + Right_Bottom
			
		elif direction == 'Bottom-Top':
			Color = Left_Bottom + Right_Bottom + Left_Top + Right_Top
		
		elif direction == 'TopRight-BottomLeft':
			Color = Left_Bottom + Right_Bottom + Left_Top + Right_Top
			
		elif direction == 'TopLeft-BottomRight':
			Color = Left_Bottom + Right_Bottom + Left_Top + Right_Top
			
		buf = bytes(Color)
		self.texture.blit_buffer(buf, colorfmt='rgba', bufferfmt='ubyte')
		
		return self.texture




#def create_gradient(colorlist, direction ):
#	global texture
#	
#	Left_Bottom = colorlist[0]
#	Right_Bottom = colorlist[1]
#	Left_Top = colorlist[2]
#	Right_Top = colorlist[3]
#	
#	if direction == 'Left-Right':
#		Color = Left_Bottom + Left_Top + Right_Bottom + Right_Top
#		
#	elif direction == 'Right-Left':
#		Color = Right_Bottom + Right_Top + Left_Bottom + Left_Top
#	
#	elif direction == 'Top-Bottom':
#		Color = Left_Top + Right_Top + Left_Bottom + Right_Bottom
#		
#	elif direction == 'Bottom-Top':
#		Color = Left_Bottom + Right_Bottom + Left_Top + Right_Top
#	
#	elif direction == 'TopRight-BottomLeft':
#		Color = Left_Bottom + Right_Bottom + Left_Top + Right_Top
#		
#	elif direction == 'TopLeft-BottomRight':
#		Color = Left_Bottom + Right_Bottom + Left_Top + Right_Top
#		
#	buf = bytes(Color)
#	texture.blit_buffer(buf, colorfmt='rgba', bufferfmt='ubyte')
#	
#	return texture