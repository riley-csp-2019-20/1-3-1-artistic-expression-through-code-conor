import turtle as trtl


board = trtl.Turtle()
board.pensize(2)
board.speed(100)

# the pawns are the 8 pieces in front.
# the bishops are the triangles.
# the knights are the circles.
# the rooks are the squares.
# the queens are the arrows.
# the knings are the turtles.




#Makes the outline of the board
board.left(135)
board.penup()
board.goto(200,200)
board.pendown()
board.circle(400,360,4)


board.penup()
board.goto(200,-295)
board.pendown()
#Makes the in board
in_board = 0
while (in_board < 8):
    board.circle(50,360,4)
    board.right(45)
    board.forward(70)
    board.left(45)
    in_board = in_board + 1
board.right(45)
board.color("white")
board.backward(58)
board.color("black")
board.left(45)

board.penup()
board.goto(128,-295)
board.pendown()

in_board = 0
while (in_board < 8):
    board.circle(50,360,4)
    board.right(45)
    board.forward(70)
    board.left(45)
    in_board = in_board + 1
board.right(45)
board.color("white")
board.backward(58)
board.color("black")
board.left(45)

board.penup()
board.goto(56,-295)
board.pendown()

in_board = 0
while (in_board < 8):
    board.circle(50,360,4)
    board.right(45)
    board.forward(70)
    board.left(45)
    in_board = in_board + 1
board.right(45)
board.color("white")
board.backward(58)
board.color("black")
board.left(45)

board.penup()
board.goto(-16,-295)
board.pendown()

in_board = 0
while (in_board < 8):
    board.circle(50,360,4)
    board.right(45)
    board.forward(70)
    board.left(45)
    in_board = in_board + 1
board.right(45)
board.color("white")
board.backward(58)
board.color("black")
board.left(45)

board.penup()
board.goto(-88,-295)
board.pendown()

in_board = 0
while (in_board < 8):
    board.circle(50,360,4)
    board.right(45)
    board.forward(70)
    board.left(45)
    in_board = in_board + 1
board.right(45)
board.color("white")
board.backward(58)
board.color("black")
board.left(45)

board.penup()
board.goto(-160,-295)
board.pendown()

in_board = 0
while (in_board < 8):
    board.circle(50,360,4)
    board.right(45)
    board.forward(70)
    board.left(45)
    in_board = in_board + 1
board.right(45)
board.color("white")
board.backward(58)
board.color("black")
board.left(45)

board.penup()
board.goto(-232,-295)
board.pendown()

in_board = 0
while (in_board < 8):
    board.circle(50,360,4)
    board.right(45)
    board.forward(70)
    board.left(45)
    in_board = in_board + 1
board.right(45)
board.color("white")
board.backward(58)
board.color("black")
board.left(45)

board.penup()
board.goto(-304,-295)
board.pendown()

in_board = 0
while (in_board < 8):
    board.circle(50,360,4)
    board.right(45)
    board.forward(70)
    board.left(45)
    in_board = in_board + 1
board.right(45)
board.color("white")
board.backward(58)
board.color("black")
board.left(45)

# all of the pieces
pawn_1 = trtl.Turtle()
pawn_2 = trtl.Turtle()
pawn_3  = trtl.Turtle()
pawn_4  = trtl.Turtle()
pawn_5  = trtl.Turtle()
pawn_6  = trtl.Turtle()
pawn_7  = trtl.Turtle()
pawn_8  = trtl.Turtle()
pawn_9  = trtl.Turtle()
pawn_10 = trtl.Turtle()
pawn_11 = trtl.Turtle()
pawn_12 = trtl.Turtle()
pawn_13 = trtl.Turtle()
pawn_14 = trtl.Turtle()
pawn_15 = trtl.Turtle()
pawn_16 = trtl.Turtle()

bishop_1 = trtl.Turtle()
bishop_2 = trtl.Turtle()
bishop_3 = trtl.Turtle()
bishop_4 = trtl.Turtle()

knight_1 = trtl.Turtle()
knight_2 = trtl.Turtle()
knight_3 = trtl.Turtle()
knight_4 = trtl.Turtle()

rook_1 = trtl.Turtle()
rook_2 = trtl.Turtle()
rook_3 = trtl.Turtle()
rook_4 = trtl.Turtle()

queen_1 = trtl.Turtle()
queen_2 = trtl.Turtle()

king_1 = trtl.Turtle()
king_2 = trtl.Turtle()

pawn_1.left(90)
pawn_1.color("green")
pawn_1.penup()
pawn_1.shapesize(3)
pawn_1.goto(160,-255)

pawn_2.left(90)
pawn_2.color("green")
pawn_2.penup()
pawn_2.shapesize(3)
pawn_2.goto(90,-255)

pawn_3.left(90)
pawn_3.color("green")
pawn_3.penup()
pawn_3.shapesize(3)
pawn_3.goto(20,-255)

pawn_4.left(90)
pawn_4.color("green")
pawn_4.penup()
pawn_4.shapesize(3)
pawn_4.goto(-50,-255)

pawn_5.left(90)
pawn_5.color("green")
pawn_5.penup()
pawn_5.shapesize(3)
pawn_5.goto(-120,-255)

pawn_6.left(90)
pawn_6.color("green")
pawn_6.penup()
pawn_6.shapesize(3)
pawn_6.goto(-190,-255)

pawn_7.left(90)
pawn_7.color("green")
pawn_7.penup()
pawn_7.shapesize(3)
pawn_7.goto(-260,-255)

pawn_8.left(90)
pawn_8.color("green")
pawn_8.penup()
pawn_8.shapesize(3)
pawn_8.goto(-330,-255)

pawn_9.right(90)
pawn_9.color("red")
pawn_9.penup()
pawn_9.shapesize(3)
pawn_9.goto(160,80)

pawn_10.right(90)
pawn_10.color("red")
pawn_10.penup()
pawn_10.shapesize(3)
pawn_10.goto(90,80)

pawn_11.right(90)
pawn_11.color("red")
pawn_11.penup()
pawn_11.shapesize(3)
pawn_11.goto(20,80)

pawn_12.right(90)
pawn_12.color("red")
pawn_12.penup()
pawn_12.shapesize(3)
pawn_12.goto(-50,80)

pawn_13.right(90)
pawn_13.color("red")
pawn_13.penup()
pawn_13.shapesize(3)
pawn_13.goto(-120,80)

pawn_14.right(90)
pawn_14.color("red")
pawn_14.penup()
pawn_14.shapesize(3)
pawn_14.goto(-190,80)

pawn_15.right(90)
pawn_15.color("red")
pawn_15.penup()
pawn_15.shapesize(3)
pawn_15.goto(-260,80)

pawn_16.right(90)
pawn_16.color("red")
pawn_16.penup()
pawn_16.shapesize(3)
pawn_16.goto(-330,80)

bishop_1.left(90)
bishop_1.color("green")
bishop_1.penup()
bishop_1.shapesize(2)
bishop_1.shape("triangle")
bishop_1.goto(20,-335)

bishop_2.left(90)
bishop_2.color("green")
bishop_2.penup()
bishop_2.shapesize(2)
bishop_2.shape("triangle")
bishop_2.goto(-190,-335)

bishop_3.right(90)
bishop_3.color("red")
bishop_3.penup()
bishop_3.shapesize(2)
bishop_3.shape("triangle")
bishop_3.goto(20,170)

bishop_4.right(90)
bishop_4.color("red")
bishop_4.penup()
bishop_4.shapesize(2)
bishop_4.shape("triangle")
bishop_4.goto(-190,170)

knight_1.left(90)
knight_1.color("green")
knight_1.penup()
knight_1.shapesize(2)
knight_1.shape("circle")
knight_1.goto(90,-335)

knight_2.left(90)
knight_2.color("green")
knight_2.penup()
knight_2.shapesize(2)
knight_2.shape("circle")
knight_2.goto(-260,-335)

knight_3.right(90)
knight_3.color("red")
knight_3.penup()
knight_3.shapesize(2)
knight_3.shape("circle")
knight_3.goto(90,170)

knight_4.right(90)
knight_4.color("red")
knight_4.penup()
knight_4.shapesize(2)
knight_4.shape("circle")
knight_4.goto(-260,170)

rook_1.left(90)
rook_1.color("green")
rook_1.shapesize(2)
rook_1.penup()
rook_1.shape("square")
rook_1.goto(160,-335)

rook_2.left(90)
rook_2.color("green")
rook_2.shapesize(2)
rook_2.penup()
rook_2.shape("square")
rook_2.goto(-330,-335)

rook_3.right(90)
rook_3.color("red")
rook_3.shapesize(2)
rook_3.penup()
rook_3.shape("square")
rook_3.goto(160,170)

rook_4.right(90)
rook_4.color("red")
rook_4.shapesize(2)
rook_4.penup()
rook_4.shape("square")
rook_4.goto(-330,170)

queen_1.left(90)
queen_1.color("green")
queen_1.shape("arrow")
queen_1.shapesize(2)
queen_1.penup()
queen_1.goto(-50,-335)

queen_2.right(90)
queen_2.color("red")
queen_2.shape("arrow")
queen_2.shapesize(2)
queen_2.penup()
queen_2.goto(-120,170)

king_1.left(90)
king_1.color("green")
king_1.shape("turtle")
king_1.shapesize(2)
king_1.penup()
king_1.goto(-120,-335)

king_2.right(90)
king_2.color("red")
king_2.shape("turtle")
king_2.shapesize(2)
king_2.penup()
king_2.goto(-50,170)

#some what a way to move the pieces
pawn_1.ondrag(pawn_1.goto)
pawn_2.ondrag(pawn_2.goto)
pawn_3.ondrag(pawn_3.goto)
pawn_4.ondrag(pawn_4.goto)
pawn_5.ondrag(pawn_5.goto)
pawn_6.ondrag(pawn_6.goto)
pawn_7.ondrag(pawn_7.goto)
pawn_8.ondrag(pawn_8.goto)
pawn_9.ondrag(pawn_9.goto)
pawn_10.ondrag(pawn_10.goto)
pawn_11.ondrag(pawn_11.goto)
pawn_12.ondrag(pawn_12.goto)
pawn_13.ondrag(pawn_13.goto)
pawn_14.ondrag(pawn_14.goto)
pawn_15.ondrag(pawn_15.goto)
pawn_16.ondrag(pawn_16.goto)

bishop_1.ondrag(bishop_1.goto)
bishop_2.ondrag(bishop_2.goto)
bishop_3.ondrag(bishop_3.goto)
bishop_4.ondrag(bishop_4.goto)

knight_1.ondrag(knight_1.goto)
knight_2.ondrag(knight_2.goto)
knight_3.ondrag(knight_3.goto)
knight_4.ondrag(knight_4.goto)

rook_1.ondrag(rook_1.goto)
rook_2.ondrag(rook_2.goto)
rook_3.ondrag(rook_3.goto)
rook_4.ondrag(rook_4.goto)

queen_1.ondrag(queen_1.goto)
queen_2.ondrag(queen_2.goto)

king_1.ondrag(king_1.goto)
king_2.ondrag(king_2.goto)

wn = trtl.Screen()
wn.mainloop()