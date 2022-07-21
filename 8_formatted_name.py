#Working with return
'''
Round 2: Including an optional argument. 
Add middle name
'''

#You must provide a variable where the returned information can be stored.

def get_formatted_name(first_name, middle_name, last_name):
	'''Return a full name, neatly formatted.'''
	full_name = first_name + " " + middle_name + " " + last_name
	return full_name.title()

musician = get_formatted_name('jimi', 'john', 'hendrix')
print(musician)	
