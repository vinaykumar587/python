#write a Python function to find 'Mall' from the dictionary 'map_details' given below.
map_details = {101:'Park', 102:'Zoo', 103:'Mall'}
def get_key(val):
    for key, value  in map_details.items():
        if val == value:
            return key
    return "key doesn't exist"

print(get_key('Mall'))
