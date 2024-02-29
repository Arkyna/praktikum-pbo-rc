# A simple example classes
class MyClass(): # Class itself
	myProperty = "Sebastian"  # Class's Property

	def myMethod(self): # Class's Method
		print(f"Aloha {self.myProperty}\n")

myObject = MyClass() # Class's Objects
myObject.myMethod() # Aloha Sebastian