import csv

def getTestList():
    content_array = []
    with open('testX.txt') as f:
            #Content_list is the list that contains the read lines.     
        for line in f:
            content_array.append(int(line.replace('\n','')))
        print(content_array)
        
def testing():
    labelNames = ["top", "trouser", "pullover", "dress", "coat",
        "sandal", "shirt", "sneaker", "bag", "ankle boot", 'Shirts', 
        'Jeans', 'Track Pants', 'Tshirts', 'Tops', 'Bra', 'Sweatshirts', 
        'Kurtas', 'Waistcoat', 'Shorts', 'Briefs', 'Sarees', 'Innerwear Vests', 
        'Rain Jacket', 'Dresses', 'Night suits', 'Skirts', 'Blazers', 'Kurta Sets', 
        'Shrug', 'Trousers', 'Camisoles', 'Boxers', 'Dupatta', 'Capris', 'Bath Robe', 
        'Tunics', 'Jackets', 'Trunk', 'Lounge Pants', 'Sweaters', 'Tracksuits', 'Swimwear', 
        'Nightdress', 'Baby Dolls', 'Leggings', 'Kurtis', 'Jumpsuit', 'Suspenders', 'Robe', 
        'Salwar and Dupatta', 'Patiala', 'Stockings', 'Tights', 'Churidar', 'Lounge Tshirts', 
        'Lounge Shorts', 'Shapewear', 'Nehru Jackets', 'Salwar', 'Jeggings', 'Rompers', 'Booties', 
        'Lehenga Choli', 'Clothing Set', 'Belts', 'Rain Trousers', 'Suits']
    d = {'key': 'value'}
    f= open("testX.txt","w+")
    f1 = open("matix.txt", "w+")
    list = []
    with open('styles.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        writer = csv.writer(csv_file)

        for row in csv_reader:
            # if line_count == 0:
            #     print(f'Column names are {", ".join(row)}')
            #     line_count += 1
            # else:
            if row[2] == 'Apparel':
                f1.write(row[0]+'\n')
                list.append(str(labelNames.index(row[4])))
                line_count += 1
                  
        print(f'Processed {line_count} lines.')
        print(d.keys())

    with open('testX.txt', 'w') as f:
        for item in list:
            f.write("%s\n" % item)
testing()