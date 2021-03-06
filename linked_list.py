class Node:
	"""docstring for node"""
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	"""docstring for LinkedList"""
	def __init__(self ):
		self.head = None


	def push(self,data):
		new_node = Node(data)

		new_node.next=self.head

		self.head = new_node

	def append(self,data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return

		last_node=self.head
		while (last_node.next):
			last_node = last_node.next

		last_node.next= new_node
		new_node.next=None

	def insert_after(self,prev_node,new_data):
		if prev_node is None:
			print ("The given previous node must inLinkedList.")
			return	
		
		new_node= Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node


							

	def print_list(self):
		temp= self.head
		while (temp):
			print(temp.data)
			temp=temp.next



if __name__ == '__main__':
	    # Start with the empty list
    llist = LinkedList()
 
    # Insert 6.  So linked list becomes 6->None
    llist.append(6)
 
    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(7);
 
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push(1);
 
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.append(4)
 
    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.insert_after(llist.head.next, 8)
 
    print ('Created linked list is:')
    llist.print_list()
						
						
										