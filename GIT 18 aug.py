a= "ABCAAC1C" #print(a.count("A"))

def strcounter(a):
    for char in (a) : #O(N**2)
        counter = 0
        for sub_char in a:
            if char==sub_char:
                counter+=1
        print(char, counter)


def strcounter1(a):
    for char in set(a) : #O(N*M)
        counter = 0
        for sub_char in a:
            if char==sub_char:
                counter+=1
        print(char, counter)

def strcounter2(a): #O(N)
    syms_counter = {}
    for char in a:
        syms_counter[char] = syms_counter.get(char, 0) + 1
    print(syms_counter)

strcounter2(a)