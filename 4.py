import urllib.request

def next_nothing(URL, nothing):
    while True:
        print(nothing, end = '')
        page = urllib.request.urlopen(URL + nothing)
        text = page.read().decode()
        string = 'and the next nothing is '
        pos = text.find(string)
        if pos == -1:
            print(':', text)
            break
        if pos != 0:
            print(':', text)
        else:
            print()
        nothing = text[pos + len(string):]

URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nothing = '12345'
next_nothing(URL, nothing)
nothing = '8022'
next_nothing(URL, nothing)
