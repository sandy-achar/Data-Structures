#include <iostream>
#define size 5 //What ever you want the size of the stack to be.

using namespace std;

class stack {

	int data[size];
	int head;
public:

	stack() { 
		head = 0; //This will point to the index that is empty.
	}				  //Lets make the stack fill up bottom up

	void push() {
		if(head == size) {
			cout<<"\nThe stack is full. Try deleting some data.";
		}

		else {
			cout<<"\nData: ";
			cin>>data[head++];
		}
	}

	void pop() {
		if(head == 0) {
			cout<<"\nStack is empty. Consider adding data.";
		}

		else {
			cout<<"\nPopped data: "<<data[(head - 1)];
			--head;
		}
	}

	void display() {
		cout<<"\nStack is: ";

		for(int i = (head - 1); i >=0 ;i--) {
			if(i == 0) {
				cout<<data[i];
			}

			else {
				cout<<data[i]<<" -> ";
			}
		}
	}	
};

int main() {
	stack stk;
	bool again = true;

	while(again) {
		int c;
		cout<<"\nOptions:\n1. Push\n2. Pop\n3. Display\n4. Exit\n";
		cin>>c;

		switch(c) {
			case 1:	stk.push();
					break;

			case 2: stk.pop();
					break;

			case 3: stk.display();
					break;

			case 4: again = false;
					break;

			default: cout<<"\nWrong option. Try again";
		}
	}

	return 0;
}