#!/usr/bin/env python3.4

class queue:
    def __init__(self):
        """Initialize stuff for the queue"""
        self.data = []

    def enqueue(self):
        """Insert data into the stack"""
        data = int(input("\nEnter the data: "))
        self.data.append(data)

    def dequeue(self):
        """Delete data from the stack"""
        if len(self.data) == 0:
            print("\nThere is nothing in the stack.")

        else:
            print("\nDeleted element is : ", self.data[0])
            self.data.pop(0)

    def display(self):
        """Display the elements in the stack"""
        print("\nQueue : ")
        
        x = len(self.data)

        for i in range(x):

            if i == (x - 1):
                print(self.data[i])

            else:
                print(self.data[i], end = " - ")

q = queue()

again = True

while(again):
    a = int(input("\nOptions \n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit\n  "))

    if a == 1:
        q.enqueue()
    elif a == 2:
        q.dequeue()
    elif a == 3:
        q.display()
    elif a == 4:
        again = False
    else:
        print("\nWrong option selected. Try again.")
