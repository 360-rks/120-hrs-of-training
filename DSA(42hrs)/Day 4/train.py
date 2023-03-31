'''A train is identified by its name and list of compartments.
The compartments are identified by its name,total seating 
capacity and the number of passengers.
Implement the class Train as given in the class diagram.
Train
- train_name
- compartment_list
_init_(train_name,compartment_list)
+ get_train_name()
+ get_compartment_list()
+ count_compartments ()
+ check_vacancy()
Write a python program to implement the following:
count_compartments()- returns the total number of compartments
 in the train
check_vacancy()-returns the count of the compartments in which
 more than 50% of the seats are vacant
Note : Compartment list is maintained as a linked list where 
data in each node refers to a compartment.
A train is identified by its name and list of compartments.
The compartments are identified by its name,total seating 
capacity and the number of passengers.
Implement the class Train as given in the class diagram.
Train
- train_name
- compartment_list
_init_(train_name,compartment_list)
+ get_train_name()
+ get_compartment_list()
+ count_compartments ()
+ check_vacancy()
Write a python program to implement the following:

count_compartments()- returns the total number of compartments in the train
check_vacancy()-returns the count of the compartments in which more than 50% of the seats are vacant
Note : Compartment list is maintained as a linked list where data in each node refers to a compartment.'''
class Compartment:
    def __init__(self, name, num_passengers,total_seating):
        self.name = name
        self.total_seating = total_seating
        self.num_passengers = num_passengers
        self.next_compartment = None

class CompartmentLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, compartment):
        new_compartment = Compartment(compartment[0], compartment[1], compartment[2])
        if self.head is None:
            self.head = new_compartment
        else:
            curr_compartment = self.head
            while curr_compartment.next_compartment is not None:
                curr_compartment = curr_compartment.next_compartment
            curr_compartment.next_compartment = new_compartment
        self.count += 1

    def __len__(self):
        return self.count

class Train:
    def __init__(self, train_name, compartment_list):
        self.train_name = train_name
        self.compartment_list = compartment_list

    def get_train_name(self):
        return self.train_name

    def count_compartments(self):
        return len(self.compartment_list)

    def check_vacancy(self):
        count = 0
        curr_compartment = self.compartment_list.head
        while curr_compartment is not None:
            if curr_compartment.num_passengers <= 0.5 * curr_compartment.total_seating:
                count += 1
            curr_compartment = curr_compartment.next_compartment
        return count

    def add_compartment(self, compartment):
        self.compartment_list.append(compartment)



compartment_list = CompartmentLinkedList()
compartment_list.append(('SL', 250, 400))
compartment_list.append(('2AC', 125, 280))
compartment_list.append(('3AC', 120, 300))
compartment_list.append(('FC', 160, 300))
compartment_list.append(('1AC', 100, 210))

train = Train("Express", compartment_list)
print(train.count_compartments()) 
print(train.check_vacancy()) 
print(train.count_compartments())
