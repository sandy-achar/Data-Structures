#!/usr/bin/env python3.4

class stack:
    def __init__(self):
        """Initialize stuff for the queue"""
        self.data = []

    def push(self):
        """Insert data into the stack"""
        data = int(input("\nEnter the data: "))
        self.data.append(data)

    def pop(self):
        """Delete data from the stack"""
        if len(self.data) == 0:
            print("\nThere is nothing in the stack.")

        else:
            print("\nPopped element is : ", self.data[-1])
            self.data.pop()

    def display(self):
        """Display the elements in the stack"""
        print("\nStack : ")
        
        x = len(self.data)
        x -= 1

        for i in range(x, -1, -1):

            if i == 0:
                print(self.data[i])

            else:
                print(self.data[i], end = " - ")

stk = stack()

again = True

while(again):
    a = int(input("\nOptions \n1. Push\n2. Pop\n3. Display\n4. Exit\n  "))

    if a == 1:
        stk.push()
    elif a == 2:
        stk.pop()
    elif a == 3:
        stk.display()
    elif a == 4:
        again = False
    else:
        print("\nWrong option selected. Try again.")
