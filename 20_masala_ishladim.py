#####################################################################################
#####################Listlardan algoritm masalar#####################################
#####################################################################################
##1-Masala
# fruts = ['olma','banan','uzum']
# fruts.index('banan')
# fruts.append("nok")
# print(len(fruts))
# if 'olma' in fruts:
#     print('True')
# else:
#    print('False')
# print(fruts)
##2-Masala
# colors = ['qizil', 'yashil', "ko'k"]
# colors.append('sariq')
# colors.sort()
# print(len(colors))
# print('yashil' in colors)
# print(colors)
# ##3-Masala
# cities = ['Toshkent', 'Samarqand', 'Buxoro']
# cities.append('Xiva')
# print(cities.index('Samarqand'))
# print(len(cities))
# cities.sort()
# print(cities)
# ##4-Masala
# numbers = [5, 2, 8, 1]
# numbers.append(10)
# numbers.sort()
# print(len(numbers))
# print(8 in numbers)
# print(numbers)
# ##5-Masala
# animals = ['mushuk', 'it', 'qush']
# animals.append('baliq')
# animals.sort()
# print(animals.index('it'))
# print(len(animals))
# print(animals)
# ##6-Masala
# fruits = ['olma', 'banan', 'uzum', 'nok']
# fruits.append('kivi')
# fruits.remove('banan')
# fruits.insert(fruits.index('nok'), 'shaftoli')
# fruits.sort()
# print(len(fruits))
# print(fruits.index('olma'))
# print('kivi' in fruits)
# fruits.sort(reverse=True)
# copy_fruits = fruits.copy()
# copy_fruits.append('ananas')
# print(fruits)
# print(copy_fruits)
# ##7-Masala
# menu = ['osh', "lag'mon", 'shashlik', 'somsa']
# menu.extend(['manti', 'norin'])
# menu.remove("lag'mon")
# menu.sort()
# menu.pop()
# print(len(menu))
# print(menu.index('osh'))
# print(menu.count('somsa'))
# print('manti' in menu)
# copy_menu = menu.copy()
# copy_menu.append('qozon kabob')
# print(menu)
# print(copy_menu)
# ##8-Masala
# cities = ['Toshkent', 'Samarqand', 'Buxoro', 'Xiva']
# cities.insert(0, 'Andijon')
# cities.remove('Xiva')
# print(cities.index('Samarqand'))
# cities.sort()
# print(len(cities))
# print('Buxoro' in cities)
# cities.pop()
# cities.sort(reverse=True)
# copy_cities = cities.copy()
# copy_cities.append("Farg'ona")
# print(cities)
# print(copy_cities)
# ##9-Masala
# students = ['Ali', 'Vali', 'Sardor', 'Aziz']
# students.append('Jamshid')
# students.remove('Sardor')
# students.insert(students.index('Vali'), 'Diyor')
# students.sort()
# print(students.index('Aziz'))
# print('Diyor' in students)
# students.pop()
# print(len(students))
# copy_students = students.copy()
# copy_students.append('Nodir')
# print(students)
# print(copy_students)
# ##10-Masala
# favorites = ['telefon', 'noutbuk', 'naushnik']
# favorites.append('planshet')
# favorites.append('soat')
# favorites.sort()
# print(len(favorites))
# print(favorites.index('noutbuk'))
# print('telefon' in favorites)
# favorites.remove('naushnik')
# favorites.pop()
# copy_fav = favorites.copy()
# copy_fav.append('televizor')
# favorites.sort(reverse=True)
# print(favorites)
# print(copy_fav)
# ##11-Masala
# songs = ['Yomg\'ir', 'Sevgi', 'Hayot', 'Kuz']
# songs.insert(songs.index('Sevgi'), 'Bahor')
# songs.remove('Kuz')
# songs.sort()
# print(songs.index("Yomg'ir"))
# print('Hayot' in songs)
# songs.pop()
# print(len(songs))
# songs.sort(reverse=True)
# copy_songs = songs.copy()
# copy_songs.append('Yoz')
# print(songs)
# print(copy_songs)
# ##12-Masala
# books = ['Alximik', 'Shaytanat', '1984']
# books.extend(["O'tkan kunlar", 'Sariq devni minib'])
# books.remove('Shaytanat')
# books.sort()
# print(books.index('1984'))
# print('Alximik' in books)
# books.pop()
# print(len(books))
# books.sort(reverse=True)
# copy_books = books.copy()
# copy_books.append('Qirq yil')
# print(books)
# print(copy_books)
# ##13-Masla
# movies = ['Inception', 'Matrix', 'Interstellar']
# movies.append('Parasite')
# movies.remove('Matrix')
# movies.sort()
# print(movies.index('Inception'))
# print('Interstellar' in movies)
# movies.pop()
# print(len(movies))
# movies.sort(reverse=True)
# copy_movies = movies.copy()
# copy_movies.append('Joker')
# print(movies)
# print(copy_movies)
# ##14-Masala
# emails = ['job_offer', 'spam', 'friend', 'news']
# emails.append('family')
# emails.remove('spam')
# emails.sort()
# print(emails.index('friend'))
# print('job_offer' in emails)
# emails.pop()
# print(len(emails))
# emails.sort(reverse=True)
# copy_emails = emails.copy()
# copy_emails.append('urgent')
# print(emails)
# print(copy_emails)
# ##15-Masala
# friends = ['Ali', 'Zara', 'Bobur', 'Nodir']
# friends.append('Jamol')
# friends.remove('Nodir')
# friends.sort()
# print(friends.index('Zara'))
# print('Ali' in friends)
# friends.pop()
# print(len(friends))
# friends.sort(reverse=True)
# copy_friends = friends.copy()
# copy_friends.append('Sardor')
# print(friends)
# print(copy_friends)
# ##16-Masala
# animals = ['sher', 'yo\'lbars', 'ayiq', 'sher', 'quyon']
# print(animals.count('sher'))
# animals.remove('ayiq')
# animals.append('kenguru')
# animals.sort()
# print(animals.index("yo'lbars"))
# print('quyon' in animals)
# animals.pop()
# print(len(animals))
# copy_animals = animals.copy()
# copy_animals.append('tuya')
# print(animals)
# print(copy_animals)
# ##17-Masala
# champions = ['Khamzat Chimaev', 'Khabib Nurmagomedov', 'Conor McGregor', 'Mike Tyson', 'Wladimir Klichko', 'Eliud']
# print(champions.count('Mike Tyson'))
# champions.pop()
# champions.extend(['Bahodir Jalolov', "Hasanboy Do'smatov"])
# champions.sort()
# print(champions.index('Mike Tyson'))
# print('Khabib Nurmagomedov' in champions)
# champions.remove('Conor McGregor')
# print(len(champions))
# copy_champions = champions.copy()
# copy_champions.append("Shaxram G'iyasov")
# print(champions)
# print(copy_champions)
# ##18-Masala
# cart = ['non', 'suyut', 'tuxum', "go'sht"]
# print(cart.index('tuxum'))
# cart.remove('suyut')
# cart.extend(["sari yog'", 'murabbo'])
# cart.sort()
# copy_cart = cart.copy()
# copy_cart.append('shakar')
# cart.clear()
# print('non' in cart)
# print(len(cart))
# copy_cart.pop()
# print(cart)
# print(copy_cart)
# ##19-Masala
# courses = ['Python', 'Java', 'Data Science', 'Python']
# print(courses.count('Python'))
# courses.remove('Java')
# courses.extend(['AI', 'Web Development'])
# courses.sort()
# print(courses.index('Data Science'))
# print('AI' in courses)
# courses.pop()
# courses.remove('Python')
# print(len(courses))
# copy_courses = courses.copy()
# copy_courses.append('Blockchain')
# print(courses)
# print(copy_courses)
# ##20-Masala
# cars = ['Chevrolet', 'Hyundai', 'Kia', 'Toyota']
# cars.insert(0, 'BMW')
# cars.remove('Kia')
# copy_cars = cars.copy()
# cars.sort()
# print(cars.index('Toyota'))
# print('Hyundai' in cars)
# cars.pop()
# print(len(cars))
# cars.sort(reverse=True)
# cars.clear()
# copy_cars.append('Mercedes')
# print(cars)
# print(copy_cars)
###########################
####Tyuple#MASALAR#10ta####
###########################
##1-Masala
# days = ('Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma')
# print(len(days))
# print('Juma' in days)
# print(days.index('Chorshanba'))
# print(days[1])
# print(days[-2:])
# lst = list(days)
# lst.append('Shanba')
# lst.append('Yakshanba')
# days = tuple(lst)
# print(len(days))
# print(days)
##2-Masala
# python
# Copy code
# colors = ('qizil', 'yashil', "ko'k", 'sariq')
# print('yashil' in colors)
# print('qora' not in colors)
# print(len(colors))
# print(colors.index("ko'k"))
# lst = list(colors)
# lst.append('pushti')
# colors = tuple(lst)
# print(colors[1:3])
# new_colors = colors * 2
# print(len(new_colors))
# print(new_colors)
##3-Masala
# python
# Copy code
# cities = ('Toshkent', 'Buxoro', 'Xiva', 'Samarqand')
# print(cities.index('Buxoro'))
# print(len(cities))
# print('Navoiy' not in cities)
# print(cities[:3])
# lst = list(cities)
# lst.append('Navoiy')
# cities = tuple(lst)
# for city in cities:
#     print(city)
# print(cities[-1])
# new_cities = cities * 2
# print(new_cities)
##4-Masala
# python
# Copy code
# scores = (78, 92, 65, 88, 100)
# print(max(scores))
# print(min(scores))
# print(sum(scores) / len(scores))
# print(92 in scores)
# print(len(scores))
# lst = list(scores)
# lst.append(85)
# scores = tuple(lst)
# for s in scores:
#     if s > 80:
#         print(s)
# print(scores[2])
# print(scores)
##5-Masala
# python
# Copy code
# movies = ('Titanic', 'Avatar', 'Inception', 'Joker')
# print('Avatar' in movies)
# print('Matrix' not in movies)
# print(len(movies))
# print(movies.index('Joker'))
# lst = list(movies)
# lst.append('Matrix')
# movies = tuple(lst)
# print(movies[1:4])
# movies2 = movies * 2
# for m in movies2:
#     print(m)
# print(movies2)
##6-Masala
# python
# Copy code
# menu = ('osh', "lag'mon", 'shashlik', 'somsa')
# print('somsa' in menu)
# print('manti' not in menu)
# print(len(menu))
# print(menu.index("lag'mon"))
# lst = list(menu)
# lst.append('manti')
# lst.remove('osh')
# menu = tuple(lst)
# print(menu * 2)
# print(menu[0:3])
# print(menu)
##7-Masala
# python
# Copy code
# genres = ('pop', 'rap', 'rock', 'jazz', 'classic')
# print(genres.index('rock'))
# print('blues' not in genres)
# print(len(genres))
# lst = list(genres)
# lst.append('blues')
# lst.append('electro')
# genres = tuple(lst)
# print(sorted(genres))
# print(genres[2])
# print(genres * 3)
# print(genres)
##8-Masala
# python
# Copy code
# phones = ('iPhone', 'Samsung', 'Nokia', 'Xiaomi', 'Huawei')
# print(phones.index('Samsung'))
# print('LG' in phones)
# print(len(phones)
# lst = list(phones)
# lst.append('Realme')
# lst.remove('Nokia')
# phones = tuple(lst)
# print(phones[1:])
# print(phones * 2)
# for p in phones:
#     print(p)
# print(phones)
##9-Masala: Kitoblar
# python
# Copy code
# books = ('1984', 'Shaytanat', 'Alkimyogar', "O'tkan kunlar")
# print('1984' in books)
# print('Sariq devni minib' not in books)
# print(len(books))
# print(books.index('Shaytanat'))
# lst = list(books)
# lst.append('Sariq devni minib')
# books = tuple(lst)
# print(books[-2:])
# print(books * 3)
# print(books)
##10-Masala
# python
# Copy code
# cars = ('BMW', 'Chevrolet', 'Hyundai', 'Toyota')
# print(cars.index('BMW'))
# print('Kia' not in cars)
# print(len(cars))
# lst = list(cars)
# lst.append('Kia')
# lst.remove('Hyundai')
# cars = tuple(lst)
# print(cars[1:])
# print(cars * 2)
# print(sorted(cars))
# print(cars)
