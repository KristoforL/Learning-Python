#Making alist of dictionaries to reference

alien_0 = {'color':'green', 'points':5, }
alien_1 = {'color':'yellow', 'points':10, }
alien_2 = {'color':'red', 'points':15, }

aliens =[alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#I can make a list of dictionaries easily and nearly autonomously
#Going to start with an empty list and use the range method with a for looop to make aliens and add them to the dictionary

aliens =[]

for alien_number in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        aliein['points'] = 15
        
for alien in aliens[:5]:
    print(alien)
print("...")

print(f"Total number of aliens: {len(aliens)}")


