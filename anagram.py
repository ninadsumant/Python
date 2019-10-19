'''stringOne = "events"
stringTwo = "steven"


def is_anagram(stringOne, stringTwo):
    print sorted(stringOne) == sorted(stringTwo)

is_anagram(stringOne, stringTwo)'''

def is_anagram(string1, string2):
    """return True if strings are anagrams of each other"""
    list1 = list(string1)
    list2 = list(string2)
    list1.sort()
    list2.sort()
    return list1 == list2

if __name__ == '__main__':
    string1='abcdef'
    string2='fedcba'
    print (is_anagram(string1, string2))

