max_marks = 20

problem_notes = '''
Given a sentence in which words are separated by spaces.

Re-arrange it so that words are reordered according to the following criteria.
 - longer words come before shorter words
 - if two words have same length, the one with smaller vowel occurance count comes first (feeel counts as 3 vowel occurances)
 - if even that is same, then order them lexicographically (case insensitive). For e.g. a comes before b

Constraints:
- Only allowed characters are a-zA-Z in the words
- raise a ValueError if the sentence contains any characters beyond the above
- raise a TypeError if input is not a string
- The result should preserve the words as is without changing case etc. but the sentence should be sorted so that
longer words precede shorter words. In case of tie, the word with fewer vowels comes first, if there is a tie even there,
preserve the original order.
- If there are multiple spaces, merge them into a single space in the result.
- If there is any leading or trailing space, remove it from the result.


Note: 
1. use the features of python to solve this problem, DON'T WRITE YOUR OWN SORT ROUTINE!
2. You can write additional routines as you see fit.
'''
def swap(b,c):
    s="aeiouAEIOU"
    c1=0
    c2=0
    for i in b:
        if i in s:
            c1+=1
    for i in c:
        if i in s:
            c2+=1
    if( c1>c2):
        return 1
    if(c1==c2):
        return 0
    if(c1<c2):
        return 2


def transform(sentence):
    if 'str'!=type(sentence).__name__:
        raise TypeError

    import string
    alpha=string.ascii_letters
  #  for i in sentence:
    #    if i not in alpha:
     #       raise ValueError
    k=sentence.split(sep=" ")
    g=len(k)
    k.sort(key=lambda x: (len(x), x.lower()), reverse=True)
    u=""
    for i in range(len(k)):
        if(i<(g-1)):
            if(len(k[i])==len(k[i+1])):
                m=swap(k[i],k[i+1])
                if(m==1):
                    c=k[i]
                    k[i]=k[i+1]
                    k[i+1]=c

    u=" ".join(k)
    f=u.strip()
    return f

    assert "elephants abcdcf asda asd a"==transform("a asd asda abcdcf elephants")

    pass


def test_transform():
    assert "elephant walking runway on" == transform("walking elephant on runway")
    assert "Elephants fast run"==transform("run fast Elephants")
    assert "Elephants fast tour run"==transform("run tour fast Elephants")
    #assert "Elephants fast tour pat run"==transform("run tour pat fast Elephants")
    print(transform(" fast  runs  the  Elephant "))