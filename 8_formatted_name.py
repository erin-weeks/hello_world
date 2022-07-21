#working with return

#You must provide a variable where the returned information can be stored.

def get_formatted_name(first_name, last_name):
	'''Return a full name, neatly formatted.'''
	full_name = first_name + " " + last_name
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)	

author = get_formatted_name('mark','twain')
print(author)
