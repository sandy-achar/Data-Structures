#include <iostream>
#define size 5 //Define the size of your queue

using namespace std;

class queue {
	int data[size];
	int tail;

public:

	queue() {
		tail = 0; //So this shows the next empty position
	}

	void insert() {

		if (tail == size) {
			cout<<"\nThe queue is full. Consider adding some elements.";
		}

		else {
			cout<<"\nData: ";
			cin>>data[tail++];
		}
	}

	void delete_data() {

		if (tail == 0) {
			cout<<"\nThe queue is empty. There is nothing to delete.";
		}

		else {
			cout<<"\nRemoved data: "<<data[0];
			for(int i = 1; i < tail; i++) {
				data[i - 1] = data[i];
			}

			tail --;
		}
	}

	void display() {
		cout<<"Queue: ";
		for(int i = 0; i < tail; i++) {
			if (i == (tail - 1)) {
				cout<<data[i];
			}

			else {
				cout<<data[i]<<" -> ";
			}
		}
	}
};

int main() {
	queue q;
	bool again = true;

	while(again) {
		int c;
		cout<<"\nOptions:\n1. Insert\n2. Delete\n3. Display\n4. Exit\n";
		cin>>c;

		switch(c) {
			case 1:	q.insert();
					break;

			case 2: q.delete_data();
					break;

			case 3: q.display();
					break;

			case 4: again = false;
					break;

			default: cout<<"\nWrong option. Try again";
		}
	}

	return 0;
}