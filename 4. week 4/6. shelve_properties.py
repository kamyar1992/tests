import shelve
# shelve does not write in file exactly after changes in its properties
name= ['kamyar', 'Saba', 'Roozbe', 'Ramtin']
age = [30, 25, 32, 27]
city = ['Tehran', 'Mashhad', 'Tabriz']
# with shelve.open('testShelve.Shelve', writeback=True) as sFile:
with shelve.open('testShelve.Shelve') as sFile:
    sFile['NAME'] = name
    sFile['AGE'] = age
    sFile['CITY'] = city

    sFile['CITY'].append('Karaj')  # *important: it does not write in to file
    for item in sFile:
        print(sFile[item])
    print('='*40)
    tempList = sFile['CITY']
    tempList.append('Karaj')
    sFile['CITY'] = tempList # *important : it writes in file
    for item in sFile:
        print(sFile[item])