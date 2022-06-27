
mobile = {
    'color' : 'Red',
    'height' : 5.6,
    'weight' : '200gms'
}

print(mobile['height'])

mobile['camera'] = '24px'


mobile['height'] = '6.7'


# clear

# mobile.clear()

print(mobile)

# copy -> after 

# fromkeys

newdict = dict.fromkeys(['a','b','c'])


# get

height = mobile.get('height')


# keys -> get list of keys from dict

k = mobile.keys()

# values -> get list of values from dict

v = mobile.values()

print(v)