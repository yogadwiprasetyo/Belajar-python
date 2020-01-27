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

# SOLVE
# FUNGSI JURUSAN
# AWAL FUNGSI
def jurusan():
	# input user
	# meminta input kode jurusan
	inpKode = int(input('Masukkan kode jurusan: '))

	# data list
	# list sebagai tempat nama jurusan
	Kodejurusan = ['Teknik Informatika', 'Manajemen', 'Ilmu Komunikasi']

	# proses 
	# jika input user sama dengan kode jurusan, tampilkan nama jurusan
	if inpKode == 1:
		# print("Jurusan: {}".format(Kodejurusan[0]))
		output = Kodejurusan[0]
	elif inpKode == 2:
		# print("Jurusan: {}".format(Kodejurusan[1]))
		output = Kodejurusan[1]
	elif inpKode == 3:
		# print("Jurusan: {}".format(Kodejurusan[2]))
		output = Kodejurusan[2]
	else:
		# print("kode yang dimasukkan tidak cocok!")
		output = 'kode yang dimasukkan tidak cocok!'

	# output
	# menghasilkan output dari proses diatas dengan return
	return output
# AKHIR FUNGSI


# FUNGSI TANGGAL LAHIR
# AWAL FUNGSI
def tgllhr():
	# data list
	# menampung tanggal lahir user
	Tgl_lahir = []

	# input user
	# memasukkan tanggal,bulan dan tahun lahir
	print('===Masukkan Tanggal Lahir===')
	it = int(input('Tanggal: '))
	ib = raw_input('Nama Bulan: ')
	ith = int(input('Tahun: '))

	# cek input user 
	# jika tanggal dan tahun yang dimasukkan melebihi batas, tampilkan pesan warning!
	if it > 31:
		print('tanggal yang dimasukkan melebihi batas')
	elif ith > 2010:
		print('tahun yang dimasukkan melebihi batas')
	else:
		Tgl_lahir.append(it)
		Tgl_lahir.append(ib)
		Tgl_lahir.append(ith)

	# cek data input user 
	# mengisi variabel output dengan nilai data list
	if len(Tgl_lahir) == 0 :
		# print('Tanggal lahir: {}'.format(Tgl_lahir[:]))
		output = Tgl_lahir[:]
	else:
		# print('Tanggal lahir: {} {} {}'.format(Tgl_lahir[0],Tgl_lahir[1],Tgl_lahir[2]))
		output = Tgl_lahir[:]

	# output
	# menghasilkan output dari proses cek data input user dengan return
	return output
# AKHIR FUNGSI


# FUNGSI IP_SEMESTER
# AWAL FUNGSI
def ip():
	# membuat data list sebagai tempat untuk nilai ip semester
	Ips = []
	# melakukan looping untuk meminta input nilai user
	while True:
		for i in range(1, 9, 1):
			nilai = float(input('Masukkan nilai Ip Semester ke-{}: '.format(i)))
			#jika nilai ip melebihi batas, ulangi looping dari awal
			if nilai > 4.0:
				print('nilai IP yang kamu masukkan melebihi batas \nTOLONG ULANGI PENGISISAN!')
				i = 1
				Ips = []
				break
			else: 
				Ips.append(nilai)
		else:
			break

	# # menampilkan nilai ips dari input user
	# for i,n in enumerate(Ips):
	# 	print('Nilai Ip Semester ke-{}: {}'.format(i+1,n))

	# output
	# mengembalikan data input user dengan return
	return Ips
# AKHIR FUNGSI


# FUNGSI MAHASISWA
# AWAL FUNGSI
def mahasiswa():
	# looping
	# bertujuan untuk melakukan pengisian data, dengan batas yang diinginkan
	while True:
		# input user
		# menanyakan mulai isi data atau tidak
		inputData = raw_input('input data? (y/n)')
		# jika input user = y, lakukan statement dibawah
		if inputData is 'y' :
			# input user 
			# mengisi data lengkap
			namaMhs = raw_input('Nama: ')
			nimMhs = input('Nim: ')
			jurusanMhs = jurusan()
			asalMhs = raw_input('Asal: ')
			tgllhrMhs = tgllhr()
			ipsemesterMhs = ip()
			totalsksMhs = input('SKS(24/20/18): ')

			# # data list
			# # menyimpan data user
			# Data_User = [namaMhs, nimMhs, jurusanMhs, asalMhs, tgllhrMhs, ipsemesterMhs, totalsksMhs]
			
			# # data dictionary
			# # menyimpan data user
			# Data_User = {'nama':namaMhs, 'nim': nimMhs, 'jurusan': jurusanMhs, 'asal': asalMhs, 'tgllhr': tgllhrMhs, 'ips': ipsemesterMhs, 'sks': totalsksMhs}

			# output
			# menampilan data input user
			print('===== DATA MAHASISWA =====')
			print('Nama: {}'.format(namaMhs))
			print('Nim: {}'.format(nimMhs))
			print('Jurusan: {}'.format(jurusanMhs))
			print('Asal: {}'.format(asalMhs))
			print('Tanggal Lahir: {} {} {}'.format(tgllhrMhs[0],tgllhrMhs[1],tgllhrMhs[2]))
			for i,n in enumerate(ipsemesterMhs):
				print('Nilai Ip Semester ke-{}: {}'.format(i+1,n))
			print('Total SKS: {}'.format(totalsksMhs))
		# jika input user = n, maka keluar dari looping
		elif inputData is 'n' :
			break
		else:
			print('kamu belum memasukkan input y/n')

# fungsi mahasiswa
mahasiswa()

# KEKURANGAN
# output fungsi mahasiswa masih dari hasil input user
# output fungsi mahasiswa belum disimpan ke data
# output fungsi mahasiswa hanya bisa menampilkan satu data
# data tidak saling berhubungan antar satu sama lain
# terlalu banyak menggunakan if elif, semua fungsi menggunakannya
# penamaan variabel, data list dan fungsi masih belum optimal
# pada fungsi tgllhr, logika masih belum sempurna

# KELEBIHAN
# sudah memakai data list
# sudah menggunakan fungsi di dalam fungsi
# sudah menggunakan looping di dalam logika fungsi

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

