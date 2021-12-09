################
# Control Flow #
################

# IF Statement
# Checks if condition matches condition2
# Syntax: if <condition> operator <condition_2>:

# ELIF Statement
# Creates another argument after an IF Statement
# Syntax: elif <condition> operator <condition2>:

# ELSE Statement
# Used after all previous arguments, that triggers after none of the conditions previously have been met
# Syntax: else:

age = 15

if age >= 18:
    print("You are old enough.\nYou can buy the ticket.")
elif age < 18:
    print("You are under 18 y/o.\nYou cannot buy the ticket.")
else:
    print("This will never happen kek.")
