first_name = ['John', 'Evan', 'Jordan', 'Max']
last_name = ['Smith', 'Smith', 'Williams', 'Bell']
full_name = []

# Output: ['John Smith', 'Evan Smith', 'Jordan Williams', 'Max Bell']

def first_last(first_name, last_name):
    for p in range(len(first_name)):
        full_name = first_name[p] +  ' ' +  last_name[p]
        full_name.append(full_name)
    return full_name
    
final_name = first_last(first_name, last_name)

print(final_name)

# print(first_last)