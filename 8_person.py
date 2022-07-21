#Building more complicated data structures

'''This exercise takes various parts of a name and then returns a dicionary.'''

def build_person(first_name, last_name, age = ''):
	'''Return a dictionary of information about a person'''
	person = {'first': first_name, 'last': last_name}
	
	'''Because age is optional, we put it in an if statement just in case.'''
	if age:
		person['age'] = age
	return person

musician = build_person('jimi','hendrix')
print(musician)

'''If we know the keys, can we format better?'''

print(musician['first'].title() + " " + musician['last'].title())

'''Testing with age'''

musician = build_person('jimi', 'hendrix', 37)

print(musician['first'].title() + " " + musician['last'].title() + ", " + str(musician['age']))
