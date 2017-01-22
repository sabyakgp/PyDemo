#defining dictionary using dict function
#This will convert a set of lists to dict.
l_list = [[1977, 'Sabya'], [1980, 'Vikas'], [1990, 'Larry']]
l_dict = dict(l_list)
print(l_dict)

#defining dictionary using {} - key: value pair
l_prog = {100: 'Sabyasachi Mitra',
          200: 'Jim Patrick',
          300: 'Var der Guisaam',
          400: 'Linus Tovald'
          }
print(l_prog)

#display the value using a key
print(l_prog[400])

#replace value using key
l_prog[200] = 'Dennis Richie'
print(l_prog[200])

#use Update to insert new key: value to a dictionary
l_prog_new = {500: 'Kennisgham', 600: 'Gosling'}
l_prog.update(l_prog_new)
print(l_prog)

#use del() to delete a key:value
del l_prog_new[600]
print(l_prog_new)
#use clear to clear all items
l_prog_new.clear()
print(l_prog_new)

#testing the existance of a key using in operator

print(100 in l_prog)

#trying a print a value whose key is not present
#print(l_prog[6000]) #this will lead to exception KeyError

#Get all keys using keys() function - this will return a dict_keys()
print(l_prog.keys())

#display values of all keys
for key in l_prog.keys():
    print(l_prog[key])

#To get all values use values() and return dict_values which I've converted to a list here
print(list(l_prog.values()))

#To get key value pair from dictioanry - return dict_items
print(l_prog.items())

#Copy lists
l_prog_save = l_prog
#This will change l_prog too!
l_prog_save[400] = 'Michael Anderson'
print(l_prog)

#use copy() function to avoid the avoid situation
l_prog = {100: 'Sabyasachi Mitra',
          200: 'Jim Patrick',
          300: 'Var der Guisaam',
          400: 'Linus Tovald'
          }
l_prog_save = l_prog.copy()
#now only l_prog_save will change. l_prog will remain unaffected
l_prog_save[400] = 'Michael Anderson'
print(l_prog)
print(l_prog_save)

