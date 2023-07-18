import csv

# extreme shorthand you can also use
# does the same stuff, just with shortcut syntax
# with open('horse csv example.csv','r', encoding='utf-8') as infile:
#     headers, *data = csv.reader(infile)
#
# print(len(data))

infile = open('horse csv example.csv', 'r', encoding='utf-8')

csvin = csv.reader(infile)

# print( next(csvin) )
# the first line should always be the headers, almost always

headers = next(csvin)

data = []
for row in csvin:
    # this is where you could manipulate the data manually
    # as needed, depending on the situation
    # if len(row) != 7:
    #     print(row)
    data.append(row)

print(len(data))
namelengths = []
for row in data:
    horsename = row[1] # will get the name field
    namelengths.append(len(horsename))
    # if horsename.lower().startswith('a'):
    #     print(horsename)
    # print(row)
    # if '’' in horsename:
    #     horsename = horsename.replace('’', '\'')
    #     row[1] = horsename
    #     print(row)

namelengths.sort()
print(namelengths)

for row in data:
    if len(row[1]) == namelengths[-1]:
        print(row)

from collections import Counter

# print(Counter(namelengths))

# let's grab just the wikidata id and the name
smalldata = []
for row in data:
    # wd_id = row[0].split('/')[-1]
    wd_id = row[0].replace('http://www.wikidata.org/entity/', '')
    horsename = row[1]
    # print(wd_id, horsename)
    newrow = [wd_id, horsename] # make the new row
    smalldata.append(newrow) # collect it up

print(smalldata)

# writing out csv files
# have two things in order:
# the new headers (if needed) for the new file
newheaders = ['wikidata_id', 'horse_name']
# and the 2D list of data to write out
# which is what we just did in making smalldata

outfile = open('small horse data.csv', 'w', encoding='utf-8', newline='')
csvout = csv.writer(outfile)

# no assignments, because it's acting on the file itself
csvout.writerow(newheaders) # singular! takes a 1D list
csvout.writerows(smalldata) #plural! takes a 2D list

outfile.close()

