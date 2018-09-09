__author__ = 'Kalyan'

max_marks = 25  # encrypt -> 13, decrypt 12

problem_notes = '''
Write encryption and decryption routines according to the given scheme. 

A secret key is used to encrypt a text message in the following manner: 
- key is a string of letters in which each letter represents the right displacement of the source 
character (a -> 0, z-> 25)
- text -> input text to be sent 

Letters of the input text are mapped to the letters in the key in a round robin manner. For e.g:

For: key = "abcde", text="hi there", the mapping is 
h->a, i -> b, (space is ignored) t ->c, h -> d, e-> e, (go back to starting a here) r -> a, e->b 

now to get the encrypted text, you move h by 0, i by 1, t by 2, h by 3 etc. So you finally get the text "hj vkirf"

The decryption works in the reverse way and returns the original text.

Notes:
- Preserve the casing(lower case remains lower case, Upper case remains Upper case).
- Ignore non-letters and punctuations, i.e., leave them as is in the final result
- For displacement, both small and large letters represent the same displacement. For e.g. b and B both represent 1
- raise TypeError if text and key are not strings.
- raise ValueError if key is empty or has non alphabet characters

Write helper sub routines as required. Make good use of the available datatypes!
'''

# do type checking, non-str should raise TypeException
def encrypt(text, key):


    if(type(key).__name__!='str' and type(text)!='str'):
        raise TypeError
    import string
    s=string.ascii_lowercase
    u=string.ascii_uppercase
    k=key
    while True:
        k+=k
        if(len(k)>=len(text)):
            break
    a=[]
    j=0

    for i in range(len(text)):
        if(text[i]==" "):
            a.append(" ")
            continue
        if(ord(text[i])>65 and ord(text[i])<91):
            u=(ord(text[i])+
            j+=1
            if(u>91):
                u=64+(u-91)
            a.append(chr(u))

        else:
            u=(ord(text[i])+ord(k[j])-ord('a'))
            j+=1
            if(u>122):
                u=96+(u-122)
            a.append(chr(u))

    return "".join(a)

    pass

def decrypt(text, key):
    if (type(key).__name__ != 'str' and type(text) != 'str'):
        raise TypeError
    import string
    s = string.ascii_lowercase
    u = string.ascii_uppercase
    k = key
    while True:
        k += k
        if (len(k) >= len(text)):
            break
    a = []
    j = 0

    for i in range(len(text)):
        if (text[i] == " "):
            a.append(" ")
            continue
        if (ord(text[i]) > 65 and ord(text[i]) < 91):
            u = (ord(text[i]) - ord(k[j]) + ord('A'))
            j += 1
            if (u > 91):
                u = 64 + (u - 91)
            a.append(chr(u))

        else:
            u = (ord(text[i]) - ord(k[j]) + ord('a'))
            j += 1
            if (u > 122):
                u = 96 + (u - 122)
            a.append(chr(u))

    return "".join(a)

    pass


def test_encrypt():
    assert "hj vkirf" == encrypt("hi there", "abcde")
    #assert "<class 'ValueError'>"==encrypt('mysecretmessage', 'invalid10')
    assert "hj vkirf" == encrypt('mysecretmessage', 'secret')
def test_decrypt():
    assert "hi there" == decrypt("hj vkirf", "abcde")

