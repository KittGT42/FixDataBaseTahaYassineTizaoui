import csv

counter = 0
with open('result.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        counter += 1
        print(counter)
        print(row)

# counter = 0
# #
# with open('noon_v5.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         counter += 1
#         print(counter)
#         print(row)
#         if 'Jaysuing 2 Piece Set ' in row[0]:
#             print(row)
#             print(counter)



