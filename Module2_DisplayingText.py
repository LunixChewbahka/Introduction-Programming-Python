# Displaying Multiple lines of text
# You can choose between single or double quotes
print('Hello World')
print('The capybara is the world largest rodent.')
print('The capybara likes to live in groups.')
print("The capybara can swim aswell")
print('Hickory Dickory Dock! The mouse ran up the clock.')
print('This is a test print statement.')
# So when are you really going to use "" and ''
# Here is a situation. What if you want to print a sentence which uses the ''
# print('It's a beautiful day in the neighborhood')
# Now, if you continue with this python would only print out the 'It' part
# and ofcourse it won't print. Syntax Error
# print('It's a beautiful day in the neighborhood')
print("It's a beautiful day in the neighborhood") # success
print("""Hickory Dickory Dock!\n
The mouse ran up the clock""")
print("The capybara lives \nSouth America")
print("""This is the strangest
way to print over multiple lines. I know!""")
# How to print a single quote with a double quote
print('"Here is a string' + " Here is more..'")
print("or you can just do this \" does the work") # '\"' means display this char
print("Can I just print a \ on the screen?")
print("But what if I want \n to appear on the screen?") # guess not
print("But what if I want \\n to appear on the screen?") # well this one works
