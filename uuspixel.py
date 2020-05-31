from PIL import Image
from implementation import *
import time
algus = time.time()

punktid = [(380, 108),(195, 299)] #There can be more than 2 points


'''
for i in range(len(pixel_values)):
    if pixel_values[i] == (255, 201, 14, 255):
        string += 'A'
    if pixel_values[i] == (153, 217, 234, 255):
        string += 'B'
    if pixel_values[i] == (195, 195, 195, 255):
        string += 'C'
    if pixel_values[i] == (200, 191, 231, 255):
        string += 'D'
    if pixel_values[i] == (255, 174, 201, 255):
        string += 'E'
    if pixel_values[i] == (239, 228, 176, 255):
        string += 'R'
    if (i+1)%20 == 0:
        print(string)
        string = ''
'''


image = Image.open('väiketamsalu.png', 'r')
widthp, heightp = image.size
pixel_values = list(image.getdata())
table = []


for a in range(widthp):
    for b in range(heightp):
        ruut = a, b
        table.append(ruut)


värvid = {}
for i in range(len(table)):
    värvid[table[i]] = pixel_values[i]


diagram4 = GridWithWeights(widthp, heightp)

värvid2 = {}

'''
    for a in range(widthp):
        for b in range(heightp):
            ruut = a, b
            if värvid[ruut] == (255, 201, 14): #tumekollane
                värvid2[ruut] = 5000
            if värvid[ruut] == (153, 217, 234): #sinine
                värvid2[ruut] = 30000
            if värvid[ruut] == (195, 195, 195): #hall
                värvid2[ruut] = 20
            if värvid[ruut] == (200, 191, 231): #lilla
                värvid2[ruut] = 40
            if värvid[ruut] == (255, 174, 201): #helekollane
                värvid2[ruut] = 100
            if värvid[ruut] == (239, 228, 176): #roosa
                värvid2[ruut] = 400
'''
for a in range(widthp):
    for b in range(heightp):
        ruut = a, b
        if 35 < värvid[ruut][0] < 45 and  160 < värvid[ruut][1] < 185 and 10 < värvid[ruut][2] < 23:
        #if värvid[ruut] == (24, 176, 0, 255):  # roheline
            värvid2[ruut] = 1
        else:  # muu
            värvid2[ruut] = 15

diagram4.weights = värvid2

path = ()

for i in range(len(punktid)-1):
    start = punktid[i]
    goal = punktid[i+1]
    print(goal)
    
    came_from, cost_so_far = a_star_search(diagram4, start, goal)
    path += tuple(reconstruct_path(came_from, start=start, goal=goal))


pixel_values = [(255, 0, 0, 255) if table[x] in path else pixel_values[x]
                for x in range(len(pixel_values))]
im2 = Image.new(image.mode, image.size)
im2.putdata(pixel_values)
im2.save('väiketamsaluval.png')
lõpp = time.time()
print(len(path))
print(lõpp-algus)
