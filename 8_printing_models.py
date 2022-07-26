#Using functions to modify a list.

'''
Functions can be used to modify lists. Sometimes that's good!
Sometimes that's bad.
'''

#Example: 3D design printer --> orders --> printed

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
printed_models = []

#Simulate printing & move each item into completed
while unprinted_designs:
	current_design = unprinted_designs.pop()
	msg = "Printing " + current_design + "."
	print(msg)
	printed_models.append(current_design)

print("\nThe following orders have been completed: ")
for model in printed_models:
	print(model.title())