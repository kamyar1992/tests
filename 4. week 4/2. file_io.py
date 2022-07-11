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
