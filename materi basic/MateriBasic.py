# ####################################### START BASIC PYTHON ###################################
# ##########################################################################
# # import library untuk data queue
# from collections import deque

# # import modul untuk cek perbandingan data tuple
# # cek size data
# import sys
# # cek kecepatan olah data
# import timeit

# # import package sains
# import sains as s

# ############################################################################
# # NUMBERS AND MATH
# # // = untuk membulatkan bilangan koma
# # contohnya:
# print(7 // 5)

# # ** = untuk kuadrat bilangan
# # contohnya:
# print(2 ** 5)

# # Operasi Matematika
# a = 4
# b = 3
# c = a + b
# print("pejumlahan 4 + 3 = ", c)
# ############################################################################
# # STRING AND SLICE THEM UP
# # \' \" = escape string untuk kata atau kalimat
# # contohnya:
# text1 = 'i don\'t like you'
# text2 = "siapa mereka? dia menjawab \"teman saya\""
# print(text1)
# print(text2)

# # """ = multiline untuk dialog teks
# # contohnya:
# text3 = """
# yoga: siapa nama kamu?
# tamu: nama saya anonim, ada masalah?
# yoga: tidak.
# """
# print(text3)

# # r = untuk escape kalimat dengan tanda \
# # contohnya:
# text4 = r"C:\nugas"
# print(text4)

# # * = mengulang kata atau kalimat
# # contohnya:
# print(10*"ha")

# # spasi = untuk menggabungkan kata atau kalimat
# # + = untuk menggabungkan kata atau kalimat
# # contohnya:
# print('nama' 'saya')
# print(text1 + text2)

# # [0/-5] = memotong kalimat menggunakan index. awal index 0, jika nilai index minus hitung dari belakang
# # 1:5 = memotong kalimat dari index 1 sampai 5
# # 0:  = memotong kalimat dari index 0 sampai akhir 
# # contohnya:
# text5 = "Yoga Dwi"
# d = text5[4]
# print(d)
# ############################################################################
# # LISTS
# # membuat array list
# Data = [1,3,5,7,9,11]
# Data2 = [2,4,6,8,10]

# # mengakses array list
# # awal index array list adalah 0
# Subdata1 = Data[0]
# print(Subdata1)

# # memotong array list
# Subdata2 = Data[0:3] # memotong array list dari index ke-0 sampai 2, karena index 3 tidak diambil
# Subdata3 = Data[:4] # memotong array awal sampai index ke-3, karena index 4 tidak diambil
# print(Subdata2)
# print(Subdata3)

# # menggabungkan array list
# Data3 = Data + Data2
# print(Data3)

# # merubah salah satu content dari array list
# Data[0] = 0;
# print(Data)

# # mencopy array list ke variabel baru
# e = Data2[:] # tanda : berfungsi untuk menghindari array list awal ikut berubah
# e[0] = 1
# print(e)

# # merubah content array list dengan menggunakan metode slicing(memotong)
# # Data[0:2] = Data[1,3]

# # array list dalam array list
# f = [Data, Data2]
# print(f)

# # mengakses list dalam multidimensial array list
# g = f[0][2]
# print(g)

# # methods untuk array list: append
# Data.append(13)
# print(Data)

# # function yang bisa digunakan array list: len()
# h = len(Data)
# print(h)
# ############################################################################
# # IF ELIF ELSE
# # jenis-jenis logika if = is, ==, is not, in, not in, elif, else
# nilai = 80
# # if nilai == 80: # if sama dengan
# #     print("nilai anda:", nilai)

# # if nilai is 80: # if sama dengan
# #     print("nilai anda:", nilai)

# # if nilai is not 80: # if tidak sama dengan
# #     print("nilai anda:", nilai)

# #if elif else
# if 80 <= nilai <= 100:
#     print("nilai anda A")
# elif 70 <= nilai <= 80:
#     print("nilai anda B")
# elif 60 <= nilai <= 70:
#     print("nilai anda C")
# elif 50 <= nilai <= 60:
#     print("nilai anda D, perbaiki lagi")
# else:
#     print("Anda tidak lulus mata pelajaran ini")

# # operator logika untuk list dan string
# Warkop = ["kopi","bubur","teh manis","indomie","rokok"]
# beli_warkop = "miras"

# if beli_warkop in Warkop:
#     print("penjual bilang, ada")

# if not beli_warkop in Warkop:
#     print("penjual bilang, tidak jual")

# karakter = "a"
# if karakter in beli_warkop:
#     print("ada", karakter)
# ############################################################################
# # FOR LOOP
# # list sebagai iterable
# makanan = ['nasi uduk','nasi padang','nasi goreng','sate ayam','martabak']
# for m in makanan:
#     print(m)
#     print(len(m))

# # string sebagai iterable
# makan = 'nasi'
# for mn in makan:
#     print(mn)

# # for di dalam for (nesting for)
# minuman = ['teh','kopi','susu','jus','jamu']
# konsumsi = [makanan,minuman]

# for data_konsumsi in konsumsi:
#     print(data_konsumsi)
#     for isi_konsumsi in data_konsumsi:
#         print(isi_konsumsi)
# ############################################################################
# # FOR ELSE, RANGE, BREAK
# # else satu sistem dengan for
# # range untuk melakukan perulangan diantara nilai yang ditentukan
# # break untuk mengakhiri sistem for
# number = 20
# for i in range(1,30):
#     print(i)
#     if i is number:
#         print('nilai ditemukan', number)
#         break
# else:
#     print('nilai tidak ditemukan')
# ############################################################################
# # CONTINUE, PASS
# # continue berfungsi untuk melanjutkan ke step berikutnya
# # pass tidak memiliki fungsi apapun atau melewatkan sebuah statement
# for i in range(1,11):
#     if i is 3:
#         # continue
#         pass
#     print(i)
# else:
#     print("akhir dari perulangan")
# ############################################################################
# # WHILE LOOP
# # while loop mempunyai dua jenis yaitu while menggunakan argumen dan while menggunakan boolean
# # while argumen
# nilai = 0
# while nilai < 5:
#     print(nilai)
#     nilai += 1

# # while boolean
# start = True
# angka = 0
# while start:
#     print(angka)
#     if angka is 20:
#         print("nilai ditemukan")
#         start = False
#     angka += 2   

# # while continue, break, pass
# # menggunakan continue di dalam while harus hati-hati
# number = 0
# while number < 10:
#     if number is 5:
#         print("angka ditemukan")
#         # break
#         # continue
#         pass
#     print(number)
#     number += 1
# else:
#     print("nilai akhir number adalah", number)
# ############################################################################
# # FUNCTION
# # mendefinisikan sebuah fungsi
# # membuat fungsi sederhana
# def my_fungsi():
#     print("INI ADALAH FUNGSI")

# # memanggil fungsi 
# my_fungsi()

# # memanggil fungsi di dalam fungsi
# def test_fungsi():
#     my_fungsi()
#     print("ini adalah fungsi ke dua")

# test_fungsi()

# # membuaat fungsi dengan input argumen
# def rata_rata_nilai(n1,n2):
#     tn = n1 + n2
#     rrn = tn/2
#     print("total nilai adalah", tn, "dengan rata-rata nilai", rrn)

# rata_rata_nilai(79,85)
# ############################################################################
# # FUNCTION & ARGUMENTS
# # fungsi dengan keywords argumen
# def mahasiswa(nama,nim):
#     print("nama mahasiswa:", nama)
#     print("nim mahasiswa:", nim)
# # memudahkan untuk memberi nilai pada argumen
# mahasiswa(nama="yoga", nim=6017)
# mahasiswa(nim=6001, nama="andi")

# # fungsi dengan default argumen
# def dosen(nama, sifat="galak"):
#     print("nama dosen:", nama)
#     print("sifat dosen:", sifat)

# dosen("Yunan")
# dosen("Arie", sifat="baik")
# ############################################################################
# # FUNCTION RETURN VALUE
# # fungsi dengan return value
# def kuadrat(n_satu):
#     return n_satu ** 2

# # return value dan multiple argumen
# def rataRata(n_satu, n_dua, n_tiga):
#     total = n_satu + n_dua + n_tiga
#     return total / 3

# i = kuadrat(9)
# j = rataRata(80,90,100)
# k = rataRata(i, 85, 90)
# print(i)
# print(j)
# print(k)
# ############################################################################
# # LAMBDA FUNCTION
# # membuat anonymus function dengan Lambda
# kuadrat_nilai = lambda x: x**2
# hasil_kuadrat = kuadrat_nilai(5)
# print(hasil_kuadrat)
# ############################################################################
# # SCOPE GLOBAL AND LOCAL VARIABEL
# # scope variabel local
# nama_mobil = "avanza"

# def ganti_mobil(nama):
#     nama_mobil = nama
#     print("mobil baru saya:", nama_mobil)

# print(nama_mobil)
# ganti_mobil("Xenia") 
# print(nama_mobil)

# # scope variabel global
# # variabel ini diawali dengan keyword global
# nama_motor = "Vario"

# def ganti_motor(nama):
#     global nama_motor
#     nama_motor = nama
#     print("setelah ganti motor, motor saya:", nama_motor)

# print(nama_motor)
# ganti_motor("Beat")
# print(nama_motor)
# ############################################################################
# # MORE ON ARRAY LIST
# Elektronik = ['komputer', 'smartphone', 'monitor', 'televisi']
# print(Elektronik)
# # method untuk memanipulasi array list
# # method menambah
# # append() = untuk menambah elemen list diakhir
# Elektronik.append('smartwatch')
# print(Elektronik)
# # extend() = untuk menambah elemen list secara tiap-tiap elemen yang dimasukkan
# Elektronik.extend('radio')
# print(Elektronik)
# # insert(index,value) = untuk menambah elemen list secara menentukan posisi
# Elektronik.insert(2,'komputer')
# print(Elektronik)

# # method menghitung
# # count() = untuk menghitung elemen pada array list
# l = Elektronik.count('televisi')
# print(l, "elemen")

# # method menghapus
# # remove() = untuk menghapus elemen, jika elemen lebih dari satu maka yang dihapus adalah elemen pertama yang ditemukan
# Elektronik.remove('komputer')
# print(Elektronik)

# # method salin
# # copy() = untuk menyalin semua elemen pada array list
# NewElektronik = Elektronik.copy()
# NewElektronik.append('kipas')
# print(NewElektronik)
# print(Elektronik)
# ############################################################################
# # STACK AND QUEUES
# # stack = data tumpukan, dengan mengeluarkan data di akhir
# data_tumpukan = [1,2,3,4,5]
# print("data awal:" ,data_tumpukan)

# # memasukkan data baru = append()
# data_tumpukan.append(6)
# print("data ditambah:", 6)
# print("data sekarang:", data_tumpukan)
# data_tumpukan.append(7)
# print("data ditambah:", 7)
# print("data sekarang:", data_tumpukan)
# data_tumpukan.append(8)
# print("data ditambah:", 8)
# print("data sekarang:", data_tumpukan)

# # mengeluarkan data tumpukan = pop()
# data_tumpukan.pop()
# print("data dikeluarkan:", 8)
# print("data sekarang:", data_tumpukan)
# data_tumpukan.pop()
# print("data dikeluarkan:", 7)
# print("data sekarang:", data_tumpukan)
# data_tumpukan.pop()
# print("data dikeluarkan:", 6)
# print("data sekarang:", data_tumpukan)

# # queue = data antrian, dengan mengeluarkan data di awal
# # queue harus memanggil sebuah library = (from collections import deque)
# # membuat queue menggunakan keywords deque([data])
# data_antrian = deque([6,7,8,9,10])
# print("data awal:", data_antrian)

# # menambahkan data antrian = append()
# data_antrian.append(11)
# print("data masuk:", 11)
# print("data sekarang:", data_antrian)
# data_antrian.append(12)
# print("data masuk:", 12)
# print("data sekarang:", data_antrian)
# data_antrian.append(13)
# print("data masuk:", 13)
# print("data sekarang:", data_antrian)

# # mengurangi data antrian = popleft()
# data_antrian.popleft()
# print("data keluar:", 6)
# print("data sekarang:", data_antrian)
# data_antrian.popleft()
# print("data keluar:", 7)
# print("data sekarang:", data_antrian)
# data_antrian.popleft()
# print("data keluar:", 8)
# print("data sekarang:", data_antrian)
# ############################################################################
# # STRUKTUR DATA TUPLE
# # Tuple = data yang tidak bisa dirubah dan ditambah, atau disebut data pasti
# # Tuple sama seperti List, yang membedakannya adalah sifat dari data dan tempat pembuatannya
# # Tuple memiliki size lebih kecil dan lebih cepat dalam mengolah data daripada List
# # membuat data tuple
# data_tuple = (1,2,3,4,5,"siapa","anda?","kenapa dia?!",False,3.14,567.6)
# data_list = [1,2,3,4,5,"siapa","anda?","kenapa dia?!",False,3.14,567.6]

# # cek perbandingan Tuple dan List
# # perbandingan size
# besar_datatuple = sys.getsizeof(data_tuple)
# besar_datalist = sys.getsizeof(data_list)

# print("besar data tuple:", besar_datatuple)
# print("besar data list:", besar_datalist)

# # perbandingan kecepatan olah data
# kecepatan_datatuple = timeit.timeit(stmt="(1,2,3,4,5)", number=100000)
# kecepatan_datalist = timeit.timeit(stmt="(1,2,3,4,5)", number=100000)

# print("kecepatan data tuple:", kecepatan_datatuple)
# print("kecepatan data list :", kecepatan_datalist)
# ###########################################################################
# # STRUKTUR DATA SET
# # Set = data yang tidak mempunyai urutan atau disebut himpunan data
# # Set tidak support indexing, karena tidak mempunyai urutan
# # membuat data set
# # cara ke-1
# kendaraan = {"motor","mobil","bajaj","bis","kereta","pesawat","kapal"}
# transportasi_umum = {"bajaj","bis","kereta","pesawat","kapal"}
# transportasi_pribadi = {"motor","mobil"}
# # cara ke-2
# kendaraan2 = set()
# kendaraan2.add("motor")
# kendaraan2.add("mobil")

# # method menggabungkan data set
# print(transportasi_umum.union(transportasi_pribadi))

# # method untuk merubah data double menjadi satu data
# print(transportasi_umum.intersection(kendaraan))
# ###########################################################################
# # STRUKTUR DATA DICTIONARY
# # Dictionary = data yang mempunyai key and value, atau disebut array asosiatif
# # membuat data dictionary
# mahasiswa_TI = {
#     "Nama":"Yoga",
#     "NPM": 20917,
#     "Jurusan": "Teknik Informatika",
#     "Fakultas": "FTKI"
# }

# mahasiswa_SI = {
#     "Nama":"Anah",
#     "NPM": 19908,
#     "Jurusan": "Sistem Informasi",
#     "Fakultas": "FTKI"
# }

# datamahasiswa_FTKI = {20917:mahasiswa_TI, 19908:mahasiswa_SI}

# # mengakses data dictionary
# print(datamahasiswa_FTKI[20917])

# # memanggil data dengan key
# print(mahasiswa_TI["Nama"])

# # memanggil data hanya key saja
# print(mahasiswa_TI.keys())

# # memanggil data hanya value saja
# print(mahasiswa_TI.values())

# # memanggil data hanya item saja atau keys and values
# print(mahasiswa_TI.items())
# ###########################################################################
# # TEKNIK LOOPING
# # data List
# laptop = ['HP', 'Asus', 'Lenovo', 'Acer', 'Axioo']
# jenis = ['Notebook', 'Vivobook', 'Laptop', 'Notebook', 'Laptop']
# # data Set
# smartphone = {'Xiaomi','Asus','Samsung','Realme','Vivo'}
# # data Dictionary
# jl = {'HP':'Notebook',
#     'Asus':'Vivobook',
#     'Acer':'Laptop'
# }

# # enumerate() = untuk memberi nilai index pada data list
# for index,merk in enumerate(laptop):
#     print(index,':',merk)

# # zip() = menggabungkan dua list dalam satu looping
# for l,j in zip(laptop,jenis):
#     print("laptop", l, "jenis:", j)

# # looping data Set
# # menggunakan method sorted
# for s in sorted(smartphone):
#     print(s)

# # looping data Dictionary
# # memakai method data Dictionary
# for lp in jl.items():
#     print(lp)

# # reversed() = untuk membalikan nilai
# for a in reversed(range(1,11,1)):
#     print(a)
# ##########################################################################
# # IMPORT & MODULE
# # syntax: import namamodul
# # as berfungsi sebagai pengganti namamodul
# # syntax: import namamodul as nm

# # mengakses spesifik modul
# # syntax: from namamodul import statement,statement
# # mengakses semua yang ada di dalam modul
# # syntax: from namamodul *
# # * berfungsi untuk mengambil semua yang ada di modul
# ##########################################################################
# # MEMBUAT PACKAGE
# # membuat __init__.py untuk mengakses semua modul di dalam satu file
# # di dalam __init__.py melakukan = from .namamodul import *
# # . sebagai tempat modul itu berada

# # mengakses fungsi maths
# s.kuadrat(4,4)
# s.modulus(14,8)

# # mengakses fungsi physics
# kecepatan = s.kecepatan(10,5)
# jarak = s.jarak_tempuh(20,5)
# waktu = s.waktu_tempuh(50,30)
# print(kecepatan)
# print(jarak)
# print(waktu)
# #########################################################################
# # MENGGUNAKAN __MAIN__
# # menggunakan __name__ untuk mendeteksi sumber modul
# # __main__ untuk mendeteksi fungsi utama terhadap modul
# ##########################################################################
# # PENGENALAN CLASS
# class mahasiswa():
#     nama = ''
#     nim = ''

# m1 = mahasiswa()
# m2 = mahasiswa()

# m1.nama = 'Yoga'
# m1.nim = 1917

# m2.nama = 'Duya'
# m2.nim = 1907

# print(m1.nama)
# print(m1.nim)

# print(m2.nama)
# print(m2.nim)
# ##########################################################################
# # MEMBUAT METHOD
# # method = fungsi di dalam class
# # self = menunjukan kepemilikan dari object
# # membuat class
# class mahasiswa():
#     nama = ''
#     nim = ''
#     # membuat mehod 
#     def belajar(self):
#         print(self.nama, "sedang belajar")
    
#     def tidur(self):
#         print(self.nama, "sedang tidur")

# m = mahasiswa()
# mh = mahasiswa()
# m.nama = 'siona'
# mh.nama = 'anisa'

# m.belajar()
# mh.tidur()
# ##########################################################################
# # MENGGUNAKAN __INIT__() atau CONSTRUCTOR
# # __init__() = berfungsi untuk mendeklarasikan objek hanya sekali
# # __init__() = dijalanlan ketika menginisialisasi objek
# # membuat class
# class mahasiswa():
#     nama = ''
#     nim = ''
#     # membuat __init__() atau constructor
#     def __init__(self, nama, nim):
#         self.nama = nama
#         self.nim = nim
#         print("DATA MAHASISWA\nnama:", self.nama, "\nnim:", self.nim)

# # memanggil __init__()
# mhs = mahasiswa('Yoga', 1970)
# ##########################################################################
# # PRIVATE ATTRIBUTE 
# # __ berfungsi untuk memprotect attribute di dalam class
# # membuat class
# class mahasiswa():
#     __nilai = 0

#     # membuat __init__() atau constructor
#     def __init__(self, nama, nim):
#         self.nama = nama
#         self.nim = nim
#         print("DATA MAHASISWA\nnama:", self.nama, "\nnim:", self.nim)
    
#     # membuat method
#     def tugas(self, n_tugas1, n_tugas2):
#         self.__nilai = n_tugas1 + n_tugas2
#         #return self.__nilai

#     # membuat method
#     def uts(self, n_uts):
#         self.__nilai += n_uts
#         # return self.__nilai
    
#     # membuat method
#     def uas(self, n_uas):
#         self.__nilai += n_uas
#         #return self.__nilai
    
#     # membuat method
#     def hasil_nilai(self):
#         self.t_nilai = self.__nilai
#         return self.t_nilai / 4
    
#     # membuat method
#     def check_status(self):
#         if self.hasil_nilai() <= 60:
#             print('nama:',self.nama, '\ntotal nilai:', self.t_nilai, 
#             '\nrata-rata nilai:', self.hasil_nilai(), 
#             '\nstatus: tidak lulus')
#         else:
#             print('nama:',self.nama, '\ntotal nilai:', self.t_nilai, 
#             '\nrata-rata nilai:', self.hasil_nilai(), 
#             '\nstatus: lulus')
        
# mhs1 = mahasiswa('yoga', 1917)
# mhs2 = mahasiswa('anisa', 1920)
# ##########################################################################
# # CLASS INHERITANCE 
# # class inheritance = mewariskan class ke class lainnya
# # membuat class
# class Animal:
#     def __init__(self, nama, umur, warna):
#         self.name = nama
#         self.age = umur
#         self.color = warna
#         print(nama, umur, warna)
    
#     def suara(self, input_suara):
#         print(input_suara)

# class Anjing(Animal):
#     pass

# hewan_anjing = Anjing('brown', '2 tahun', 'hitam')
# hewan_anjing.suara('gukgukgukguk')
# ##########################################################################
# # INPUT & OUTPUT FILE .TXT
# # mode file:
# # w = write atau menulis text sebuah file, jika belum ada filenya akan dibuat
# # r = read atau hanya membaca
# # a = appending atau menambahkan text pada file 
# # r+ = write and read, atau membaca dan menulis text di file

# # membuat file txt
# file1 = open("test.txt", 'w')
# file1.write('dibuat menggunakan metode w atau write')
# file1.close()

# # membaca file txt
# file1 = open("test.txt", 'r')
# # cara ke-1
# print(file1.read())
# # cara ke-2
# # print(file1.readline())

# # menambahkan file txt
# file2 = open("test.txt", 'a')
# file2.write("\nteks ini ditambahkan melalui mode appending atau a")
# file2.close()
# ##########################################################################
# EKSTERNAL PACKAGE DENGAN PIP
# syarat = python terinstal, internet, dependency
# cek package terinstall = pip list --format=columns atau pip list
# install package = pip install namapackage

# # package numpy
# import numpy as np
# # menggunakan package numpy
# a = np.array([1,2,3,4,5])
# b = np.array([6,7,8,9,10])
# print(a+b)
# ##########################################################################
# VIRTUAL ENVIRONTMENT & MIGRASI
# venv berfungsi untuk memisahkan lingkungan pengembangan pada folder sendiri

# membuat folder virtual envirotnment
# mac = python3 -m venv namafolder
# windows = python -m venv namafolder

# merubah python di komputer ke folder venv
# mac = source namafolder venv/bin/activate
# windows = namafolder venv\Scripts\activate.bat

# keluar dari folder venv
# deactivate

# migrasi dari folder venv ke folder venv yang lain
# pip freeze --local > namafile.txt

# install package dari namafile.txt
# pip install -r namafile.txt
# ##########################################################################
# # ERROR HANDLING: TRY AND EXCEPTION
# # try and exception

# # type exception error
# # 1. IOError                4. KeyboardInterupted       
# # 2. ImportError            5. Divisionbyzero
# # 3. ValueError             6. EOFError

# # cara handling error
# # 1.menerima/except
# try:
#     a = 4 / 0
# except:
#     print("ada error")

# # 2. mengambil jenis error
# try:
#     a = 3 / 0
# except ZeroDivisionError:
#     print('salah')

# print('selesai')
# ##########################################################################
# ####################################### FINISH BASIC PYTHON ###################################