import random
# loops from 0 to 9 - until 10
# numbers display 0-9
for x in range (0, 10):
    print x

print '\n'
grocery_list = ['Juice', 'Tomatoes','Potatoes', 'Bananas']
# print list
for y in grocery_list:
    print y

# loops though every defined option
for x in [2,3,4,5,6,7]:
    print x

num_list = [[1,2,3], [10,20,30], [100,200,300]]
# loop over multiple lists in the list
for x in range(0,3):
    for y in range(0,3):
        print num_list[x][y]


# WHILE LOOPS
random_num = random.randrange(0, 100)
print '---' * 3
while random_num != 15:
    print random_num
    random_num = random.randrange(0,100)
print '---' * 3
i = 0;
while i <= 20:
    if i%2 == 0:
        print i
    elif i == 9:
        break
    else:
        i += 1
        continue
    i+=1
