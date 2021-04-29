import random

raha = random.randint(50,1000)  # генерирование случайной цены товара (денег)

pood_nimi= []                            # создаю списки
pood_hind = []							# создаю списки

tsekk = []							# создаю списки
tsekk_hind = []					# создаю списки

ostsin_nimi = []							# создаю списки
ostsin_hind = []					# создаю списки



def koige_kallim():                # Находится самый дорогой товар по цене
	maks_hind = pood_hind[0]       # Приравнивание максимальной цены к первой цене, чтобы ошибок не было
	m_nimi = []
	m_hind = []
	indeks = 0
	for i in pood_hind:
		if maks_hind < i:
			maks_hind = i
	for i in pood_hind:
		if maks_hind == i:
			m_nimi.append(pood_nimi[indeks])
			m_hind.append(pood_hind[indeks])
		indeks += 1
	return m_nimi, m_hind

def ostma():
	n = int(input("Введите код товара "))
	tsekk.append(pood_nimi.pop(n))
	tsekk_hind.append(pood_hind.pop(n))

def fill():                           # Заполнить списки товарами
	a = int(input("Сколько товаров вы хотите заполнить? \n[1 kuni 10]:"))
	for b in range(a):
		r = random.randint(0,10)                                           # Вызывание рандома, чтобы перед каждым запуском программы появлись именно эти товары, но в разброс
		if r == 0:                                           
			pood_nimi.append("GeForce RTX 3080 Graphics Card")
			pood_hind.append(1200)

		elif r == 1:
			pood_nimi.append("Intel Core™ i9-9900K")
			pood_hind.append(700)
		elif r == 2:
			pood_nimi.append("Laptop LENOVO")
			pood_hind.append(450)
		elif r == 3:
			pood_nimi.append("RAM HyperX 2tk 8GB")
			pood_hind.append(116)
		elif r == 4:
			pood_nimi.append("PC Setup for office")
			pood_hind.append(799)
		elif r == 5:
			pood_nimi.append("Mousepad")
			pood_hind.append(15)
		elif r == 6:
			pood_nimi.append("Keyboard")
			pood_hind.append(110)
		elif r == 7:
			pood_nimi.append("Headphones")
			pood_hind.append(85)
		elif r == 8:
			pood_nimi.append("Web-cam")
			pood_hind.append(20)
		elif r == 9:
			pood_nimi.append("Mouse")
			pood_hind.append(80)
		elif r == 10:
			pood_nimi.append("Microphone HyperX")
			pood_hind.append(101)



fill()                               # Вызов функции филл 
print(pood_nimi)
print(pood_hind)
while True:                             # Вызываются функции на экран для того или иного выбора
	print(f"На счету: {raha}")
	print("1 - Lisama tšekkis") # добавить в чек
	print("2 - Vaatama tšekki") # посмотреть чек
	print("3 - Vaatama kõige kallim toote/kaup") # посмотреть самый дорогой товар
	print("4 - Ostma") # купить товары
	print("5 - Vaatama ostetud kauplused") # посмотреть купленные товары
	print("6 - Otsima hind nimi järge") # искать цену по названию 
	a = int(input("Введите комманду "))
	if a == 1:
		n = int(input("Введите номер товара "))
		tsekk.append(pood_nimi.pop(n)) # убираем название с товара и присваиваем к чеку
		tsekk_hind.append(pood_hind.pop(n)) # убираем цену с товара и присваиваем к чеку
		#_________________________________________________________
		#/_\			tsekk_hind.append(pood_hind.pop(n)) Шаг 1
		#\_/		tsekk_hind.append(45) Шаг 2
		#/_\	tsekk_hind = [5,5,5,45] Шаг 3
		#_________________________________________________________
	elif a == 2:
		for i in tsekk:
			print(i)
			
	elif a == 3:
		m_nimi, m_hind = koige_kallim()
		indeks = 0
		while indeks < len(m_nimi):
			print(m_nimi[indeks])
			print(m_hind[indeks])
			indeks += 1
	elif a == 4: # Купить все, что в чеке
		if sum(tsekk_hind) <= raha:
			raha -= sum(tsekk_hind)
			ostsin_nimi.extend(tsekk)
			ostsin_hind.extend(tsekk_hind)
			tsekk.clear()
			tsekk_hind.clear()
	elif a == 5:
		index = 0
		while indeks < len(ostsin_nimi):
			print(ostsin_nimi[indeks])
			print(ostsin_hind[indeks])
			indeks += 1
	elif a == 6:
		n = input("Введите название товара ")
		indeks = pood_nimi.index(n)
		print(pood_hind[indeks])









