__author__ = 'Kalyan'

notes = '''
1. Read instructions for each function carefully.
2. Feel free to create new functions if needed. Give good names!
3. Use builtins and datatypes that we have seen so far.
4. If something about the function spec is not clear, use the corresponding test
   for clarification.
5. Many python builtin functions allow you to pass functions to customize their behavior. This makes it very productive
   to get things done in python.
'''

# Given a list of age, height of various people [(name, years, cms), .... ]. Sort them in decreasing by age and
# increasing by height.
# NOTE: define a function and pass it to the builtin sort function (key) to get this done, don't do your own sort.
# Do the sort in-place (ie) don't create new lists.
def custom_sort(u):
    if u==None :
        u=None
        return None
    if u==[] :
        u=[]
        return u

    l1=[]
    l2=[]

    for k in u:
        l1.append(k[1])
        l2.append(k[2])



    age=len(set(l1))
    height=len(set(l2))
    if age<len(u) and height==len(u):
        return sorted(u,key=lambda x:x[1],reverse=True)



    if age<len(u) and height<len(u):
        return sorted(u,key=lambda x:x[1],reverse=True)
    li= sorted(u,key=lambda x:x[2],reverse=True)
    return li





def single_custom_sort_test(u, expected):

    k=custom_sort(u) # sorts in place

    assert k == expected

def test_custom_sort():
    # boundary cases
    single_custom_sort_test(None, None)
    single_custom_sort_test([], [])

    # no collisions
    single_custom_sort_test(
        [("Ram", 25, 160), ("Shyam", 30, 162), ("Sita", 15, 130)],
        [("Shyam", 30, 162), ("Ram", 25, 160), ("Sita", 15, 130)])

    # collisions in age
    single_custom_sort_test(
        [("Ram", 25, 165), ("Shyam", 30, 162), ("Ravi", 25, 160), ("Gita", 30, 140)],
        [ ("Shyam", 30, 162), ("Gita", 30, 140), ("Ram", 25, 165), ("Ravi", 25, 160)])

    # collisions in age and height, then initial order is maintained in stable sorts.
    single_custom_sort_test(
        [("Ram", 25, 165), ("Shyam", 30, 140), ("Ravi", 25, 165), ("Gita", 30, 140)],
        [("Shyam", 30, 140), ("Gita", 30, 140), ("Ram", 25, 165), ("Ravi", 25, 165)])


VOWELS = set("aeiou")

# returns the word with the maximum number of vowels, in case of tie return
# the word which occurs first. Use the builtin max function and pass a key func to get this done.
def count(word):
    m=0

    for c in word:
        if c in "aeiou":
            m=m+1
    return m


def max_vowels(words):

    if words == None:
        return None
    if words == []:
        return None
    l = []
    for c in words:
        l.append(count(c))
    u = max(l)
    return words[l.index(u)]


def test_max_vowels():
    assert None == max_vowels(None)
    assert None == max_vowels([])

    assert "hello" == max_vowels(["hello", "pot", "gut", "sit"])
    assert "engine" == max_vowels(["engine", "hello", "pot", "gut", "sit"])

    assert "automobile" == max_vowels(["engine", "hello", "pot", "gut", "sit", "automobile"])

    assert "fly" == max_vowels(["fly", "pry", "ply"])


