#defining set using set() function
s_set = set((1977, 'Software Engineer', 'Hyderabad', 'India', 98.5))
print('#defining set using set() function')
print(s_set)

#defining set using {} - Sets are always unordered
s_set = {1977, 'Software Engineer', 'Hyderabad', 'India', 98.5}
print('#defining set using {} - Sets are always unordered')
print(s_set)

#defining empty set
s_set = set()
print('#defining empty set')
print(s_set)

#using Set with Dictionary to define a key value pair
d_employee = {
    'Sabya': {1977, 'Software Engineer', 'Hyderabad', 'India', 98.5},
    'John': {1981, 'Business Analyst', 'Newyork', 'USA', 96.5}
}
print('#using Set with Dictionary to define a key value pair')
print(d_employee['John'])

#using for loop to print value using key stored in a list
l_emp = ['Sabya', 'John', 'Mike']
print('#using for loop to print value using key stored in a list')
for key in l_emp:
    if key in d_employee.keys():
        print(d_employee[key])
    else:
        print('Not Found')

#display key and value of a dictionary using for loop
print('#display key and value of a dictionary using for loop')
for key, record in d_employee.items():
        print(record)

d_database = {
    'RDBMS': {'Oracle', 'SQL Server', 'MySQL', 'PostGre'},
    'NoSQL': {'HBase', 'Cassendra', 'Mongo'}
}

