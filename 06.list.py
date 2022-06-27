

a = [1,2,3,4,5]


print(a[2])

print(a[-2])


# length of list

len(a)

# adding an element to list

a.append(6)
a.append(6)


# insert -> insert an element at any position

a.insert(2,44)

# extend -> add a list to end of another list

l1 = [1,1,2,3,4,5]
l2 = [6,7,8,9,10]

l1.extend(l2)

# count -> count no of times an element occurs in a list

count = l1.count(1)

# sum -> find the sum of the list

total = sum(l1)

# min -> find min value in a list

m = min(l1)

#max -> Finx max value in a list

ma = max(l1)

# index -> retuns the index of the given element

i = l1.index(4)

# sort -> sort a list in ascending or descending

l1.sort(reverse=True)


# pop -> remove last element of a list
l1.pop()

# del -> delete an element

del l1[3]

# remove -> remove an element from list

l3 = [1,2,3,3]
l3.remove(3)


