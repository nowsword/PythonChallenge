import zipfile

def next_nothing(URL, nothing):
    file = open('6.out', 'wb')
    while True:
        print(nothing, end = '')
        txt_name = nothing + '.txt'
        text = zip.read(txt_name).decode()
        comment = zip.getinfo(txt_name).comment
        print(' comment[%r] ' % comment, end = '')
        file.write(comment)
        string = 'Next nothing is '
        pos = text.find(string)
        if pos == -1:
            print(':', text)
            break
        if pos != 0:
            print(':', text)
        else:
            print()
        nothing = text[pos + len(string):]
    file.close()

zip = zipfile.ZipFile('6.zip')
print(zip.read('readme.txt').decode())
nothing = '90052'
next_nothing(zip, nothing)

