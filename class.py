class student:
	university="ABC"
	def __init__(self,name,id_no):
		self.name=name
		self.id=id_no

	def show(self):
			print(f'name: {self.name}')
			print(f'id: {self.id}')
			# print(f'{cls.university}')

	@classmethod
	def add(cls,n1,n2):
		return n1+n2
	




student1= student('satya',123)
student1.show()
student2= student('riyad',111)
student2.show()
print(student.add(13,12))
