from itertools import product


"""""""""
stores = [
    {"store": "kralja petra",
     "products":[
         {"product":"ice cream", "categories": ["vanila","cokolada","malina"]},
         {"product": "juice", "categories": ["orange","cocacola","ice tea"]},

     ]},
    {"store": "njegoseva",
     "products": [
         {"product": "ice cream", "categories": ["cinamon", "sumskovoce", "valnnut"]},
         {"product": "milkshake", "categories": ["cappucino", "vanilla", "ice tea"]},

     ]}
    ]




def get_categories (stores,product_name,store_name):
    for store in stores:
        if store["store"] == store_name:
            for product in store["products"]:
                if product["product"] == product_name:
                    return product["categories"]
    return []

print(get_categories(stores,"ice cream","njegoseva"))
print(get_categories(stores,"milkshake","njegoseva"))
"""""""""

"""""""""
def odd_even(nums):
    total = sum(nums) if nums else 0
    return "even" if total % 2 == 0 else "odd"

print(odd_even([1,2,4]))


"""""""""
"""""""""
def digital_root(num):
    while num >= 10:
        num = sum(int(c) for c in str(num))

    return num
print(digital_root(25))
print(digital_root(152))

"""""""""
"""""""""
nums = [-1,2,0,3,4,-5,6,7,-8,9]

def max_sum(nums):
    total = 0
    for num in nums:
        if num >=0:
            total += num
    return total

print(max_sum(nums))
"""""""""
"""""""""
def name_list(names):
    names = [person['name'] for person in names]

    if not names:
        return ''
    elif len(names) == 1:
        return names[0]
    elif len(names) == 2:
        return f"{names[0]} & {names[1]}"
    else:
        return ", ".join(names[:-1]) + " & " + names[-1]


print(name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
print(name_list([{'name': 'Bart'}, {'name': 'Lisa'}]))
print(name_list([{'name': 'Bart'},]))
print(name_list([]))
"""""""""""
"""""""""""
s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";


def meeting(s):
    people = s.upper().split(";")
    formated_people = []
    for person in people:
        first, last = person.split(":")
        formated_people.append((last, first))

    formated_people.sort()

    return "".join(f"({last}, {first})" for last, first in formated_people)


print(meeting(s))
"""""""""
"""""""""
text = input('enter text: ')
reversed = text[::-1]
print("reversed:",reversed)
"""""""""

def move_zeroes(arr):
    non_zero = [x for x in arr if x != 0]

    zero_count = arr.count(0)
    return non_zero + [0] * zero_count

print(move_zeroes([0,1,0,3,12,0]))



