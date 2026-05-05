'''Q3. Input two lists of integers from the user. Merge them into one list and sort the result.
Eg-,list1 = [1, 2, 7]list2 = [2, 4, 5]result = [1, 2, 3, 54, 5, 7]'''

list1 = [1,2,7]
list2 = [2,5,4]
result = list1+list2
# result = result.sort() #  sort() does not return anything (it returns None).
#                            It sorts the list in place, so when you assign it back to result, you lose your list.
result.sort()
print("The sorted list is :",result)