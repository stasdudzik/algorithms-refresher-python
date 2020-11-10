# ilustrating recursion with Tower of Hanoi Problem 
# as explained by prof. Thorsten Altenkirch


# f stands for "from"
# t stand for "to"
# v stands for "via"
def move(f,t):
    print("Move disc from {} to {}!".format(f,t))

# move("A", "C")

def moveVia(f,v,t):
    move(f, v)
    move(v, t)

# moveVia("A","B","C")

def hanoi(n, f, h, t):
# "n" number of disks "f" from "h" helper "t" target
    # base case : when 0 disks, do nothing 
    if n == 0:
        pass
    else:
        hanoi(n-1, f, t, h)
        move(f,t)
        hanoi(n-1, h, f, t)

user_input = int(input("Type in number of disks: "))
hanoi(user_input, "A", "B", "C")
num_moves = str((2**user_input) - 1)
print("minimal number of moves required to solved it is 2**n - 1 where n is the number of disks. In this case: {}".format(num_moves)) 