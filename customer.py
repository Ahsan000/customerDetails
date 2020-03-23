import pandas as pd

colnames = ['arrival_date', 'category', 'color', 'material_info', 'price', 'product_id', 'rating', 'size',
            'title']

data = pd.read_csv('products.csv', names=colnames)

arrival_date_list = list(data['arrival_date'])
category_list = list(data['category'])
color_list = list(data['color'])
material_info_list = list(data['material_info'])
price_list = list(data['price'])
product_id_list = list(data['product_id'])
rating_list = list(data['rating'])
size_list = list(data['size'])

# CATEGORY FILTER

# removing duplication from list
duplicate_items_category = list()
unique_items_category = []

for x in category_list:
    if x not in duplicate_items_category:
        unique_items_category.append(x)
        duplicate_items_category.append(x)

# ADDING DATA TO DICTIONARY
keys = []
for i in range(len(duplicate_items_category)):
    keys.append(i)

for i in duplicate_items_category:
    values_category = dict(zip(keys, duplicate_items_category))
# PRINTING VALUES FOR USER
print(values_category)

# TAKING INPUT FROM User
print("\n")

categoryuserinput = int(input("Enter Id of One Product's Category:"))
print("Your chosen category is:", duplicate_items_category[categoryuserinput])

print("\n")
print("Choose any of the Following Filter for this Category:")
print("press 1 for brand.")
print("press 2 for color.")
print("press 3 for size.")
print("press 4 for price_range.")
filteruserinput = int(input())

if filteruserinput == 1:

    print("Brand portion is empty.Choose another one")

elif filteruserinput == 2:

    # COLOR FILTER
    print("\nAvailable colors are below:")
    color_list = list(data['color'])

    # removing duplication from list
    duplicate_items_color = list()
    unique_items_color = []

    for x in color_list:
        if x not in duplicate_items_color:
            unique_items_color.append(x)
            duplicate_items_color.append(x)

    # ADDING DATA TO DICTIONARY
    keys = []
    for i in range(len(duplicate_items_color)):
        keys.append(i)

    for i in duplicate_items_color:
        values_color = dict(zip(keys, duplicate_items_color))
    print(values_color)

elif filteruserinput == 3:

    # SIZE FILTER
    print("\nAvailable sizes are below:")
    size_list = list(data['size'])

    # removing duplication from list
    duplicate_items_size = list()
    unique_items_size = []

    for x in size_list:
        if x not in duplicate_items_size:
            unique_items_size.append(x)
            duplicate_items_size.append(x)

    # ADDING DATA TO DICTIONARY
    keys = []
    for i in range(len(duplicate_items_size)):
        keys.append(i)

    for i in duplicate_items_size:
        values_size = dict(zip(keys, duplicate_items_size))
    print(values_size)

elif filteruserinput == 4:
    # PRICE_RANGE FILTER
    print("\nAvailable Prices are below:")
    price_list = list(data['price'])

    # removing duplication from list
    duplicate_items_price = list()
    unique_items_price = []

    for x in price_list:
        if x not in duplicate_items_price:
            unique_items_price.append(x)
            duplicate_items_price.append(x)

    # ADDING DATA TO DICTIONARY
    keys = []
    for i in range(len(duplicate_items_price)):
        keys.append(i)

    for i in duplicate_items_price:
        values_price = dict(zip(keys, duplicate_items_price))
    print(values_price)
else:
    print("\nChoose any of the given correct value.")

# FOLLOWING MENU TO USER
print("Choose Any of the Following Given Menu:\n"
      "a. Show max price 10 items\n"
      "b. Show min price 10 items\n"
      "c. Show top rated 10 items\n")
x = input()
ascendinglist=[]
if x == 'b':

    # PRICE_RANGE FILTER

    print("\nAvailable Prices are below:")
    price_list = list(data['price'])

    # removing duplication from list
    duplicate_items_price = list()
    unique_items_price = []
    newlist = []
    for x in price_list:
        if x not in duplicate_items_price:
            unique_items_price.append(x)
            duplicate_items_price.append(x)
    del duplicate_items_price[0]

    # MINIIMUM PRICES ARE BELOW
    ascendinglist = duplicate_items_price.copy()

    for i in range(0, len(ascendinglist)):
        ascendinglist[i] = int(ascendinglist[i])

    ascendinglist.sort()
    min_price_items = []
    i = 0
    for i in range(10):
        min_price_items.append(ascendinglist[i])

    print("10 Minimum Prices:", min_price_items)

elif x == 'a':

    # MAXIMUM PRICES ARE BELOW

    descendinglist = ascendinglist.copy()
    descendinglist.reverse()
    max_price_items = []
    i = 0

    for i in range(10):
        max_price_items.append(descendinglist[i])
    print("10 Maximum Prices :", max_price_items)

elif x == 'c':

    # RATING FILTER

    print("\nMaximum ratings are below:")
    rating_list = list(data['rating'])

    # removing duplication from list
    duplicate_items_rating = list()
    unique_items_rating = []

    for x in rating_list:
        if x not in duplicate_items_rating:
            unique_items_rating.append(x)
            duplicate_items_rating.append(x)

    # ADDING DATA TO DICTIONARY
    keys = []
    for i in range(len(duplicate_items_rating)):
        keys.append(i)

    for i in duplicate_items_rating:
        values_rating = duplicate_items_rating.copy()

    del values_rating[0]

    for i in range(len(values_rating)):
        values_rating[i] = int(values_rating[i])

    values_rating.sort()
    values_rating_rev = values_rating.copy()
    values_rating_rev.reverse()

    max_rating_list = []

    for i in range(10):
        max_rating_list.append(values_rating_rev[i])
    print(max_rating_list)
