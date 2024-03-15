# DODATNO : Python Functions
#           File Operations 
#           Exception handle
#           Iterators and Itertools


#                                                   I. Basic Data Types 
#       1. Text Type: str (string)
#       2. Numeric Types: int, float, complex 
#       3. Sequence Types: list, tuple, range 
#       4. Mapping Type: dict
#       5. Set Type: Set, frozenset
#       6. Boolean Types: bool
#       7. Binary Types: bytes, bytearray, memoryview
#       8. None Type : NoneType

#                                          1. str type (String)
#  0  1   2  3  4  5  6  7  8  9 10
#  H  e   l  l  o  _  W  o  r  l  d
#-10 -11 -9 -8 -7 -6 -5 -4 -3 -2 -1

# String ne moze da se menja "imutable object"
# Moze da se pise i sa '' i sa "" i sa """ """
# String je zapravo spojena lista i svakom elementu se pristupa isto kao listi, pomocu indeksa

x_str1 = "Hello World"
x_str2 = 'Hello World'
x_str3 = """Hello World"""

print(x_str1[0])                # Print prvog elementa
print(x_str1[-1])               # Print poslednjeg elementa
print(x_str1[0:4])              # Print od 1-5 elementa
print(x_str1[::-1])             # dlroW olleH -> obrtanje stringa / obrnut string.
x_str1.lower()                  # Pretvori sve elemente u mala slova
x_str1.upper()                  # Pretvori sve elemente u velika slova
x_str1.strip()                  # Odstrane beline sa leve i desne strane
x_str1.lstrip()                 # Odstrani beline sa leve strane
x_str1.rstrip()                 # Odstrani beline sa desne strane
x_str1.strip('#')               # Odstrani sve karaktere '#' sa leve i desne strane
x_str1.count('l')               # Izbroji kojilo ima slova l
x_str1.find('H')                # Pronadje PRVI 'H' element u stringu
x_str1_1 = x_str1.replace('H','Y')         # Posto je str immutable objekat, ova komanda NECE promeniti postojeci string, nego ce napraviti novu promenljivu sa izmenom!
x_str1_2 = x_str1 + x_str2      # Konkatanacija stringa

# Konvertovanje stringa u Listu: 
# 1. String to List of Strings : "Danas je lep dan" -> ["Danas","je","lep","dan"]
x_temp_string = "Danas je lep dan"
x_temp_list = x_temp_string.split()

# 2. String to List of Charracters : "Lep dan" -> ["L","e","p"," ","d","a","n"]
x_temp_string = "Lep dan"
x_temp_list = list(x_temp_string)

# 3. List of Strings to List of Lists: "Ovo je Pajton" -> [["O","v","o"],["j","e"],["P","a","j","t","o","n"]]
x_temp_string = "Ovo je Pajton"
x_temp = x_temp_string.split()
x_temp_list_of_lists = list(map(list,x_temp))

# 4. CSV to List : "ovo,je,csv" -> ["ovo","je","csv"]
x_temp_string = "ovo,je,csv"
x_temp_list = x_temp_string.split(',')

# 5. String of Integers to List of Integers : "1 2 3 4" -> [1,2,3,4]
x_temp_string = "1,2,3,4,5,6"
final = [int(num) for num in  x_temp_string.split(',')]

#Konvertovanje Liste u String
# Iz ["Danas","je","lep","dan"] -> Danas je lep dan
temp = ["Danas", "je", "lep", "dan"]
temp_string = ' '.join(temp)


#                               2. Numeric Types: int, float, complex 
x_int = 20
x_float = 20.5
x_complex = 1j

#                               3. Sequence Types: list, tuple, range 
x_list = [1,2,"Uros", 'C']
x_tuple = (1,2,"Uros", 'C')
x_range = range(6)

#       LISTE                        TUPLES                          SETS                         DICT
#  L = [1,2,3,"Abc"]        |     T = (1,2,3,"Abc")         |    S = {1,2,3,"Abc"}              | D = { "prvi_kljuc":1, "drugi_kljuc":"abc" }
# Skup poredjanih podataka  |  Skup poredjanih podataka     | Skup neporedjanih podataka        | Skup poredjanih podataka po kljucevima
# Nemoraju biti jedinstveni |  Nemoraju biti jedinstveni    | MORAJU biti jedinstveni           | Kljucevi Moraju biti jedinstveni, elementi ne moraju!
#      Mutable              |          IMUTABLE             |           Mutable                 | Mutable, ali KLJUCEVI NISU
# append() -> doda na kraj  |            /                  | add() -> Ubaci na pos. poziciju   | update() 
# pop(3) -> izbaci el.4     |            /                  | pop() -> izbaci RANDOM ELEMENT    | pop() -> kao u listi
# sort() -> sortira         |            /                  |               /                   | sort() -> kao lista

# Liste : 
# Index liste je isti kao kod Stringa, pocinje sa 0 i zavrsava se sa -1
temp_list = [1,2,3,"Uros","123"]
temp_list2 = [4,5,"sest",'7']
temp_list[0]                        # Hvatanje prvog elementa
temp_list[-1]                       # Hvatanje poslednjeg elementa
temp_list[0:4]                      # Hvatanje od prvog do petog elementa
len(temp_list)                      # Prikaz duzine liste -> u ovom slucaju 5
temp_list.append("Banana")          # Dodavanje elementa "Banana" na kraj liste
temp_list.append(3,"Banana")        # Dodavanje elementa "Banana" na 4-tu poziciju liste
temp_list.insert(5,"pet")           # Dodavanje elementa na poziciju
temp_list.extend(temp_list2)        # Dodavanje jedne liste u drugu, tako da senapravi jedna velika lista : [1,2,3,"Uros","123",4,5,"sest",'7']
temp_list.append(temp_list2)        # Apend doda LISTU unutar Liste [1,2,3,"Uros","123",[4,5,"sest",'7']]
temp_list.remove('sest')            # Skine element 'sest'
temp_list.pop()                     # Skine poslednji element
temp_list.reverse()                 # Obrne listu
temp_list.sort()                    # Po difoltu, sortira listu alfabetno / od najmanje ka najvecoj
temp_list.sort(reverse=True)        # Poredja obrnutim redosledom od obicnog sorta
min(temp_list)                      # Prikaz najmanjeg elementa
max(temp_list)                      # Prikaz najveceg elementa
sum(temp_list)                      # Sumiranje liste
temp_list.index('Uros')             # Vrati index na kome se nalazi vrednost

# Matrica / Ugnjezdena lista / Lista lista : 

matra = [
            [1,2,3], 
            ["jedan", "dva", "tri"],
            ["1", "2", "3"],
            ["abc",
                ["123", "Uros"]
            ]
        ]

matra[0]                            # Vraca: [1,2,3]
matra[0][1]                         # Vraca: 1   
matra[3][1][1]                      # Vraca: Uros

# List Comprehention : 
# To je elegantan nacin da se napravi lista. Nema nikakve prednosti performansa, cista stilska stvar!
temp_lista = [1,2,3,4,5]
[num*2 for num in temp_lista]                                    # Duplirati sve vrednosti u listi
[num*2 for num in temp_lista if num % 2 == 0]                    # Duplira samo parne brojeve
[num*2 for num in temp_lista if num % 2 == 0 if num % 5 == 0]    # Duplira one koji su deljivi sa 2 i sa 5



# Tuples : 
# Imutable objekat
temp_tuple = (1,2,3,"cetri", ["pet",6], "abc")
temp_tuple2 = 1,2,3,"cetri", ["pet",6], "abc"   # Takodje primer Tuple, dakle moze da se pravi i sa zagradama i bez njih
temp_tuple[0]                                   # Pristup elementima je identican kao u Listama, u ovom slucaju prikaz '1'
temp_tuple[4][0]                                # Prikaz 'pet'
temp_tuple[0:5]                                 # Sliceing tuple-a isto kao u Listama 
del temp_tuple                                  # Brisanje CELOG tuple
del temp_tuple[0]                               # Brisanje elemenata ne radi
temp_tuple.count('pet')                         # Prebrojavanje elemenata 'pet'
temp_tuple.index('abc')                         # Vracanje indeksa 'abc'


#                               4. Mapping Type: dict
x_dict = {
    "prva":"Uros",
    "druga": "22",
    "treca":[1,2,3,"Cetiri"],
    "cetvrta": 4,
    "peta": 'C',
    "sesta": True
    }
# Kljucevi recnika se ne mogu menjati! 

x_dict["prva"]                                 # Pristupanje elementima recnika se vrsi preko Kljuceva. Moramo imenovati kljuc!
x_dict[0]                                      # Ovo ne radi, jer se ne pristupa elementima vec imenima.
x_dict["treca"][0]                             # Ovo je pristup prvom elementu pod kljucem "treca"
x_dict["prva"] = "Nemanja"                     # Ako kljuc "prva" postoji u recniku, onda ce tom recniku PROMENITI vrednost u "Nemanja", ako kljuc "prva" ne postoji, onda ce napraviti novi kljuc pod tim imenom i dodati mu vrednost "Nemanja"
x_dict.get('peta')                             # Radi kao print(x_dict['peta'])
list(x_dict.keys())                            # Vraca LISTU kljuceva iz recnika x_dict
list(x_dict.values())                          # Vraca LISTU Vrednosti iz recnika x_dict
x_dict.pop('sesta')                            # Ukloni ceo kljuc 'sesta' kao i sve negove elemente
del x_dict['peta']                             # Ukloni ceo kljuc 'sesta' kao i sve negove elemente

# Pretvaranje dict u JSON -> decoding 
# Gotovo da nema razlike izmedju JSON i dict fajlova, imaju identicnu strukturu ali u web projektima se cesto koristi JSON
import json
person = {"name":"Uros", "age":26, "city":"Belgrade", "hasChildren": False, "titles":["engineer", "programer", "artist"]}
person_json = json.dumps(person, indent=4, sort_keys=True)

with open('person.json', 'w') as file:        # Export JSON-a u tekstualni dokument
    json.dump(person, file, indent=4)


#                               5. Set Type: Set, frozenset
x_set = {1,2,3,"cetiri"}
x_frozenset = ({1,2,3,"cetiri"})

# Setovi su tipovi podataka koji nema redosled (nemamo indeksovanje elemenata)
# Podaci moraju biti UNIKATNI
# Setovi u sebi ne mogu da sadrze LISTE
temp_set = {1,2,3,[4,5]}                    # Ovo ne radi jer imamo LISTU unutar seta, a lista je MUTABLE Objekat
x_set.add(5)                                # Dodavanje elemenata u set
x_set.add(1)                                # Ako dodamo element koji vec postoji u setu, nece se NISTA desiti, cak ni eror
x_set.update([5,6,7,8,"devet"])             # Ovako izgleda dodavanje vise elemenata odjednom
x_set.discard(2)                            # Brisanje elementa koji ima vrednost 2
x_set.remove(2)                             # Brisanje elementa koji ima vrednost 2. Razlika izmedju discard i remove je sto ce remove baciti EROR ako element ne postoji u setu
x_set.pop()                                 # brisanje RANDOM elementa iz seta...
x_set | temp_set                            # Uradice UNIJU dva seta, odnosno spajanje
x_set.union(temp_set)                       # Uradice UNIJU dva seta, odnosno spajanje
x_set & temp_set                            # Uradice Razliku dva seta
x_set.intersection(temp_set)                # Uradice Razliku dva seta
x_set - temp_set                            # Vraca sve ono sto se nalazi u x_set u odnosu na temp_set
x_set.difference(temp_set)                  # Vraca sve ono sto se nalazi u x_set u odnosu na temp_set
x_set ^ temp_set                            # Vraca sve sto se nalazi u x_set i u temp_set ALI sto nije u jednom i drugom
x_set.symmetric_difference(temp_set)        # Vraca sve sto se nalazi u x_set i u temp_set ALI sto nije u jednom i drugom
sortirani = sorted(x_set)                   # Ovo vraca sortirani niz ali u obliku LISTE! Sam set se ne sortira!

# Poredjenje setova         Prvo poredi 0-ti element prvog i 0-ti element drugog, pa 1 element prvog i 1 element drugog itd...
(1,2) > (1,3)                               # False
(1,2) < (1,3)                               # True 
(1,2,2) > (1,3)                             # False 
(1,2,2) > (1,2,1)                           # True

#                               6. Boolean Types: bool
x_bool = True 
x_bool = False 
True == 1                                   # True ima numericku vrednost 1
False == 0                                  # False ima numericku vrednost 0
True + (False / True)                       # 1 + (0 / 1) = 1 + 1 = 1.0


#                               7. Binary Types: bytes, bytearray, memoryview
x_bytes = b"Hello"
x_bytearray = bytearray(5)
x_memoryview = memoryview(bytes(5))

#                               8. None Type : NoneType
x_NoneType = None

# ----------------------------------- Conditional Statements in Python ---------------------# 
# if -> elif -> else 
# One line if statement : if <expresion> : <statement>

# Python nema implementiran Switch po difoltu

# Equal : =             ==
# Not Equal :           !=
# Greather than:        >
# Lees than:            <
# Greather or Equal :   >=
# Less or Equal :       <=
# Object identity :     is
# Booleans :            and , or , not

if 'a' in x_list:
    print("a is in x_list")
elif 'a' in temp_list:
    print("a is in temp_list")
else:
    print("a not found :D ")


# ------------------------------------ Looping in Python ----------------------------------# 
# Postoje : for, while i do while
# Petlje trba izbegavati svaki put kad je to moguce, jer su spore. 
# Umesto petlji, uvek treba koristiti built-in funkcije

# For : 
temp_list = ["jedan",2,3,"abc", False]

for i in temp_list:                         # Ispis svakog elementa liste
    pass

for i in range(5):                          # Iteracija ide kao : 0,1,2,3,4 
    pass

for i in range(len(temp_list)):             # Iteracija ide u ovom slucaju kao : 0,1,2,3,4
    pass

for i, val in enumerate(temp_list):         # Enumerate napravi format recnika, sa kljucem i vrednosti
    print(i, ",", val)

# Umesto da koristimo petlju kojom bi smo pomnozili svaki element liste : 
lista_brojeva = [1,2,3,4,5]
rezultat = 0
for broj in lista_brojeva:
    rezultat += broj

# Mnogo je bolje da koristimo ugradjene funkcije koje rade isti posao, npr: 
rezultat = sum(lista_brojeva)

# Ako imamo 2 liste, kroz koje trebamo da prodjemo petljom, mozemo da koristimo zip funkciju: 
l1 = [1,2,3]
l2 = ['a','b','c']

for val1, val2 in zip(l1,l2):               # U slucaju da je jedna lista duza od druge, zip ce prikazati samo elemente koji jednake duzine obe liste
    print(val1, val2)

# While : 
x=0
while x < 10:                               # Petlja koja ima 10 iteracija
    x+=1

while True:                                 # Petlja koja ima beskonacno iteracija
    print("123")
    break 
# ------------------------------------ Input Operacije ----------------------------------- # 
n, k = map(int,input().split())                 # CodeForces unos
temp_list = list(map(int, input().split()))     # Unos elemenata sa konzole u listu, i konvertovanje istih u brojeve



# ------------------------------------ Bonus gradivo -------------------------------------- # 

                                    # Map funkcija : 
# Map funkcija se koristi kada hocemo da primenimo odredjenu funkciju na vise argumenata. 
# map(funkcija,argument)
lista = [1,2,3,4]

def dupliraj(x):
    return x*2

print(list(map(dupliraj,lista)))

lista_stringova = ["1","2","3"]
lista_intova = list(map(int,lista_stringova))

words = ["Welcome", "to", "Python"]
char_count_in_words = list(map(len,words))

# Primena Mapiranja na vise argumenata: 
prvi_argument = [1,2,3]
drugi_argument = [4,5,6]
duplirani_spojeni = list(map(pow,prvi_argument,drugi_argument))         # Rezultat ovoga je JEDNA lista sa kvadriranim podacima

with_spaces = ["processing ", "  strings", "with   ", " map   "]
stripovani = list(map(str.strip, with_spaces))                          # Odstrani beline svim elementima

                                    # Filter Funkcija : 
# Filter funkcija funkcionise slicno kao Map. Ona primejuje Funkciju nad argumentima i oni cuva samo one argumente koji su prosli "filter"
# filter(funkcija,*argumenti)

brojevi = [-1, -2, 0, 1, 2]
def da_li_je_pozitivan(lista):
    return lista > 0
pozitivni_brojevi = list(filter(da_li_je_pozitivan,brojevi))            # Vraca novu listu sa samo pozitivnim projevima


                                    # Reduce Funkcije : 
# Reduce funkcija primenjuje funkciju i vraca JEDNU vrednost kao rezultat! 
# Reduce funkcija nije standardna u paketu Python 3.0, pa mora da se importuje iz functools
# Sintaksa : reduce((funkcija),*argumenti)
# Radi po principu :  reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5) = 15

import functools
slova = ['s','l','o','v','a']
rec = functools.reduce((lambda x,y: x+y),slova)                         # vraca samo 1 vrednost koja glasi : slova

brojevi = [1,2,3,4]
zbir = functools.reduce((lambda x,y : x+y), brojevi)                    # Vraca sabranu vrednost : 10  

                                    # Lambda Funkcije : 
# Lambda funkcija je nacin da napisemo funkciju u jednom redu. 
# Lambda funkcija je ekvivalent finkciji koja uvek vraca argument (ima return)

def add(x,y):
    return x+y

add2 = lambda x,y : x + y 

# Primer u List Comprehentions : 
sekvenca = [1,2,3,4,5]
duplirana_sekvenca = [(lambda x : x*2)(broj) for broj in sekvenca]



                                    # Walrus Operator : 
# Kako izgleda dodela vrednosti:
# 1. 42 se dodeljuje vrednosti x 
x = 42 

# Kako izgleda dodela u Walrus operatoru: 
# 1. 42 se dodeljuje vrednosti x 
# 2. povratna vrednost 42 
(x:= 42)

# Koristi se kada zelimo da u nekoj duzoj ekspresiji napravimo promenljivu.
# Primer  : 

foods = []
while True:
    food = input("Unesi neku hranu: ")
    if food == 'quit':
        break
    foods.append(food)

# Sad sa koriscenjem Walrus operatora 
foods = []
while food:= input("Unesi neku hranu: ") != 'quit':
    foods.append(food)

 #---------------------  Kako izmeriti vreme izvrsavanja necega : ----------------------------------# 
import time
start_time = time.time()
# ONO STO MERIMO ... 
end_time = time.time()
final_time = end_time - start_time
print(final_time)                #Prikaz vremena...


# ---------------------------------------- IterTools -----------------------------------------------------------#
# itertools moduls je kolekcija koja omogucava upravljanje iteratorima.
# U prevodu, to su tipovi podataka koji se mogu koristiti u petljama.
# najcesci itertool je lista
# product, permutation, combinations, accumulate , groupby, infinite iteratos

from itertools import product, permutations, combinations, accumulate, groupby
a = [1,2]
b = [3,4]
prod = product(a,b)                     
print(list(prod))               # [(1,3), (1,4), (2,3), (2,4)]

prod2 = product(a,b, repeat=2)   
print(list(prod))               # [(1,3,1,3), (1,3,1,4), (1,3,2,3)........]

a2 = [1,2,3]
perm3 = permutations(a)
print(list(perm3))              # [(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)]

a2 = [1,2,3]
perm4 = permutations(a, 2) # 2 = duzina permutacije
print(list(perm4)) 

a4 = [1,2,3,4]
perm5 = combinations(a)
print(list(perm5))              # [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]


a5 = [1,2,3,4]
perm6 = accumulate(a)
print(list(perm6))              # [1,3,6,10]  -> po principu: [prvi je uvek isti, 1+2, 3+3, 6+4]


# ---------------------------------------- Error and Exceptions  -----------------------------------------------------------#
# raise error se koristi kada zelimo da genericnu error poruku personalizujemo, tako da znamo gde smo pogresili.
# try / except, radi kao u svakom drugom jeziku, veoma jednostavno
# Takodje mozemo sami da pravimo nase custom greske
# a = 5 + '10'                  # TypeError. Ne mozemo da spajamo int i str
# b = c                         # NameError. Ime c ne postoji
# f = open('example.txt')       # FileNotFoundError. Ne postoji file sa takvim imenom
# a = [1,2,3]... a.remove(4)    # ValueError. 4 se ne nalazi u listi 
# a[4]                          # IndexError. Index 4 ne postoji u listi a
# my_dict = {'name':'Max'}
# my_dict['age']                # KeyError. Ne postoji kljuc pod imenom 'age'

x = -5
if x < 0:
    raise Exception("X treba da je pozitivan") 

# Svaki put kada radimo try except, dobra praksa je da navedemo kakavu gresku ocekujemo.


try:
    a = 5/0
except ZeroDivisionError:
    print("Greska deljenja sa nulom")
except TypeError:
    print("Greska spajanja razlicitih tipova podataka")
else:
    print("Sve je proslo uredu.")
finally: 
    print("Ovo ce se uvek pokrenuti, bez obzira na ishod prethodnih uslova")

class ValueTooHightError(Exception):
    pass

def test_value(x):
    if x > 100:
        raise ValueTooHightError("Uneta vrednost je previse velika")


try:
    test_value(200)
except ValueTooHightError as e:
    print("Doslo je do greske")
    print(e)



