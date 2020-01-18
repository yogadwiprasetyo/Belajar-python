# PROBLEM SOLVE
# # PROBLEM
# # 1.buatlah algoritma suatu program yang menerima 3 angka A, B, dan C 
# # program kemudian akan menuliskan ketiga angka secara terurut dari yang terkecil ke yang terbesar

# # SOLVE
# # membuat input user
# a = int(input('Masukkan angka pertama: '))
# b = int(input('Masukkan angka kedua: '))
# c = int(input('Masukkan angka ketiga: '))

# # memasukkan input user ke dalam list
# data_angka = {a,b,c}

# # melakukan sorted
# for d in sorted(data_angka):
# 	print(d)
# #######################################################################################################
# # PROBLEM
# # 2.buatlah algoritma untuk kasus berikut : 
# # di dalam Kotak A, terdapat beberapa bola berwarna merah, oranye, kuning, hijau, dan biru
# # jumlah bola di dalam kotak A tidak diketahui, 
# # Andi ingin memilah-milah bola-bola di dalam kotak A sesuai warnanya ke dalam kotak-kotak berwarna merah, oranye, kuning, hijau, dan biru
# # dengan cara mengambil satu-persatu bola dari kotak A 
# # dan memasukkan bola tersebut ke kotak berwana sesuai warna dari bola yang terambil hingga bola di dalam Kotak A habis
# # (tidak perlu memusingkan tipe variabel, tuliskan saja logika algoritmanya)

# # SOLVE
# # membuat list untuk data bola di kotak A
# kotak_A = ['bola merah','bola oranye', 'bola kuning', 'bola hijau', 'bola biru']

# # membuat list, untuk tempat bola yang akan diambil
# kotak_merah = []
# kotak_oranye = []
# kotak_kuning = []
# kotak_hijau = []
# kotak_biru = []

# # melakukan looping untuk memasukkan bola ke tempatnya
# for bw in kotak_A:
# 	# jika warna bola cocok dengan tempat nya maka masukkan bola tersebut
# 	if(bw == 'bola merah'):
# 		kotak_merah.append(bw)
# 	elif(bw == 'bola oranye'):
# 		kotak_oranye.append(bw)
# 	elif(bw == 'bola kuning'):
# 		kotak_kuning.append(bw)
# 	elif(bw == 'bola hijau'):
# 		kotak_hijau.append(bw)
# 	elif(bw == 'bola biru'):
# 		kotak_biru.append(bw)
# else:
# 	print('bola yang ada di dalam kotak A berhasil dipindah dan sudah habis')
# #######################################################################################################
# PROBLEM
# 3. buatlah tipe data bentukan untuk kasus berikut
# tipe Mahasiswa merupakan tipe bentukan yang berisi:
# 	Nama, NIM, Jurusan, Asal, Tanggal_Lahir, IP_semester, Total_SKS
# Jurusan hanya dapat diisi dengan kode Jurusan yang ada di Universitas Telkom
# (tidak perlu semua, pilih 3 saja)
# Tanggal_Lahir merupakan tipe bentukan tgl yang berisi :
# 	Tanggal, Bulan, Tahun
# IP_Semester merupakan tipe bentukan IPS yang berisi : 
# 	IP_Sem_1, IP_Sem_2, IP_Sem_3, IP_Sem_4, IP_Sem_5, IP_Sem_6, IP_Sem_7, IP_Sem_8
# deklarasikan 1 variabel bertipe mahasiswa dengan nama variabel adalah nama kalian

# NOT SOLVE
# # FUNGSI MENENTUKAN JURUSAN DENGAN KODE
# def jurusan(inp):
# 	Kodejurusan = ['FTKI', 'FEB', 'FISIP']
# 	if inp == 1:
# 		print(Kodejurusan[0])
# 	elif inp == 2:
# 		print(Kodejurusan[1])
# 	elif inp == 3:
# 		print(Kodejurusan[2])

# FUNGSI TANGGAL LAHIR
def tgllhr():
	# input user
	it = input('Masukkan tgl:')
	ib = input('Masukkan bulan:')
	ith = input('Masukkan tahun:')

	# cek input user 
	if it > 31:
		print('tgl tidak tersedia')
	elif ib > 12:
		print('bulan tidak tersedia')
	elif ith > 2010:
		print('tahun yang anda masukkan tidak masuk akal')

	# data input user
	Datalahir = {'tgl': int(it), 'bln':int(ib), 'thn':int(ith)}

	# output data input user
	print(Datalahir.items())

tgllhr()

# latihan ini baru sampai membuat kerangka fungsi jurusan
# fungsi tanggal lahir belum selesai

# #######################################################################################################
# PROBLEM
# 4. buatlah algoritma suatu program untuk menyimpan dan menampilkan data pegawai dengan spesifikasi sebagai berikut:
# pegawai merupakan tipe bentukan yang memiliki Nama, ID_Pegawai, Jenis_Kelamin, Jabatan, Tahun_Masuk, Gaji, dan Tunjangan
# Jabatan hanya dapat diisi dengan Pegawai, Manager, dan Direktur, sementara Jenis_kelamin hanya dapat diisi dengan L atau P
# Program akan meminta input user untuk mengisi Nama, ID_Pegawai, Jenis_Kelamin, dan Jabatan

# Program akan menghitung isi dari Gaji sesuai Jabatan (Pegawai = 3 juta, Manager = 5 juta, Direktur = 8 juta)
# Program akan menghitung isi dari Tunjangan sesuai lama bekerja (asumsi lama bekerja dihitung hingga tahun 2014)
# 	- Pegawai <= 1 tahun = 1 juta, Pegawai 1-2 tahun = 1.5 juta, Pegawai > 2 tahun = 2 juta
# 	- Manajer <= 1 tahun = 2 juta, Manajer > 1 tahun = 3 juta
# 	- Direktur <= 1 tahun = 3 juta, Direktur > 1 tahun = 4 juta

# NOT SOLVE
# #######################################################################################################

