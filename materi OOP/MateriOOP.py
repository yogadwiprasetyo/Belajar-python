# ####################################### START OOP PYTHON ###################################
# ##########################################################################
# # MEMBUAT CLASS DI PYTHON
# # class = template untuk sebuah object
# # nama class harus berawalan kapital, untuk membedakan dari nama variabel
# # Object.__dict__ = melihat attribute pada object

# # membuat class
# class Cars:
#     pass


# # membuat object baru atau inisialisasi objek
# mobil1 = Mobil()
# mobil1 = Mobil()
# ##########################################################################
# # CONSTRUCTOR
# # constructor adalah fungsi di dalam sebuah class
# # constructor dijalankan ketika dipanggil

# # membuat class
# class Mahasiswa:
#     # membuat constructor
#     def __init__(self, nameMhs, npmMhs, jurusanMhs):
#         self.name = nameMhs
#         self.npm = npmMhs
#         self.jurusan = jurusanMhs


# # membuat object dan memanggil constructor
# mhs1 = Mahasiswa('Ario', 1901, 'Hukum')
# mhs2 = Mahasiswa('Suni', 1905, 'Pariwisata')

# # melihat attribute pada objek mhs
# print(mhs1.__dict__)
# print(mhs2.__dict__)
# ##########################################################################
# # CLASS & INSTANCE VARIABEL
# # class variabel berbeda dengan instance variabel
# # class variabel dimiliki oleh class, sedangkan instance variabel dimiliki oleh object

# # membuat class
# class Mahasiswa:
#     # membuat class variabel
#     data_namaMhs = []

#     # membuat constructor
#     def __init__(self, nameMhs, npmMhs, jurusanMhs):
#         # membuat instance variabel
#         self.name = nameMhs
#         self.npm = npmMhs
#         self.jurusan = jurusanMhs
#         Mahasiswa.data_namaMhs.append(self.name)


# # membuat object dan memanggil constructor
# mhs1 = Mahasiswa('Ario', 1901, 'Hukum')
# mhs2 = Mahasiswa('Suni', 1905, 'Pariwisata')

# # mengakses class variabel
# print(Mahasiswa.data_namaMhs)
# ##########################################################################
# # METHODS
# # method adalah sebuah fungsi di dalam class
# # method memiliki 3 jenis yaitu method tanpa argumen, dengan argumen, dan dengan nilai return

# # membuat class
# class Mahasiswa:
#     # class variabel
#     jumlah_mhs = 0

#     # membuat constructor
#     def __init__(self, namaMhs, npmMhs, jurusanMhs, alamatMhs):
#         # instance variabel
#         self.name = namaMhs
#         self.npm = npmMhs
#         self.jurusan = jurusanMhs
#         self.alamat = alamatMhs
#         # menghitung jumlah mahasiswa
#         Mahasiswa.jumlah_mhs += 1

#     # membuat method tanpa argumen, atau void function
#     def namaMhs(self):
#         print(self.name)
    
#     # membuat method dengan argumen
#     def alamatBaru(self, alamatBaru):
#         self.alamat = alamatBaru
#         print('Alamat baru anda menjadi', self.alamat)

#     # membuat method dengan nilai return
#     def getNpm(self):
#         return self.npm


# # membuat object dan memanggil constructor
# mhs1 = Mahasiswa('Ario', 1901, 'Hukum', 'Jl.Indah sawarja')
# mhs2 = Mahasiswa('Suni', 1905, 'Pariwisata', 'Jl.Pejaten raya')

# # mengakses semua jenis method
# mhs1.namaMhs()
# mhs2.alamatBaru('Jl.Pondok Indah')
# print(mhs1.getNpm())
# ##########################################################################
# # PRIVATE VARIABEL
# # variabel private = __namaVariabel, untuk merahasiakan data-data sensitiv
# # variabel protected = _namaVariabel, untuk melindungi data-data

# # membuat class
# class Hero:
#     # membuat constructor
#     def __init__(self,name,besar):
#         # instance variabel publik atau default
#         self.nama = name
#         self.besar = besar
#         # membuat instance variabel private
#         self.__rahasia = "secret"
#         # membuat instance variabel protected
#         self._dilindungi = "terlindungi"

# # membuat object
# coba = Hero('Fuin', 50)

# # tes akses variabel private dan protected
# print(coba.__dict__)
# print(coba.__rahasia)
# print(coba._dilindungi)
# ##########################################################################
# # ENCAPSULASI
# # encapsulasi = untuk menjaga variabel agar tidak dirubah dari luar
# # encapsulasi mempunyai peraturan = membuat semua variabel menjadi private dan menggunakan get & set 

# # membuat class
# class Hero:
#     # membuat constructor
#     def __init__(self, nameHero,HealthHero,attackPowerHero):
#         # instance variabel private
#         self.__name = nameHero
#         self.__health = HealthHero
#         self.__attPower = attackPowerHero
    
#     # membuat method get
#     # method name
#     def getName(self):
#         return self.__name
#     # method health
#     def getHealth(self):
#         return self.__health
    
#     # membuat method set
#     # set health
#     def diserang(self, power):
#         self.__health -= power
#     # set attackPower
#     def attackPower(self, newPower):
#         self.__attPower = newPower


# # membuat object
# # awal dari game
# support = Hero('Support',50,5)
# marksman = Hero('Marksman',50,15)

# # game berjalan
# print(support.getName())
# print(support.getHealth())
# support.diserang(15)
# print(support.getHealth())
# ##########################################################################
# # STATICMETHOD & CLASSMETHOD
# # static method = method yang bisa dipakai oleh class dan objek

# # membuat class
# class Hero:
#     # private class variabel
#     __jumlah = 0

#     # membuat constructor
#     def __init__(self, nameHero):
#         # instance variabel private
#         self.__name = nameHero
#         # menambahkan private class variabel, jika hero baru dibuat
#         Hero.__jumlah += 1

#     # method yang hanya bisa dipakai oleh objek
#     def getJumlahObj(self):
#         return Hero.__jumlah

#     # method yang hanya bisa dipakai oleh class
#     def getJumlahCls():
#         return Hero.__jumlah
    
#     # method static(decorator), tidak membutuhkan argumen dan bisa dipakai oleh objek dan class
#     @staticmethod
#     def getJumlahBoth():
#         return Hero.__jumlah

#     # method class, membutuhkan argumen dan bisa dipakai oleh objek dan class
#     # berfungsi ketika menggunakan inheritance
#     @classmethod
#     def getJumlahBothArg(cls):
#         return cls.__jumlah


# # membuat objek
# assasin = Hero('Assasin')
# fighter = Hero('Fighter')

# print(assasin.getJumlahObj())
# print(Hero.getJumlahCls())
# print(fighter.getJumlahBoth())
# print(Hero.getJumlahBothArg())
# ##########################################################################
# # GETTER & SETTER DECORATOR PYTHON
# # @property = untuk mengubah method menjadi sebuah variabel

# # membuat class
# class Hero:
#     # membuat constructor
#     def __init__(self, nameHero, healthHero, defenceHero):
#         # instance variabel private
#         self.__name = nameHero
#         self.__health = healthHero
#         self.__defence = defenceHero
#         # instance variabel
#         #self.info = 'name: {} \n health: {}'.format(self.__name, self.__health)
    
#     # membuat method property
#     @property
#     def info(self):
#         return 'name: {} \n health: {}'.format(self.__name, self.__health)
    
#     # membuat method property untuk mengakses variabel __defence
#     @property
#     def defence(self):
#         pass

#     # membuat method getter decorator untuk variabel __defence 
#     @defence.getter
#     def defence(self):
#         return self.__defence
    
#     # membuat method setter decorator untuk variabel __defence
#     @defence.setter
#     def defence(self, newDefence):
#         self.__defence = newDefence

#     # membuat method deleter decorator untuk variabel __defence
#     @defence.deleter
#     def defence(self):
#         self.__defence = None


# # membuat objek
# marksman = Hero('Marksman',100,20)
# support = Hero('Support',100,40)

# # akses
# # mengakses method info yang menjadi sebuah variabel
# print(support.info)
# # mengakses method getter defence yang menjadi sebuah variabel
# print(marksman.defence)
# # mengakses method setter defence yang menjadi sebuah variabel
# marksman.defence = 50
# # mengakses method getter defence yang menjadi sebuah variabel
# print(marksman.defence)
# # mengakses method deleter defence yang menjadi sebuah variabel
# del marksman.defence
# # melihat attribute yang terdapat di objek
# print(marksman.__dict__)
# ##########################################################################
# # PENDAHULUAN INHERITANCE
# # inheritance adalah mewariskan class dari class utama
# # class utama = superclass, class yang diwarisi = subclass

# # membuat class utama(superclass)
# class Animal:
#     # membuat constructor
#     def __init__(self, nama, warna):
#         self.nama = nama 
#         self.warna = warna

# # membuat class yang diwarisi(subclass)
# class AnimalDarat(Animal):
#     pass

# # membuat class yang diwarisi(subclass)
# class AnimalLaut(Animal):
#     pass


# # membuat objek class utama(superclass)
# ular = Animal('ular','hijau')
# # membuat objek class yang diwarisi(subclass)
# kucing = AnimalDarat('kucing', 'orange')
# # membuat objek class yang diwarisi(subclass)
# ikan = AnimalLaut('ikan paus','hitam-putih')

# print(ular.nama)
# print(kucing.nama)
# print(ikan.nama)
# ##########################################################################
# # SUPER
# # super() = mengambil constructor,method,attribute dari superclass

# # membuat class utama(superclass)
# class Laptop:
#     # membuat constructor
#     def __init__(self, jenisLaptop, warnaLaptop, hargaLaptop):
#         self.jenis = jenisLaptop
#         self.warna = warnaLaptop
#         self.harga = hargaLaptop

#     # membuat method menampilkan info laptop
#     def info(self, laptop):
#         print('\t{}\njenis: {}\nwarna: {}\nharga: {}'.format(laptop,self.jenis,self.warna,self.harga))

# # membuat class yang diwarisi(subclass)
# class LaptopGaming(Laptop):
#     # membuat constructor dari class subclass
#     def __init__(self, jenis, warna, harga):
#         # menggunakan super(), untuk mengambil constructor dari superclass
#         super().__init__(jenis,warna,harga)
#         # menggunakan super(), untuk mengambil method dari superclass
#         super().info('LAPTOP FOR GAMING')

# # membuat class yang diwarisi(subclass)
# class LaptopOffice(Laptop):
#     # membuat constructor dari class subclass
#     def __init__(self, jenis, warna, harga):
#         # menggunakan super(), untuk mengambil constructor dari superclass
#         super().__init__(jenis,warna,harga)
#         # menggunakan super(), untuk mengambil method dari superclass
#         super().info('LAPTOP FOR OFFICE')


# # membuat objek 
# # objek laptop gaming
# asus = LaptopGaming('Asus ROG', 'hitam-merah', 'Rp.15,000,000')
# hp = LaptopGaming('HP Pavilion', 'hitam-hijau', 'Rp.10,000,000')
# lenovo = LaptopGaming('Lenovo Legion', 'hitam-merah', 'Rp.11,000,000')
# # objek laptop office
# macbook = LaptopOffice('Macbook Pro', 'putih-silver', 'Rp.18,000,000')
# dell = LaptopOffice('Dell Inspiron', 'hitam-putih', 'Rp.6,000,000')
# acer = LaptopOffice('Acer Aspire', 'full-hitam', 'Rp.6,000,000')
# ##########################################################################
# OVERRIDE METHOD
# override method = untuk menimpa method yang ada di superclass, jika sama.
# ##########################################################################
# # MULTIPLE INHERITANCE
# # multiple inheritance = untuk mendapatkan warisan dari apa yang ada di beberapa class 

# # membuat class yang mewarisi(superclass)
# class TeamPemain():
#     # membuat method team
#     def setTeam(self, team):
#         self.team = team
#     # membuat info team
#     def infoTeam(self):
#         print(self.name, 'berada di team', self.team)

# # membuat class yang mewarisi(superclass)
# class PosisiPemain():
#     # membuat method set posisi
#     def setPosisi(self, posisi):
#         self.posisi = posisi
#     # membuat method info posisi
#     def infoPosisi(self):
#         print(self.name, 'berada di posisi', self.posisi)

# # membuat class yang diwarisi(subclass)
# class PemainBola(TeamPemain,PosisiPemain):
#     # membuat constructor
#     def __init__(self, namaPemain, posisiPemain, teamPemain):
#         #instance variabel
#         self.name = namaPemain
#         # menggunakan super(), untuk memanggil method dari subclass
#         super().setPosisi(posisiPemain)        
#         # menggunakan super(), untuk memanggil method dari subclass
#         super().setTeam(teamPemain)
    
#     # membuat method info full pemain
#     def infoPemain(self):
#         print('{} \n\tPosisi: {}\n\tTeam: {}'.format(self.name,self.posisi,self.team))


# # membuat objek
# supriadi = PemainBola('Supriadi', 'Sayap', 'Persebaya')
# supriadi.infoPemain()
# supriadi.setTeam('Liverpool')
# supriadi.infoPemain()
# ##########################################################################
# # METHOD RESOLUTION ORDER  
# # method resolution order = urutan dari multiple inheritance, jika constructor dan method mempunyai nama yang sama
# # method resolution order untuk mengetahui urutan dari sebuah warisan class
# ##########################################################################
# # DIAMOND PROBLEM
# # menyelesaikan multiple inheritance yang berbentuk diamond
# # dengan cara = mengecek class sebelah kiri, tengah dan kanan, jika tidak ada baru ke awal class
# ##########################################################################
# # MAGIC METHOD
# # magic method = keyword method yang ada di python yang bisa kita gunakan

# # membuat class
# class Smartphone:
#     # magic method 1
#     def __init__(self, namaHP, jumlahHP):
#         self.name = namaHP
#         self.jumlah = jumlahHP

#     # magic method 2, digunakan ketika debug
#     def __repr__(self):
#         return self.name

#     # magic method 3, digunakan ketika sudah jadi
#     def __str__(self):
#         return self.name
    
#     # magic method 4, menjumlahkan dua objek
#     def __add__(self, objek2):
#         return self.jumlah + objek2.jumlah


# # membuat objek
# xiaomi = Smartphone('Xiaomi', 5)
# samsung = Smartphone('Samsung', 5)

# # akses repr
# print(repr(xiaomi))
# # akses str
# print(samsung) 
# # akses add
# print(xiaomi + samsung)
# ##########################################################################
# # CLASS ABSTRACT
# # class abstract harus import modul terlebih dahulu
# # abc = abstract base class
# # ABC = class, abstractmethod = decorator

# # import modul abc
# from abc import ABC,abstractmethod

# # membuat class abstract
# class MahklukHidup(ABC):

#     # melakukan decorator untuk method agar harus diimplementasikan
#     @abstractmethod
#     def berjalan(self):
#         print('sedang berjalan')

# # membuat class untuk implementasi dari class abstract
# class Manusia(MahklukHidup):
#     # mengimplementasi method yang ada di class abstract
#     def berjalan(self):
#         print('sedang berjalan')

# # membuat class untuk implementasi dari class abstract
# class Binatang(MahklukHidup):

#     # mengimplementasi method yang ada di class abstract
#     def berjalan(self):
#         print('sedang berjalan')


# # membuat objek
# man = Manusia()
# # akses method dari abstract class
# man.berjalan()
# ##########################################################################
# ####################################### FINISH OOP PYTHON ###################################