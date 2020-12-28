#!/usr/bin/env python3
# The Shebang tell the computer what to call the file with when it runs.
# For more info:https://bash.cyberciti.biz/guide/Shebang.

import flywheel

context = flywheel.GearContext()  # Get the gear context.
config = context.config           # from the gear context, get the config settings.

## Load in values from the gear configuration.
my_name = config['my_name']
toppings = config['pizza_toppings']


print("Hello, {}! Here's your pizza order:\n".format(my_name))
pizza_desc = "One large thin crust with "
for i in range(len(toppings)):
    pizza_desc = pizza_desc + toppings[i]
    if i == len(toppings)-2:
        pizza_desc = pizza_desc + ' and '
    elif i < len(toppings)-1:
        pizza_desc = pizza_desc + ', '

print(pizza_desc)