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
database = ['Oracle', 'SQL Server', 'HBase']
language = ['Python', 'Java', 'Scala']
skill = [language, database]
print(skill[0])

#add an item the list
database.append('PostgreSQL')
print(skill)



