
# Dictionaries/Maps
# Key for each value you store
# you cannot join disctionaries
titanic_cast = {'Jack Dawson': 'Leonardo DiCaprio',
                'Rose DeWitt Bukater':'Kate Winslet',
                'Caledon \'Cal\' Hockley':'Billy Zane',
                'Molly Brown': 'Kathy Bates',
                'Ruth Dewitt Bukater':'Frances Fisher'}

print(titanic_cast['Jack Dawson'])

del titanic_cast['Caledon \'Cal\' Hockley']

print titanic_cast

#replace the value
titanic_cast['Rose DeWitt Bukater'] = 'K Winslet'

print titanic_cast
print len(titanic_cast)

print titanic_cast.get("Molly Brown")

print titanic_cast.keys()

print titanic_cast.values()