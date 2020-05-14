import random
import math


# 2. The excuse must be in a variable:
# ```python
# excuse = 'The dog eat my homework when I finished'
# ```
# 3. Using python, create a function that generates and returns a random excuse with the following structure:
# ```python
# who = ['the dog','my granma','his turtle','my bird']
# what = ['eat','pissed','crushed','broked']
# when = ['before the class','right in time','when I finished','during my lunch','while I was praying']
# ```
# 4. To create a consistent excuse you have to concatenate one item from each array in the proper order.
# 5. Print the excuse on the console using the `print` function.

# your code here

who = ['the dog','my granma','his turtle','my bird','my cat','my mouse']
what = ['eat','pissed','crushed me','stole from me','broke', 'screamed', 'destroyed']
when = ['before the class','right in time','when I finished','during my lunch','while I was praying']


def excuse_generator(some_parameter, some_other_parameter, a_final_parameter):
    excuse = some_parameter[random.randint(0,len(some_parameter)-1)]+" "+some_other_parameter[random.randint(0,len(some_other_parameter)-1)]+" "+a_final_parameter[random.randint(0,len(a_final_parameter)-1)]
    return excuse


print(excuse_generator(who, what, when))