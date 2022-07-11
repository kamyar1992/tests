# path:
# absolute c:\Users
# .. in windows means that go back to previous folder
# . or \. means here in windows
# relative ..\scripts


# this is not pythonic
# fid = open('sample.txt')
# for line in fid:
#     print(line.strip())
# fid.close()


# context manager
with open('sample.txt') as fid:  # it is a pythonic way
    for line in fid:
        print(line.strip())

print("=" * 40)
# .readline() : read first line then wait for another call to read the next line
with open('sample.txt') as fid:
    line = fid.readline()
    while line:
        print(line.strip())
        line = fid.readline()

print("=" * 40)
# .readlines() : it return all lines as a list elements
with open('sample.txt') as fid:
    lines = fid.readlines()
print(lines)

print('=' * 40)
with open('sample.txt') as fid:
    rf = fid.read()
    rfChar = fid.read(5)

print(rf, '\n')
print('=' * 40)
with open('sample.txt') as fid:
    rfChar = fid.read(5)
print(rfChar)

# write in a file:
# with print()
with open('sampleWrite.txt', 'w') as fid:
    print('hello kamyar', file=fid)
    # readFile = fid.read()  *important it is a bug because the file was opened for writhing
    # print(readFile)
    # fid.seek(0)
    # print(fid.read())

# writelines()
lines = ['Kamyar\n', 'Mazaheri\n', str(30)+'\n']
with open('sampleWrite.txt', 'w') as fid:
    fid.writelines(lines)  # *important all iterable elements should be string
