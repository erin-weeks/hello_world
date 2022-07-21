#Working with return
'''
Round 3: Including an optional argument. 
Add middle name
But not everyone has a middle name.
So we give it an empty default argument.
Remember that parameters with defaults have to be at the end!
'''

#You must provide a variable where the returned information can be stored.

def get_formatted_name(first_name, last_name, middle_name = ''):
	'''Return a full name, neatly formatted.'''
	
	'''Check whether there is a middle name.'''
	if middle_name:
		full_name = first_name + " " + middle_name + " " + last_name #include middle name
	else:
		full_name = first_name + " " + last_name #exclude middle name
	
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john','hooker','lee')
print(musician)
