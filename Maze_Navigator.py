# Setting up the maze
import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A maze Game")
wn.setup(700, 700)
wn.tracer(0)

'''
#Register Shapes
turtle.register_shape("wizzard_right.gif")
turtle.register_shape("wizzard_left.gif")
turtle.register_shape("treasure.gif")
turtle.register_shape("wall.gif")
'''

# Create Pen
class Pen(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("square")
		self.color("white")
		self.penup()
		self.speed(0)
		self.gold = 0
# Create Player class
class Player(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("square")
		self.color("blue")
		self.penup()
		self.speed(0)
		self.gold = 0  # Add gold attribute to the Player class

	def go_up(self):
		#calculate the spot to move to
		move_to_x = self.xcor()
		move_to_y = self.ycor() + 24
		
		#check if the space has a wall
		if (move_to_x, move_to_y) not in walls:
			self.goto(move_to_x, move_to_y)

	def go_down(self):
		#calculate the spot to move to
		move_to_x = player.xcor()
		move_to_y = player.ycor() - 24
		
		#check if the space has a wall
		if (move_to_x, move_to_y) not in walls:
			self.goto(move_to_x, move_to_y)

	def go_left(self):
		#calculate the spot to move to
		move_to_x = player.xcor() - 24
		move_to_y = player.ycor()
		
		#check if the space has a wall
		if (move_to_x, move_to_y) not in walls:
			self.goto(move_to_x, move_to_y)
		
	def go_right(self):
		#calculate the spot to move to
		move_to_x = player.xcor() + 24
		move_to_y = player.ycor()
		
		#check if the space has a wall
		if (move_to_x, move_to_y) not in walls:
			self.goto(move_to_x, move_to_y)
	
	def is_collision(self, other):
		a = self.xcor()-other.xcor()
		b = self.ycor()-other.ycor()
		distance = math.sqrt((a ** 2) + (b ** 2))
		if distance < 5:
			return True
		else:
			return False
class Treasure(turtle.Turtle):
	def __init__(self,x, y):
		turtle.Turtle.__init__(self)
		self.shape("circle")
		self.color("gold")
		self.penup()
		self.speed(0)
		self.gold = 100
		self.goto(x, y)
		
	def destroy(self):
		self.goto(2000, 2000)
		self.hideturtle()

class Enemy(turtle.Turtle):
	def __init__(self, x, y):
		turtle.Turtle.__init__(self)
		self.shape("triangle")
		self.color("red")
		self.penup()
		self.speed(0)
		self.gold = 25
		self.goto(x, y)
		self.direction = random.choice(["up", "down", "left", "right"])
	
	def move(self):
		if self.direction == "up":
			dx = 0
			dy = 24
		elif self.direction == "down":
			dx = 0
			dy = -24
		elif self.direction == "left":
			dx = -24
			dy = 0
		elif self.direction == "right":
			dx = 24
			dy = 0
		else:
			dx = 0
			dy = 0
		#Check if player is close
		#If so, go in that direction
		if self.is_close(player):
			if player.xcor() < self.xcor():
				self.direction = "left"
			elif player.xcor() > self.xcor():
				self.direction = "right"
			elif player.ycor() < self.ycor():
				self.direction = "down"
			elif player.ycor() > self.ycor():
				self.direction = "up"
				
		# calculate the spot to move to
		move_to_x = self.xcor() + dx
		move_to_y = self.ycor() + dy
		
		#check if the space has a wall
		if (move_to_x, move_to_y) not in walls:
			self.goto(move_to_x, move_to_y)
		else:
			#choose a different direction
			self.direction = random.choice(["up", "down", "left", "right"])
			
		#set timer to move next time
		turtle.ontimer(self.move, t=random.randint(100, 300))
	
	def is_close(self, other):
		a = self.xcor()-other.xcor()
		b = self.ycor()-other.ycor()
		distance = math.sqrt((a ** 2) + (b ** 2))
		
		if distance < 75:
			return True
		else:
			return False
	
	def destroy(self):
		self.goto(2000, 2000)
		self.hideturtle()
		
# creates levels list
level = [""]

# Define first level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXX          XXXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X       XX  XXX        XX",
"XXXXXX  XX  XXX        XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXX        XXXXT XXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X                XXXXXXXX",
"XXXXXXXXXXXX   E XXXXX  X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX  XXXXXXXXXX         X",
"XXX                  E  X",
"XXX         XXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX              X",
"XX   XXXXX     T       EX",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX    YXXXXXXXXXXX  XXXXX",
"XX          XXXX        X",
"XXXX  T            T   EX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]

#Add a treasures list
treasures = []

#Add enimies list
enemies = []

# Add maze to mazes list
level.append(level_1)

# create Level Setup Function
def setup_maze(level):
	for y in range(len(level)):
		for x in range(len(level[y])):
			# Get the character at each x,y coordinate
			#NOTE the order of y and x in the next line
			character = level [y][x]
			#calculate the screen x, y coordinates
			screen_x = -288 + (x * 24)
			screen_y = 288 - (y * 24)
			
			#Check if it is an X (representing a wall)
			if character == "X":
				pen.goto(screen_x, screen_y)
				pen.stamp()
				# add coordinates to wall list
				walls.append((screen_x, screen_y))
				
			#Check if it is a P (representing the player)
			if character == "P":
				player.goto(screen_x, screen_y)
			
			#Check if it is a T (representing Treasure)
			if  character == "T":
				treasures.append(Treasure(screen_x, screen_y))
			
			#check if it is an E (representing Enemy)
			if character == "E":
				enemies.append(Enemy(screen_x, screen_y))



# Create class instances
pen = Pen()
player = Player()

# Create wall coordinate list
walls =[]

# Set up the level
setup_maze(level[1])

# Keyboard Binding
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

#Turn off screen updates
wn.tracer(0)

#start moving enimies
for enemy in enemies:
	turtle.ontimer(enemy.move, t=250)


# Main Game Loop
while True:
	#check for player collision with treasure
	#Iterate through treasure list
	for treasure in treasures:
		if player.is_collision(treasure):
			#Add the treasure gold to the player gold
			# Change this line
			player.gold += treasure.gold

			print("Player Gold:{}".format(player.gold))
			#Destroy the tresure
			treasure.destroy()
			#Remove the treasure from the treasures list
			treasures.remove(treasure)
	
	#Iterate through enemy list to see if the player collided
	for enemy in enemies:
		if player.is_collision(enemy):
			print("Player dies!")
			turtle.bye()
	#Update screen
	wn.update()
