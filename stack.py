class Stack:
	def __init__(self):
		self.data=[]

	def is_empty(self):
		return len(self.data)==0

	def push(self,e):
		self.data.append(e)

	def pop(self,e):
		if self.is_empty():
			raise Empty("stack is empty")
		return self.data.pop()		

	def	print(self):
		show=[]
		for item in self.data:
			show.append(item)

		print(show)	

	def top(self):
		if self.is_empty():
			raise Empty("stack is empty")
		return (self.data[-1])		



stack = Stack()

stack.print()
for i in range(1,11):
	stack.push(i)
	stack.print()
for i in range(1,11):
	stack.pop(i)
	stack.print()	