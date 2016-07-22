
# Define list
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']

# Print first item on the list
print 'First Item: ', grocery_list[0]

grocery_list[0] = 'Orange Juice'
print 'First Item: ', grocery_list[0]

# Print a range of items from the list
print grocery_list[1:3] # 3 is not included - from 1 until 3

other_events = ['Wash Car',
                'Pick Up Kids',
                'Cash Check']

# You can put 2 lists together
to_do_list = [other_events, grocery_list]
print to_do_list # now there are lists inside a list

# Now to print 2nd item from the second list
print to_do_list[1][1] # almost like 2D arrays

# Can append to the list
grocery_list.append('Onions')
print to_do_list

#insert at specific index
grocery_list.insert(0, 'Pickles')
print to_do_list

#remove from the list
grocery_list.remove('Pickles')
print  to_do_list

# sort in descending order
grocery_list.sort()
grocery_list.reverse()

print grocery_list

#delete from the list
del grocery_list[4]
print grocery_list

# append 2 lists
to_do_list2 = other_events + grocery_list
print to_do_list2

# get lists length, max and min are whatever first/last alphabetically
print len(to_do_list2)
print max(to_do_list2)
print min(to_do_list2)



