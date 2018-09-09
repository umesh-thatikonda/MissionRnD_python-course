
__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Given a string of digits, you must return a list of all (substring, count) in the input string such that count >=2 and 
len(substring) >= 2. count represents the number of times the substring repeats in the input string (non-overlapping 
occurances).

The result must be sorted by count first (descending) and then in case of a tie the numerical value of 
substring (descending)

For e.g. if input is "123451236786712" you must return [("12", 3), ("123", 2), ("67", 2), ("23", 2)]

Notes:
1. if input is not a str, raise TypeError
2. Write clean bruteforce code to do this using python features. Do not devise new algorithms in the exam!
3. Write your own test cases 
'''


def get_substring(input_string):
    length = len(input_string)
    return [input_string[i:j + 1] for i in range(length) for j in range(i, length)]


def repeats(digits):
    if(type(digits).__name__!='str'):
        raise TypeError
    a=get_substring(digits)
    d=dict()
    for i in a:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1

    a2=[]
    for i in list(d.items()):
        if(len(i[0])>1 and (i[1]>1)):
            a2.append(i)

    a2.sort(key=lambda x:(x[1],int(x[0])),reverse=True)
    return a2


    pass


def test_repeats():
    assert [("12", 3), ("123", 2), ("67", 2), ("23",2)] == repeats("123451236786712")
    assert [("12",2)]==repeats("12123456789")
    print(repeats("12301230"))
    assert [("123",2),("30",2),("12",2)]==repeats("12301230")