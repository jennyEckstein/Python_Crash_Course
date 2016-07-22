

# tuples you cannot change after you create them
pi_tuple = (3,1,4,1,5,9)

# you can convert tuple to list alter and them convert back to tuple
list_tuple = list(pi_tuple)
print list_tuple
new_tuple  = tuple(list_tuple)
print new_tuple
# length/max/min
print len(new_tuple)
print min(new_tuple)
print max(new_tuple)