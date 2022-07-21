#This greeter program is to explore functions

name = input("What's your name? ")

def greet_user(user_name):
	"""Display a greeting"""
	print("Hello, " + user_name.title())	

greet_user(name)

greet_user('Emily')
