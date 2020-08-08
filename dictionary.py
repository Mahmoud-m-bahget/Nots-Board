import json
from difflib import get_close_matches
data = json.load(open('data.json'))
word = input('write the word here ? \n')
def trancelator():
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper()in data:
        return data[word.upper()]
    elif len (get_close_matches(word , data.keys())) > 0 :
        print('did you mean %s instaed ?' %get_close_matches(word ,data.keys(),cutoff=0.8))
        decided = input('enter (y) for yes (n)  for no\n ')
        if decided == 'y':
            return data[get_close_matches(word,data.keys())[0]]
        elif decided =='n':
            print('the word dosent exist ')
        else:
            print('please enter y for yes n for no')
    else:
        print('the word not found ')
out = trancelator()
if type(out)== list:
    for i in out:
        print(i)
else:
    print(out)

print(out)

