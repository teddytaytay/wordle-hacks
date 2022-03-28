from hyper_wordbook import wordsize
from os import system as sys

def removeduplicates(x):
    return list(dict.fromkeys(x))
    
print("Getting Words..")

dictionary = removeduplicates(wordsize(5))

sys('clear')

one = []
two = []
three = []
four = []
five = []

right = list(input("Input The Correct Letters So Far (no spaces required): "))
wrong = list(input("Input The Incorrect Letters So Far (no spaces required): "))

x = 0

a = None

for i in dictionary:
    for j in i:
        if right[0] == j:
            one.append(i)
            a = one    
            
if len(right) > 1:
    for i in one:
        for j in i:
            if right[1] == j:
                two.append(i)
                a = two

if len(right) > 2:
    for i in two:
        for j in i:
            if right[2] == j:
                three.append(i)
                a = three

if len(right) > 3:
    for i in three:
        for j in i:
            if right[3] == j:
                four.append(i)
                a = four

if len(right) > 4:
    for i in four:
        for j in i:
            if right[4] == j:
                five.append(i)
                a = five

a = removeduplicates(a)

lst = []
for i in a:
    lst.append(i)
            
for i in lst:
    for j in wrong:
        if j in list(i):
            a.remove(i)
            break

o = input("(Click Enter For Nothing)\nGreen Letter In First Spot: ")
t = input("Green Letter In Second Spot: ")
th = input("Green Letter In Third Spot: ")
f = input("Green Letter In Fourth Spot: ")
fi = input("Green Letter In Fifth Spot: ")

lst = []
for i in a:
    lst.append(i)
for i in lst:
    if o != "":
        if i[0] == o: pass
        else: a.remove(i)
lst = []
for i in a:
    lst.append(i)
for i in lst:
    if t != "":
        if i[1] == t: pass
        else: a.remove(i)
lst = []
for i in a:
    lst.append(i)
for i in lst:
    if th != "":
        if i[2] == th: pass
        else: a.remove(i)
lst = []
for i in a:
    lst.append(i)
for i in lst:
    if f != "":
        if i[3] == f: pass
        else: a.remove(i)
lst = []
for i in a:
    lst.append(i)
for i in lst:
    if fi != "":
        if i[4] == fi: pass
        else: a.remove(i)
            
input("[ENTER] To View Results: ")

x = 0
for i in a:
    print(i)
    x += 1
print("\n" + str(x) + " Total Words")