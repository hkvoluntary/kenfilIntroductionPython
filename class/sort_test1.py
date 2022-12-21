
"""
numbers = [1,10,6,4]
print(numbers)
print(numbers.sort())
print(numbers)
numbers = [1,43,8,34]
print(sorted(numbers))
print(numbers)

strs = ["ge", "1", "Ge", "banana"]
strs.sort()
print(strs)


numbers = [1,3,5,2]
numbers.sort(reverse=True)
print(numbers)


cars = [
    {'car':'Ford', 'year':2001},
    {'car':'BMW', 'year':2011},
    {'car':'Honda', 'year':2017},
    {'car':'VM', 'year':2011},    
]

def myFunc(e):
    return e['year']

cars.sort(key=myFunc)
print(cars)

cars = ['Ford','Honda', 'BMW', 'VM']
def myFunc2(e):
    return len(e)

cars.sort(reverse=True, key=myFunc2)
print(cars)

"""
people = {
    3:"Jim",
    2:"Jack",
    4:"Jane",
    1:"Jill"
}

print(people)
print(sorted(people))
print(people)
print(sorted(people.keys()))
print(sorted(people.values()))
print(sorted(people.items()))

def convert(tup,dictionary):
    dictionary = dict(tup)
    return dictionary

dictionary  = {}
print(convert(sorted(people.items()),dictionary))

