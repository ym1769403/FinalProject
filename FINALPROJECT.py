import csv
from datetime import datetime
#Yasir Mushtaque
#1769403

manulist=[]
with open("ManufacturerList.csv", 'r') as m:
    for line in m:
        manulist.append(line.split(','))
price=[]
with open("PriceList.csv.", 'r') as p:
    for line in p:
        price.append(line.split(','))
date =[]
with open("ServiceDatesList.csv.", 'r') as d:
    for line in d:
        date.append(line.split(','))

FullInventory =[] # a. Create empty list for full inventory and append to manulist
for x in manulist:
    FullInventory.append(x)

for row in FullInventory:          # iterate and insert price
    for pricerow in price:
        if row[0] in pricerow:
            row.insert(3, pricerow[1])

for row in FullInventory: # iterate and insert date
    for daterow in date:
        if row[0] in daterow:
            row.insert(4, daterow[1])

with open("FullInventory.csv", 'w') as f:
    writer = csv.writer(f)
    FullInventory.sort(key=lambda FullInventory: FullInventory[1])  #sort manufacturer indexed at [1]
    writer.writerows(FullInventory)

LaptopInventory= []
for x in FullInventory:
    LaptopInventory.append(x)

FilterLaptop =[]
for laptoprow in LaptopInventory:   #row= all nested
    if laptoprow[2] in 'laptop':
        FilterLaptop.append(laptoprow)

with open("LaptopInventory.csv", 'w') as l:
    writer = csv.writer(l)
    FilterLaptop.sort(key=lambda FilterLaptop: FilterLaptop[0])
    writer.writerows(FilterLaptop)

PhoneInventory = []
for x in FullInventory:
   PhoneInventory.append(x)

FilterPhone =[]
for phonerow in PhoneInventory:   #row= all nested
    if phonerow[2] in 'phone':
        FilterPhone.append(phonerow)

with open("PhoneInventory.csv", 'w') as p:
    writer = csv.writer(p)
    FilterPhone.sort(key=lambda FilterPhone: FilterPhone[0])
    writer.writerows(FilterPhone)

TowerInventory= []
for x in FullInventory:
    TowerInventory.append(x)

FilterTower= []
for towerrow in TowerInventory:
    if towerrow[2] in 'tower':
        FilterTower.append(towerrow)

with open("TowerInventory.csv", 'w') as t:
    writer = csv.writer(t)
    FilterTower.sort(key=lambda FilterTower: FilterTower[0])
    writer.writerows(FilterTower)

now =datetime.now()         #find current date
current_date = now.strftime("%m/%d/%y")

date_list =[] # empty  list  to hold all of the dates
for x in FullInventory:
    date_list.append(x[4])  # date_list = all the dates

filter_list=[] # filters date past
for x in date_list:
    if x > current_date:
        filter_list.append(x)

PastServiceDateInventory= []
for x in FullInventory:
    if x[4] in  filter_list:
        PastServiceDateInventory.append(x)

with open("PastServiceDateInventory.csv", 'w') as p:
    writer = csv.writer(p)
    PastServiceDateInventory.sort(key=lambda PastServiceDateInventory: PastServiceDateInventory[4])
    writer.writerows(PastServiceDateInventory)

dmginvt = []
for x in FullInventory:
    dmginvt.append(x)

Filterdmg =[]     #empty list to filter dmg and append
for row in dmginvt:   #row= all nested
   if row[5] == 'damaged\n':
    Filterdmg.append(row)
    row.pop(5)  # damaged inventory created, remove damage from nested list

with open("DamagedInventory.csv", 'w') as d:
    writer = csv.writer(d)
    Filterdmg.sort(key=lambda Filterdmg: Filterdmg[3], reverse=True)  #reversed price sorting b/c price high to low
    writer.writerows(Filterdmg)

brand_list = []  # for query  filter out all brand names in one list
for brand in FullInventory:
    brand_list.append(brand[1])
item_list = []  # for query  filter out all items in one list
for item in FullInventory:
    item_list.append(item[2])
laptop_index = []      #these index to help in query find if item_type is laptop phone or tower without hard coding type into query
for laptop in FilterLaptop:
    laptop_index.append(laptop[2])
phone_index = []
for phone in FilterPhone:
    phone_index.append(phone[2])
tower_index =[]
for tower in FilterTower:
   tower_index.append(tower[2])

manufacturer_name = input("Enter manufacturer name.")
item_type = input(" Enter item type.")


while  manufacturer_name or item_type != 'q':
    if  manufacturer_name not in brand_list or item_type not in item_list:
        print ('No such item in inventory')
        break
    if manufacturer_name not in Filterdmg:  # not in damaged inventory
        if manufacturer_name not in PastServiceDateInventory: #not past service date
            if item_type in laptop_index:
                print('Your item  is:',FilterLaptop[0][0],FilterLaptop[0][1],FilterLaptop[0][2], FilterLaptop[0][3])
                print('You may also consider:',FilterLaptop[1][0],FilterLaptop[1][1] ,FilterLaptop[1][2] ,FilterLaptop[1][3])
                break
            elif item_type in phone_index:
                print('Your item  is:',FilterPhone[1][0], FilterPhone[1][1], FilterPhone[1][2] ,FilterPhone[1][3])
                print('You may also consider:',FilterPhone[0][0],FilterPhone[0][1], FilterPhone[0][2] ,FilterPhone[0][3])
                break
            elif item_type in tower_index:
                print('Your item  is:',FilterTower[0][0],FilterTower[0][1], FilterTower[0][2], FilterTower[0][3])
                print('You may also consider:',FilterTower[0][0],FilterTower[1][1] ,FilterTower[1][2] ,FilterTower[1][3])
            else:
                break