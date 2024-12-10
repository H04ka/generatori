print("Задание", 1)
gen_class = (i**3 for i in range(1, 6))
print(type(gen_class))
print(next(gen_class))
print(next(gen_class))
print(next(gen_class))
print(next(gen_class))
print(next(gen_class))

print("Задание", 2)
def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b

gen_class = (c for c in fibonacci(11))
print(next(gen_class))
print(next(gen_class))
print(next(gen_class))
print(next(gen_class))
print(next(gen_class))
print(next(gen_class))
print(next(gen_class))
print(next(gen_class))
print(next(gen_class))
print(next(gen_class))

print("Задание", 3)
def get_even(gen_list):
    for i in gen_list:
        if i % 2 == 0:
            yield i

gen_list = list(range(1, 101))
print("До" + str(gen_list))
print("После", end= " ")
for i in get_even(gen_list):
    print(i, end = " ")

print("Задание", 4)
fruits = ['mango', 'banana', 'orange']

first_letter = [l[0] for l in fruits]
print(type(first_letter))
print(first_letter)
filtered = [len(fruits) for fruits in fruits]
print(filtered)
lenght = [fruits for fruits in fruits if len(fruits) <3]
print(lenght)

print("Задание", 5)
people = {'Nightwalker': 22, 'obstul': 16, 'John Cena': 19, 'Diana': 14}
variable = {key: age for key, age in people.items() if age > 18}
print(variable)

print("Задание", 6)
metrs = {1, 1.5, 2, 4.4, 5.3}
metr_to_sm = {metrs:metrs*100 for metrs in metrs}
print(metr_to_sm)

print("Задание", 7)
import string
import random

def generate_email(num_adress):
    domains = ['example.com', 'test.com', 'myemail.com', 'sample.net', 'demo.org']
    for _ in range(num_adress):
        em = ''.join(random.choices(string.ascii_lowercase, k = 8))
        domain = random.choice(domains)
        yield f"{em}@{domain}"

for email in generate_email(10):
    print(email)
