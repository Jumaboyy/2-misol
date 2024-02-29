#masala1

# import csv
#
# users = [
#     {'username': 'tonny', 'followers': 987, 'online': True},
#     {'username': 'jimmy', 'followers': 1000, 'online': False},
#     {'username': 'tommy', 'followers': 1285, 'online': True},
#     {'username': 'mikky', 'followers': 822, 'online': True},
# ]
#
# a = 'users_info.csv'
# with open(a, 'w', newline='') as file:
#     b = ['username', 'followers', 'online']
#     writer = csv.DictWriter(file, fieldnames=b)
#     writer.writeheader()
#     for user in users:
#         writer.writerow(user)
# print(f"Ma'lumotlar {file} fayliga yozildi.")

# masala2
#
# import csv
#
# a = 'users_info.csv'
# with open(a, newline='') as file:
#     reader = csv.DictReader(file)
#     for natija in reader:
#      print(natija)


#3masala

import csv

# a = 'users_info.csv'
# b = 'users_info.txt'
# with open(a, newline='') as afile:
#     reader = csv.DictReader(afile)
#     with open(b, 'w') as bfile:
#         for row in reader:
#             bfile.write(f"Username: {row['username']}, Followers: {row['followers']}, Online: {row['online']}\n")
#
# print(f"Ma'lumotlar {b} fayliga yozildi.")

#4masala
# def qoshish(raqam):
#     try:
#         raqam = int(raqam)
#         natija = raqam + 2
#         print('\033[91m' + f"Natija: {natija}" + '\033[0m')
#     except ValueError:
#         print("Qabul qilinqan raqam - raqam emas")
#
# raqam = input("Istalgan raqamni kiriting: ")
# qoshish(raqam)

