#This greeter program is to explore functions

'''Expanding on functions to review how to include functions in loops'''

people_in_line = True

def get_formatted_name(first_name, last_name):
	"""Format full name"""
	full_name = first_name + " " + last_name
	
	return full_name

def greet_user(format_name):
	"""Display a greeting"""	
	print("\nHello, " + format_name.title())	
	
greet_user('Emily')


while people_in_line == True:
	print("\nPlease tell me your name.") #get name
	f_name = input("First name: ")
	l_name = input("Last name: ")
	
	formatted_name = get_formatted_name(f_name, l_name) #call format function
	greet_user(formatted_name) #call greet function
	
	'''Prevent infinite loops by including a flag.'''
	more_people = input("Are there more people to greet? (yes / no ) ")
	if more_people == 'no':
		people_in_line = False

	
	
	
	
