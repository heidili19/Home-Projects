#This code is creating the graphics and the game of tictactoe for two players
# By Mike G and Heidi L-G
import turtle
import os

#This is is creating it own class TicTacToe
class TicTacToe(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self, visible=True)
        self.x_board = 0
        self.o_board = 0
        self.turn = 'X'
        self.theBoard = {1: '1', 2: '2', 3: '3',
                         4: '4', 5: '5', 6: '6',
                         7: '7', 8: '8', 9: '9'}
        self.winning_hands = [0b111000000,0b000111000,0b000000111,0b100100100,0b010010010,
                              0b001001001,0b100010001,0b001010100]
        self.counter = 0
        self.xo_coord = {1: (-200,200), 2: (0,200), 3: (200,200),
                         4: (-200,0), 5: (0,0), 6: (200,0),
                         7: (-200,-200), 8: (0,-200), 9: (200,-200)}
        self.winclick = False
        
    def winner(self, board):
        #print(bin(board))
        for hand in self.winning_hands:
            if (hand & board) == hand:
                 return True
        return False

#draw_shape is only calling the square and line function for now. 
    def draw_shapes(self):
        #This opens a window for the function turtle 
        self.reset()
        window = turtle.Screen()
        window.register_shape("o.gif")
        window.register_shape("x.gif")
        self.shape("turtle")
        self.width(10)
        #self.title("TicTacToe Graphics")
        self.speed(10)
        #This will go to the right locations to create the lines
        self.up()
        self.goto(-100,300)
        self.right(90)
        self.down()
        self.forward(600)
        #
        self.up()
        self.goto(100,300)
        self.down()
        self.forward(600)
        #
        self.up()
        self.goto(-300,100)
        self.left(90)
        self.down()
        self.forward(600)
        #
        self.up()
        self.goto(-300,-100)
        self.down()
        self.forward(600)
        #
        print('Turn for ' + self.turn + '. Move on which space?')
        turtle.up()
        turtle.goto (-200,-350)
        turtle.write('Turn for ' + self.turn + '. Move on which space?', font=("Arial", 16, "normal"))
        #turtle.clear()
        self.grab_answer()



#In here, I still need to draw an x or an o depening on my coordinate
    def getPos(self, x, y):
        self.up()
        #print("Coordinates of the turtle:")
        #print(x, y)
        if self.winclick:
            os._exit(0)
        n = float (100)
        if (x==n or y==n or x==(-n) or y==(-n)):
            print("You are in between two quadrants, click again")
        if x<-n and y>n:
           #print("In in quadrant 1")
           move = 1
        if ((-n < x < n) and y>n):
           #print("In in quadrant 2")
           move = 2
        if x>=n and y>=n:
           #print("In in quadrant 3")
           move = 3
        if (x<-n and (-n < y < n)):
           #print("In in quadrant 4")
           move = 4
        if ((-n < x < n) and (-n < y < n)):
           #print("In in quadrant 5")
           move = 5
        if (x>n and (-n < y < n)):
           #print("In in quadrant 6")
           move = 6
        if x<-n and y<-n:
           #print("In in quadrant 7")
           move = 7
        if ((-n < x < n) and y<-n):
          #print("In in quadrant 8")
          move = 8
        if x>n and y<-n:
           #print("In in quadrant 9")
           move = 9
        if ((self.theBoard[move] is 'X') or (self.theBoard[move] is 'O')):
            print('That space is taken, please click another space.')         
        else:
            self.theBoard[move] = self.turn
            self.counter = self.counter + 1
            if self.turn == 'X':
                self.x_board = self.x_board | (1<<(move-1))
                xsign = turtle.Turtle()
                xsign.up()
                #print(self.xo_coord[move])
                xsign.shape("x.gif")
                xsign.goto(self.xo_coord[move])
                if self.winner(self.x_board):
                    print("X won!  Hooray X!!!")
                    self.winclick = True
                    turtle.up()
                    turtle.clear()
                    turtle.goto (-200,350)
                    turtle.write
                    turtle.write('X is a Winner!!!!!!! Hooray X!', font=("Arial", 26, "normal"))
                    #os._exit(0) #enhance it to keep the board up if someone wins
                    #turtle.exitonclick()
                self.turn = 'O'
            else:
                self.o_board = self.o_board | (1<<(move-1))
                osign = turtle.Turtle()
                osign.up()
                osign.shape("o.gif")
                osign.goto(self.xo_coord[move])
                if self.winner(self.o_board):
                    print("O won!  OH YEAH O!!!")
                    #turtle.exitonclick()
                    #os._exit(0) #enhance it to keep the board up if someone wins
                    self.winclick = True
                    turtle.up()
                    turtle.clear()
                    turtle.goto (-200,350)
                    turtle.write
                    turtle.write('O Won! OH YEAH O!!!!!!!', font=("Arial", 26, "normal"))
                self.turn = 'X'
            if self.winclick == False:   
                print('Turn for ' + self.turn + '. Move on which space?')
                turtle.up()
                turtle.clear()
                turtle.goto (-250,-350)
                turtle.write('Turn for ' + self.turn + '. Move on which space?', font=("Arial", 16, "normal"))
                if self.counter >= 9:    
                    print("Booh, nobody won :-(.  A tie is like kissing your sister!")
                    #turtle.exitonclick()
                    #os._exit(0) #enhance it to keep the board up if someone wins
                    self.winclick = True
                    turtle.up()
                    turtle.clear()
                    turtle.goto (-350,350)
                    turtle.write
                    turtle.write('Bummer, nobody won. A tie is like kissing your brother :-(', font=("Arial", 20, "normal"))
    def grab_answer(self):
        mouse = turtle.onscreenclick(self.getPos)
ttt = TicTacToe()
ttt.draw_shapes()
