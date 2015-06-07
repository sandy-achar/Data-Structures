#!/usr/bin/env python3.4

size = 10 # Can change the size of the hash table on the go
class node:
	def __init__(self, key):
		"""Init the various elements in the node"""
		self.key = key
		self.next = None
		#self.prev = None

class hashtable:
	def __init__(self):
		"""Make an array to hold the hashed objects"""
		self.hash = [None for x in range(size)]

	def hash_function(self, data):
		"""Return the index the data has to belong in"""
		return (data % size)

	def insert(self):
		"""Insert the data into the hash table"""
		data = int(input("Data to insert: "))
		index = self.hash_function(data)
		newnode = node(data)

		if self.hash[index] is None:
			self.hash[index] = newnode

		else:
			# We search for the end of the list
			current_node = self.hash[index]

			while(current_node.next is not None):
				current_node = current_node.next

			#newnode.prev = current_node
			current_node.next = newnode

	def search(self):
		"""Search for a given data in the hash table"""
		data = int(input("Data to be searched: "))
		index = self.hash_function(data)
		isfound = False

		if self.hash[index] is not None:
			current_node = self.hash[index]

			while(current_node is not None):

				if(current_node.key == data):
					isfound = True
					break

				current_node = current_node.next

		if isfound is True:
			print(data, " successfully found at index: ", index)

		else:
			print(data, " not found in the hash table.")

	def delete(self):
		"""Search and delete a given data"""
		data = int(input("Data to be deleted: "))
		index = self.hash_function(data)
		isfound = False

		if self.hash[index] is not None:
			current_node= self.hash[index]

			if current_node.key == data:
				self.hash[index] = current_node.next
				print(data," successfully deleted at index: ",index)
				isfound = True

			else:
				while(current_node.next is not None):

					if current_node.next.key == data:
						isfound = True

						temp_node = current_node.next
						temp_node = temp_node.next
						current_node.next = temp_node

						print(data," successfully deleted at index: ",index)

					else:
						current_node = current_node.next

		if isfound is False:
			print(data, " not found in the hash table.")

	def display_table(self):
		"""Show the entire hash table"""
		# We never use this
		# Using this will defeat the purpose of hashtable
		# And if you have to use it for searching for an element, be really ashamed
		print("\nThe entire hash table is :")
		for x in self.hash:

			if x is None:
				print("*")

			else:
				current_node = x
				while(current_node is not None):

					if current_node.next is None:
						print(current_node.key)

					else:
						print(current_node.key, end = " -> ")

					current_node = current_node.next

hash = hashtable()

again = True

while(again):
	a = int(input("\nOptions \n1. Insert\n2. Display Table\n3. Search\n4. Delete\n5. Exit\n  "))

	if a == 1:
		hash.insert()

	elif a == 2:
		hash.display_table()

	elif a == 3:
		hash.search()

	elif a == 4:
		hash.delete()

	elif a == 5:
		again = False
    
	else:
		print("\nWrong option selected. Try again.")