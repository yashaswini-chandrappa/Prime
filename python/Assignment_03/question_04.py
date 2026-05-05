'''Q4. Given a tuple of integers, create
• A tuple of all even numbers
• A tuple of all odd numbers 
'''
'''✅ 1. Using Generator Expression (Best & Pythonic)
Create tuples directly using tuple()
Clean and concise
even = tuple(x for x in t if x % 2 == 0)
odd = tuple(x for x in t if x % 2 != 0)

👉 ✔️ Readable
👉 ✔️ Efficient
👉 ✔️ Preferred in real code

✅ 2. Using Loops + List (Most Practical)
Store values in lists, then convert to tuple
even_list, odd_list = [], []

for x in t:
    if x % 2 == 0:
        even_list.append(x)
    else:
        odd_list.append(x)

even = tuple(even_list)
odd = tuple(odd_list)

👉 ✔️ Easy to understand
👉 ✔️ Good for exams/interviews
👉 ✔️ Efficient

⚠️ 3. Using Pure Tuple (No Lists)
Build tuple using concatenation
even, odd = (), ()

for x in t:
    if x % 2 == 0:
        even = even + (x,)
    else:
        odd = odd + (x,)

👉 ❌ Less efficient (creates new tuple each time)
👉 ✔️ Shows immutability concept
👉 ✔️ Used when lists are not allowed'''

tuple1 = (12,234,21,34,46,11,7,1235,352)
even_tuple = ()
odd_tuple = ()

for i in tuple1:
    if(i%2==0):
        even_tuple += (i,)
    if(i%2!=0):
        odd_tuple +=(i,)
print("The given tuple is : ",tuple1)
print("A tuple of all even numbers :",even_tuple)
print("A tuple of all odd numbers :",odd_tuple)
 