#!/usr/bin/env python3.4

# This is a singly linked,linked list.

class node: # This is the simplest element in the linked list

	def __init__(self, key):
		"""Init the values of the node"""
		self.key = key
		self.next = None

class stack:

	def __init__(self):
		"""Init the head of the list"""
		self.head = None

	def push(self, key):
		"""function to insert element into the linked list"""
		
		newnode = node(key)

		if self.head is None:
			self.head = newnode

		else:
			# Since this is a stack, the insertion is only at the front (and yeah thats what she said :( )
			newnode.next = self.head
			self.head = newnode

	def pop(self):
		"""Function to delete elements from the linked list"""

		if self.head is None:
			print("There is nothing to delete from the list. Consider adding some elements.")

		else:
			print("Popped element(stack): ", self.head.key)
			self.head = self.head.next

	def display(self):
		"""Display all the keys in the linked list"""

		current_node = self.head # Cause we start from there

		print("\nStack: ")
		while(current_node is not None):
			if(current_node.next is None):
				print(current_node.key)
				current_node = None

			else:
				print(current_node.key, end = " -> ")
				current_node = current_node.next

class queue:

	def __init__(self):
		"""Init the head of the list"""
		self.head = None

	def enqueue(self, key):
		"""function to insert element into the linked list"""
		
		newnode = node(key)

		if self.head is None:
			self.head = newnode

		else:
			# Since this is a stack, the insertion is at the end of the linked list
			# So we have to first find the end of the linked list

			current_node = self.head

			while(current_node.next is not None):
				current_node = current_node.next

			current_node.next = newnode

	def dequeue(self):
		"""Function to delete elements from the linked list"""

		if self.head is None:
			print("There is nothing to delete from the list. Consider adding some elements.")

		else:
			print("Removed element(queue): ", self.head.key)
			self.head = self.head.next

	def display(self):
		"""Display all the keys in the linked list"""

		current_node = self.head # Cause we start from there

		print("\nQueue: ")
		while(current_node is not None):
			if(current_node.next is None):
				print(current_node.key)
				current_node = None

			else:
				print(current_node.key, end = " -> ")
				current_node = current_node.next

stk = stack()
q = queue()

again = True

while(again):
    a = int(input("\nOptions \n1. Push\n2. Pop\n3. Display\n4. Exit\n  "))

    if a == 1:
        key = int(input("Key: "))
        stk.push(key)
        q.enqueue(key)

    elif a == 2:
        stk.pop()
        q.dequeue()

    elif a == 3:
        stk.display()
        q.display()

    elif a == 4:
        again = False
    
    else:
        print("\nWrong option selected. Try again.")