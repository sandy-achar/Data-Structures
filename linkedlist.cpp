#include <iostream>
using namespace std;

class node{
	public:
	
	int key;
	node * next;

	void insert_key(int data) {
	 	key = data;
		next = NULL;
	}
};

class stack{
	node * head = new node();

public:

	stack() {
		head = NULL; //Since this doesnt point to anything during init
	}

	void push(int data) {
		
		//Make a newnode and init
		node * newnode = new node();
		newnode->insert_key(data);

		if(head == NULL) {
			//Then the newnode will become the head
			head = newnode;
		}

		else {
			newnode->next = head;
			head = newnode;
		}
	}

	void pop() {
		if (head == NULL) {
			cout<<"\nThere is nothing in the stack to delete.";
		}

		else {
			cout<<"\nPopped element(stack): "<<head->key;
			head = head->next;
		}
	}

	void display() {
		cout<<"\nStack: ";
		node * current_node = new node ();
		current_node = head;

		while(current_node != NULL) {
			if (current_node->next == NULL) {
				cout<<current_node->key;
			}

			else {
				cout<<current_node->key<<" -> ";
			}

			current_node = current_node->next;
		}
	}
};

class queue{
	node * head = new node();

public:

	queue() {
		head = NULL; //Since this doesnt point to anything during init
	}

	void enqueue(int data) {
		
		//Make a newnode and init
		node * newnode = new node();
		newnode->insert_key(data);

		if(head == NULL) {
			//Then the newnode will become the head
			head = newnode;
		}

		else {

			//Here we have to find the end of the linked list to insert the node
			node *current_node = new node();
			current_node = head;
			
			while(current_node->next != NULL) {
				current_node = current_node->next;
			}

			current_node->next = newnode;
		}
	}

	void dequeue() {
		if (head == NULL) {
			cout<<"\nThere is nothing in the queue to delete.";
		}

		else {
			cout<<"\nRemoved element(queue): "<<head->key;
			head = head->next;
		}
	}

	void display() {
		cout<<"\nQueue: ";
		node * current_node = new node ();
		current_node = head;

		while(current_node != NULL) {
			if (current_node->next == NULL) {
				cout<<current_node->key;
			}

			else {
				cout<<current_node->key<<" -> ";
			}

			current_node = current_node->next;
		}
	}
};

int main() {
	stack stk;
	queue q;
	bool again = true;

	while(again) {
		int c;
		cout<<"\n\nOptions:\n1. Insert\n2. Delete\n3. Display\n4. Exit\n";
		cin>>c;

		switch(c) {
			case 1:	int data;
					cout<<"\nData: ";
					cin>>data;
					
					stk.push(data);
					q.enqueue(data);

					break;

			case 2: stk.pop();
					q.dequeue();
					break;

			case 3: stk.display();
					q.display();
					break;

			case 4: again = false;
					break;

			default: cout<<"\nWrong option. Try again";
		}
	}

	return 0;
}