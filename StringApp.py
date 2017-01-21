# python array
letters = 'abcdefghijklmnopqrstuvwxyz'

#print first char - a
print(letters[0])

#print last char - z
print(letters[-1])

#print second from the last - y
print(letters [-2])

#print the entire string
print(letters[:])

#wil print NaNaNaNa - four times
print('Na' *4)

#slice

#from beginning to end offset minus 1 a-y
print(letters[:-1])

#from start to end offset minus 1 - a-x
print(letters[0:-2])

#display ace, start to end skipping one char
print(letters[0:5:2])

#display u-x
print(letters[-6:-2])

print(len(letters)) #display length of the string - 26
print(len(""))

#split a string
csvar='sabya, john, mike'
print(csvar.split(',')) #convert a string into a list delimited by ,
print(csvar.split()) #without any delimiter split will take newline, space and tab

#join

cs_list=csvar.split(',')
print('displaying list', cs_list)

#convert list to string
cs_str = ','.join(cs_list)
print(cs_str)

#String functions

poem = '''All that doth flow we cannot liquid name Or else would fire and water be the same;
But that is liquid which is moist and wet Fire that property can never get.
Then 'tis not cold that doth the fire put out But 'tis the wet that makes it die, no doubt.'''

#does the string starts with All

print(poem.startswith('All'))

#does the string ends with All

print(poem.endswith('All'))

#first offset of the

print(poem.find('the'))

#last offset of the

print (poem.rfind('the'))

setup = 'a duck goes into a bar...duck'

# remove all .

print(setup.strip('.'))

print(setup.capitalize())

print(setup.replace('duck', 'human', 1))


