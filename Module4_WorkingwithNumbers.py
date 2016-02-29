area = 0
height = 10
width = 20

# calculate the area of a triangle
area = width * height / 2

# printing formatted float value with 2 decimal places
print('The area of the triangle would be %0.2f' % area)

print('My favorite number is %d !' % 42)
print('My favorite number is %6d !' % 42)
print('I have {0:d} cats'.format(6))
print('I have {0:3d} cats'.format(6))
print('I have {0:03d} cats'.format(6))
print('I have {0:f} cats'.format(6))
print('I have {0:.2f} cats'.format(6))

# Let's do the same thing with the .format syntax to include numbers
# our output
print("The area of the Triangle would be {0:f} ".format(area))
print("My Favorite number is {0:d} ".format(42))

# This is an example with multiple numbers
# I have used the '\' to incdicate command continues on next line
print("Here are three numbers!" + \
		"The first is {0:d} The second number is {1:4d}" + \
		" and The last number is {2:d} ".format(7,8,9))
