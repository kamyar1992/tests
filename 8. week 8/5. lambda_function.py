# Alonzo Church 1930's: lambda calculus
# lambda calculus features (also programming): computational base, pure, abstract, stateless --> functional programming
# languages like: Haskell, Lips, Erlang


# Alen Turing: Turing Machine
# Imperative coding: --> C / Python

# lambda <bind variable(s)s>: body
# lambda function also  is called inline function

def add_one(n):
    return n+1


print(add_one(2))

one_adder = lambda x: x + 1
print(one_adder(1))

adder = lambda x, y: x+y
print(adder(3, 2))


print(lambda x, y: x * y)
print(lambda x, y: x * y(2, 3))

# lambda feature:
# 1. can be anonymous
# 2. single line
# 3. no support for statements (a=b)
# 4. just support expression (a+1)
# 5. IIFE : Immediate Invoked Function Execution : at the moment that define can get arguments
# 6. no support for Annotation

sample_list = [('Saba', 25), ('Ramtin', 27), ('Roozbeh', 32), ('Kamyar', 30)]
sample_list_2 = sorted(sample_list, key= lambda x : x[1], reverse=True)
print(sample_list_2)

