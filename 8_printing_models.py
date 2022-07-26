#Using functions to modify a list.

'''
Functions can be used to modify lists. Sometimes that's good!
Sometimes that's bad.
'''

#Example: 3D design printer --> orders --> printed

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
printed = []

def print_models(to_be_printed, printed):
	#Simulate printing
	while to_be_printed:
		in_print = to_be_printed.pop()
		msg = "Printing " + in_print.title() + "."
		print(msg)
		
		#Move to printed.
		printed.append(in_print)

def finish_print(printed):
	#Report completed jobs.
	print("\nThe following models have been printed: ")
	for model in printed:
		print(model.title())

print_models(unprinted_designs, printed)
finish_print(printed)
