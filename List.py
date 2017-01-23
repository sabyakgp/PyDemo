#initialize a list
weekday = list()
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thusday', 'Friday']
print(weekdays)

#convert string to list
print (list('cat'))

#tuple to list
t_tuple = ('Monday', 'Tuesday', 'Wednesday', 'Thusday', 'Friday')
print(list(t_tuple))
#split a string by delimiter
sysdate='01-Jan-2017'
l_date= sysdate.split('-')
print('Day:', l_date[0])
print('Month:', l_date[1])
print('Year:', l_date[2])

# display list reverse
print(l_date[-1])

#Lists within lists
database = ['Oracle', 'HBase']
language = ['Python', 'Java', 'Scala']
skill = [language, database]
print(skill[0])

#add an item the list
newdb=['Exadata', 'Teradata']
database.append(newdb)
print(skill)

#combine lists using extend
language.extend(['R', 'SQL'])
#or using +=
database += ['MySQL', 'MarkLogic']
print(skill)

#insert item at offset
database.insert(2, 'SQL Server')
database.insert(-1, 'DB2')
database[3].insert(1, 'Netezza')
print(database)

#delete items
#del language[-2]
print(language.pop(-2))
print(language)

#using in operator in List
scala='Scala'
print(scala in language)

#using index
print(language.index(scala))

#using count
print(language.count('PL/SQL'))

#convert list to string - join - opposite of split
dlmit = ','
str_var = dlmit.join(language)
print(str_var)

#convert string to list - split - opposite of join
list_var = str_var.split(dlmit)
print(list_var)

#sort the list
numbers = [10, 2, 3, 4, 5, 6]
numbers.sort()
print(numbers)

#in-place change in List

a = [1, 2, 3, 4, 5]
b = a
#change in b will reflect in a
b[1] = 'Sabyasachi'
print(a)
print(b)

#use copy or list function to create a copy of List
city_india1 = ['Delhi', 'Kolkata', 'Mumbai', 'Hyderabad']
city_india2 = ['Ahmedabad', 'Kharagpur', 'Jamshedpur', 'Secuderabad']

city_india1 = city_india2.copy()
city_india1[0] = 'Bengalore'
print(city_india1)
print(city_india2)

# copy can be made using : and list unction as well
city_india1 = ['Delhi', 'Kolkata', 'Mumbai', 'Hyderabad']
city_india2 = ['Ahmedabad', 'Kharagpur', 'Jamshedpur', 'Secuderabad']

city_india1 = list(city_india2)
city_india1[0] = 'Bengalore'
print(city_india1)
print(city_india2)

#using :
city_india1 = ['Delhi', 'Kolkata', 'Mumbai', 'Hyderabad']
city_india2 = ['Ahmedabad', 'Kharagpur', 'Jamshedpur', 'Secuderabad']

city_india1 = city_india2[:]
city_india1[0] = 'Bengalore'
print(city_india1)
print(city_india2)