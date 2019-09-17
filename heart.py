for row in range(6):
    for coloum in range(7):
        if (row==0 and coloum %3 !=0) or (row==1 and coloum%3==0) or (row - coloum == 2) or (row+coloum ==8):
            print("*",end="") #after printing one * control should be in same line so end="" <- null string
            #by default after one * end of line
        else:
            print(" ",end="")
    print()
        
   