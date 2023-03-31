class Node:
    def __init__(self,data):
        self.item = data
        self.ref = None

class linkedlist:
    def __init__(self,):
        self.start_node = None
    
    def traverse_list(self):
        if self.start_node is None:
            print("List has No element")
        else:
            n=self.start_node
            while n is not None:
                print(n.item,"")
                n=n.ref
    def insert_at_start(self,data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node

    def delete_at_start(self):
        if self.start_node is None:
            print("there is no element to delete")
            return
        self.start_node=self.start_node.ref
    
    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element")
            return
        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None
    
    def delete_element_by_value(self,X):
        if self.start_node is None:
            print("The list has no element")
            return
        if self.start_node.item==X:
            self.start_node=self.start_node.ref
            return
        
        n = self.start_node
        while n.ref is not None:
            if n.ref.item == X:
                break
            n=n.ref
        if n.ref is None:
            print("Item not found")
        else:
            n.ref = n.ref.ref
    
    def search_item(self,X):
        if self.start_node is None:
            print("item not found")
            return
        n = self.start_node
        while n is not None:
            if n.item == X:
                print("Item found")
                return True
            n = n.ref
        print("Item not found")
        return False

    def get_count(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        count = 0
        while n is not None:
            count = count+1
            n=n.ref
        return count
    
    def insert_at_index(self,index,data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node= new_node
        i = 1
        n = self.start_node
        while i<index-1 and n is not None:
            n = n.ref
            i=i+1
        if n is None:
            print("Index out of Bound")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

new_linked_list = linkedlist()
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(10)
new_linked_list.insert_at_end(15)
new_linked_list.insert_at_end(20)
new_linked_list.insert_at_end(25)
new_linked_list.insert_at_end(30)
new_linked_list.insert_at_end(35)
new_linked_list.insert_at_end(40)
new_linked_list.insert_at_end(45)
new_linked_list.traverse_list()
new_linked_list.delete_at_start()
print("After deletion at the beginning ")
new_linked_list.traverse_list()
new_linked_list.delete_at_end()
print("After deletion at the end")
new_linked_list.traverse_list()
new_linked_list.delete_element_by_value(20)
new_linked_list.traverse_list()

print("Ater deleting")
new_linked_list.search_item(5)
new_linked_list.search_item(10)
print("no of nodes",new_linked_list.get_count())
new_linked_list.insert_at_index(3,8)
new_linked_list.traverse_list()



