#experimenting with tuples

#defining Tuple using trailing comma
one_footballer = 'Maradona',
print(one_footballer)

#defining Tuple using parenthesis
footballers = ('Maradona', 'Pele', 'Bebeto', 'Jiko')
print(footballers)

#tuple unpacking

first, second, third, fourth = footballers
print(first)

#use tuples to swap variables in one statement

address1 = 'Hyderabad'
address2 = 'Kharagpur'
print('Addr1: ', address1)

print('Addr2: ', address2)

address1, address2 = address2, address1

print('Addr1: ', address1)

print('Addr2: ', address2)

#convert List to Tuple using tuple function

address = [address1, address2]
print (tuple(address))

#convert List to String using tuple function
print(tuple('Sabya'))