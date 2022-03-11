import random


def merge_1(list_one, list_two):
    return list_one + list_two


def merge_2(list_one, list_two):
    list_one.extend(list_two)
    return list_one


list_1 = ['Washington, D.C.', 'Chicago', 'New York']
list_2 = ['Los Angeles', 'Las Vegas']

print(merge_1(list_1, list_2))
print(merge_2(list_1, list_2))

a = ()
b = tuple("")
c = ("tupo",)
d = ([])
e = tuple()
print("a", type(a))
print("b", type(b))
print("c", type(c))
print("d", type(d))
print("e", type(e))

f = list("MikhailMorozov")
print(f)
for i in range(20):
    random.seed(i)
    random.shuffle(f)
    print("".join(f))

print("%.4f" % 3.14159265358979)
print("{1} {1} {1}".format(1, 2, 3))
# print("{1} is a {kind}".format(kind="fruit", "grapefruit"))
print("{city} is the capital of {country}".format(country="Portugal",
                                            city="Lisbon"))