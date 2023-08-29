# Hint 1: You will need an append
# Hint 2: Using an empty list will make life easier




names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']

# nams2=

for i in names:
    while names.count(i) > 1:
        names.remove(i)

print(names)

#Another way, and that one makes sense. start at the beginning, and keep going through until there are no duplicates!!

i = 0

while i < len(names):
    if names.count(names[i]) > 1:
        names.remove(names[i])
    else:
        i+=1

print(names)







# integers= ()



# for int in int(range(len(names))):
    

# for s in names:
#     if str((names[0])) == str((names[s] + 1)): names.remove(s)

# print(names)