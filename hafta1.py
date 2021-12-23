# %% """ Bir metnin uzunluğunu hesaplamak için bir Python programı yazınız. ipucu Len fonksiyonu """

print(len(input("Please enter the text: "))) # bu satırda kullanıcıdan girdiyi input komutuyla aldım 
# daha sonra len komutuyla boyunu öğrenip printle bastırdım

# %%  """Kullanıcı tarafından girilen bir metnin ilk iki ve son iki karakterini ekrana yazdıran Python programını yazınız."""
text =''
flag = True # Kontroller için flag oluşturdum
text = input("Please enter same word(s), shuold be longer then 2 letter: ") # yazılan kelimeyi burada alınıyor
if not(len(text) >= 2): #Girilen input istenilen uzunluktamı kontrol edildiği yer
    print("Please enter more longer entry! ") #değilse hata mesaj yazılıyor
    while flag: # input istenilen uzunlukta olana kadar bu döngüde 
            text = input("Please enter same word(s), shuold be longer then 2 letter: ")
            if len(text) >= 2: 
                flag = False
            else:
                print("Please enter more longer entry! ")

print("First two letters: ",text[0:2]) # ilk iki kelime ekrana bastırılıyor
print("Last two letters: ",text[-1:-3:-1]) #son ili kelime ekrana bastırlıyor

# %% """Kullanıcıdan değişecek metin ve eski harf ve yeni harf bilgisini alarak girilen metin üzerinden
#  değişikliği yapıp sonucu ekrana yazdıran Python programını yazınız."""

text = input("Please enter the text you want changed: ") # text alınıyor
old_letter = input("Please enter the old letter: ") # değişmesi istenilen harf
new_letter = input("Please enter the new letter: ") # değiştirlmek istenilen harf
print(text.replace(old_letter,new_letter)) # iki harf replace fonsiyonuyla yer değişiyor
#%% """Kullanıcı tarafından girilen bir kelimenin palindrom olup olmadığını karşılaştırma operatöründen faydalanarak 
# print() fonksiyonu ile ekrana yazdırınız. """

palin = input("Please enter the text: ") # Textin alındığı kısım
drom = palin[::-1] # Text burada ters çeviriliyor

if palin == drom: # ikisinin aynı olup olmadığının kontrol edildiği kısım
    print("Yes this word palindrom.") # aynıysa çıktı
else:
    print("Sorry it is not palindrom :(") # farklıysa çıktı

# %% Girilen bir metnin son 2 karakterini 4 defa çoğaltarak ekrana yazan Python programını yazınız. * aritmetik operatöründen faydalanabilirsiniz.

text = input("Please enter the text: ") #Textin alındığı kısım
print("Last two letters: ",text," -->",text[-2:]*4) #kelime ve son iki harf 4 kere ekrana bastırlıyor

# %% """ 5 elemanlı bir liste oluşturunuz. 
# Bu liste içerisindeki 2. elemanı 100 ile değiştiren python kodu yazınız. """

from string import ascii_lowercase,ascii_uppercase,punctuation,digits #rasgele bir liste oluşturmak için import edilen kütüphaneler
import random as rnd # rasgele seçim yapılması için eklenen random kütüphanesi
lst_5=[] # 5lik lisemiz daha boş
lst = [ascii_lowercase,ascii_uppercase,punctuation,digits] # kullanılacak herşey burada
for _ in range(5): # rasgele seçim yapan döngümüz 
            lst_5.append(rnd.choice(rnd.choice(lst))) #listemize elemanların eklendiği satır
print(lst_5) # listenin ilk hali
lst_5[1]=100 # ikinci elemen değiştiriliyor
print(lst_5) # listenin son hali


# %% İki farklı listede tutulan verileri tek bir listede sırasıyla append,extend metodlarıyla ve "+" operatörü ile birleştiren python kodunu yazınız 
# liste1 = [1,2,3] liste2 = [4,5,6] liste3 = ????? """

#listeleri tanımlıyoruz
liste1 = [1,2,3] 
liste2 = [4,5,6] 
liste3 =[]

#append özelliğinin kulanıldığı yer
liste3.append(liste1)
liste3.append(liste2)
print(liste3,"--> append")
liste3 =[]

#extend özelliğinin kulanıldığı yer
liste3.extend(liste1)
liste3.extend(liste2)
print(liste3,"--> extend")
liste3 =[]

# '+' operatörünün kulanıldığı yer
liste3 = liste1+liste2
print(liste3,"--> '+' ")

# %% Oluşturduğunuz 3 elemanlı bir liste içerisine ilk sıraya "Elma" kelimesini ekleyiniz.

from string import ascii_lowercase,ascii_uppercase,punctuation,digits #rasgele bir liste oluşturmak için import edilen kütüphaneler
import random as rnd # rasgele seçim yapılması için eklenen random kütüphanesi
lst_3=[] # 5lik lisemiz daha boş
lst = [ascii_lowercase,ascii_uppercase,punctuation,digits] # kullanılacak herşey burada
for _ in range(3): # rasgele seçim yapan döngümüz 
            lst_3.append(rnd.choice(rnd.choice(lst))) #listemize elemanların eklendiği satır
print(lst_3) # listenin ilk hali
lst_3.insert(0,'Elma')
print(lst_3) # listenin son hali
# %% """liste = [1,2,3,4,5,6,7,1,3,3,3,2,2,1,23] yukarıdaki listeden ilk 3 sayısını silip ekrana yazdırınız. """

liste = [1,2,3,4,5,6,7,1,3,3,3,2,2,1,23]
liste.remove(3) #karşılaştığı ilk üçü çıkarır
print(liste) # yeniden bastırma

# %% """ liste1 = ["1",1,2,"3"] Yukarıdaki listenin bir kopyasını alarak 250 sayısını listenin sonuna ekleyiniz,her iki listeyi ekrana yazdırınız. 
# Beklenen Çıktı: ["1",1,2,"3"] => Liste1 Çıktısı ["1",1,2,"3",250] => Liste2 Çıktısı """

lst1 = ["1",1,2,"3"] #listeler defineedildi
lst2 = []
lst2 = lst1.copy() #birinci liste ikinciye kopyalandı
lst1.append(250) #sonuna 250 eklendi
print(lst1)
print(lst2)

# %% Aşağıdaki üç farklı sözlüğü tek sözlükte birleştiren python kodunu yazınız dict1={1:10, 2:20} dict2={3:30, 4:40} dict3={5:50,6:60}
#  Beklenen Çıktı : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} """

#dict tanımlamaları
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}
dict4={}

#birleştirmek için forlar kullandım
for key, value in dict1.items():
    dict4[key] = value
for key, value in dict2.items():
    dict4[key] = value
for key, value in dict3.items():
    dict4[key] = value
#bastırma
print(dict4)


# %% sozluk ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} Sözlükteki en son elemanı silerek ekrana işlem sonucunu yazdırınız Beklenen Çıktı :(6,60) 

sozluk ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(sozluk.popitem()) # son elemanı çıkarıyor

# %% """dict1={1:10, 2:20} Yukarıdaki sözlüğe bir eleman ekleyiniz. Beklenen Çıktı :{1:10, 2:20, 3:30} """

dict1={1:10, 2:20}
dict1.update({3: 30}) #updatele yeni ele
print(dict1)

# %% liste=[1,2,3,4,5] a.Yukarıdaki listeden faydalanarak bir sözlük oluşturun 
# b.sözlüğün her alamanının karşılığına değer olarak anahtarda bulunan sayısal değerin 10 katını eşitleyin. 
# Beklenen Çıktı : a. {1:0,2:0,3:0,4:0,5:0} b. {1:10,2:20,3:30,4:40,5:50} """

# gerekli tanımlamalar
liste=[1,2,3,4,5]
a={}
b={}

# ilk dict oluşturma
for key in liste:
    a[key] = 0

# ikinci dict oluşturma
for  key in liste:
    b[key] = key*10

#çıktılar
print(a)
print(b)


# %% sozluk={1:10,2:20,3:30,4:40,5:50} Sözlük içerisine 6 sayısını anahtar olarak değeri 60 olacak şekilde setdefault fonksiyonunu kullanarak ekleyiniz

sozluk={1:10,2:20,3:30,4:40,5:50}

def setdefault(sozluk, key , value):
    sozluk.update({key: value})
    return sozluk

print(setdefault(sozluk, 6 , 60))

# %%
digit = int(input("Please enter digit"))
if digit == 0:
        print("""
                 *******
                 *     *
                 *     *
                 *     *
                 *     *
                 *     *
                 *******""")
elif digit == 1:
        print("""
                 *
                 *
                 *
                 *
                 *
                 *
                 *""")
elif digit == 2:
        print("""
                 *******
                       *
                       *
                 *******
                 *
                 *     
                 *******""")
elif digit == 3:
        print("""
                 *******
                       *
                       *
                 *******
                        *
                        * 
                 *******""")
elif digit == 4:
    print("""
                 *     *
                 *     *
                 *     *
                 *******
                       *
                       *
                       *     
                 """)
elif digit == 5:
    print("""
                 *******
                 *
                 *
                 *******
                       *
                       *     
                 *******""")
elif digit == 6:
    print("""
                 *******
                 *
                 *
                 *******
                 *     *
                 *     *
                 *******""")
elif digit == 7:
    print("""
                 *******
                       *
                       *
                       *
                       *
                       *     
                       *""")
elif digit == 8:
    print("""
                 *******
                 *     *
                 *     *
                 *******
                 *     *
                 *     *
                 *******""")
elif digit == 9:
    print("""
                 *******
                 *     *
                 *     *
                 *******
                       *
                       *
                 *******""")

# %% Bir listeyi bir sözlükte sıralamak için bir Python programı yazın 
# Örnek Veri: num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]} """

x = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
{k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
print(x)

# %%

# %% Bir listeyi bir sözlükte sıralamak için bir Python programı yazın 
# Örnek Veri: num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]} """

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}

num = {x : sorted(num[x]) for x in num.keys()} # oneline forda sort ettirme
print(num)

# %% """sozluk = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']} 
# ilgili sözlükten anahtar kısımlarında bulunan boşlukları temizleyen python kodu yazınız. """
sozluk2={}
x_new=''
sozluk = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}
for x in sozluk.keys():
    x_new=x.replace(' ','')
    sozluk2.update({x_new: sozluk[x]})
print(sozluk2)

# %% liste1=[1,2,3] liste2=[4,5,6,7,8] iki listeyi liste3 ile birleştiriniz? 

liste1=[1,2,3] 
liste2=[4,5,6,7,8]
liste3=[10,11,12,13,14,15]
liste4 = liste1 +liste2+ liste3

print(liste4)
# %%  """liste=[1,2,3,4,5,6] listesindeki 1. elemanı del komutu ile siliniz?

liste=[1,2,3,4,5,6]
del liste[0]
print(liste)

# %%  liste=["elma" , "armut", "çilek"] listesine append komutu ile sona 3 elemanını ekleyiniz?

liste=["elma" , "armut", "çilek"]
for i in range(3):
    liste.append(liste[i])
print(liste)

# %% """Girilen on sayı içerisinden en büyük üç sayıyı bulmak için bir Python fonksiyonu yazınız"""

num_arr= [int(input("Please enter number")) for x in range(10)]
num_arr.sort()
print("most bigger number is ", num_arr[-1])
print("second bigger number is ", num_arr[-2])
print("third bigger number is ", num_arr[-3])

# %%"""Bir metin içerisindeki büyük ve küçük harflerin listesini yazdıran python programını yazınız."""

text = input("Please enter the text: ")
small=[]
capital=[]
useless=[]

for i in range(len(text)):
    if text[i].isupper():
        small.append(text[i])
    elif text[i].islower():
        capital.append(text[i])
    else:
        useless.append(text[i])

print("upper case letter numbers is ",len(capital)," and this letters are : " ,small)
print("lower case letter numbers is ",len(small)," and this letters are : " ,capital)
print("not a letter number is ",len(useless)," and this terms are : " ,useless)
# %% """kullanıcıdan alınan 10 sayının çift ve tek sayıların sayısını ekrana yazdıran programı yazınız. """

num_arr= [i for i in range(10)]
even=[]
odd=[]

for i in range(len(num_arr)):
    if num_arr[i] % 2 ==0:
        odd.append(num_arr[i])
    elif not(num_arr[i] % 2 ==0):
        even.append(num_arr[i])

print("There are ",len(odd)," odd numbers and this numbers are : " ,odd)
print("There are ",len(even)," even numbers and this numbers are : " ,even)
