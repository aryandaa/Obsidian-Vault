#devops 
Sebelumnya kita hanya mengintegrasikan 2 container saja yaitu aplikasi dan database, gimana kalo pada Study case real nya kita harus mengintegrasikan puluhan container sekaligus, yang pastinya bakalan ribet dan melelahkan kita bikin container, network, dan integrasikannya satu per satu. 

di docker sendiri ada 1 fitur bernama docker compose, docker compose digunakan untuk mengautomisasi proses-proses tersebut, misalnya membuat container, connect antar container, membuat network, dan integrasi ke Environment Variable, itu dilakukan dalam 1 buah file dan kita cukup menggunakan 1 perintah Docker Compose saja untuk menjalankan semua itu.

untuk bisa menggunakan Docker Compose ini kita cukup buat 1 buah file konfigurasi dalam format .yml. untuk penamaan standard untuk file ini adalah "docker-compose.yml".


Hal pertama yang perlu di set adalaha set container-container terlebih dahulu, untuk men set container kita perlu membungkusnya di dalam attribute "services:"
```yml
services:
	mongo:
		container_name: mongo
		image: mongo:7
		ports: 
			- 27017:27017
		environment:
			MONGO_INITDB_ROOT_USERNAME: root
			MONGO_INITDB_ROOT_PASSWORD: 123456
		networks: 
			- python_network
	app-python:
		container_name: app-python
		image: aryanda/app-python:compose
		ports: 
			- 8080:5000 
		depends_on: 
			- mongo
		environment:
			NAMA: Aryanda
			DB_HOST: mongo
			DB_PORT: 27017
			DB_USER: root
			DB_PASS: 123456
		networks: 
			- python_network
```
`container_name:` nama container.
`image:` nama image:tag.
`ports:` - port untuk tampil ke public : port bawaan docker/image nya.

untuk memberitahu compose agar container tersebut butuh container lain agar bisa jalan, disini bisa menggunakan atribute di dalam container bernama 
```
depens_on: 
	- <namaContainer>
	- <namaContainer2>
(bisa multiple)
```
kenapa kita harus menggunakan itu? agar di compose bisa tau mana yang lebih dahulu di prioritaskan untuk running agar tidak nabrak atau keduluan container parent daripata child nya.

environment adalah set untuk menambahkan environment variable yang di butuhkan oleh aplikasi itu.


hal selanjutnya yang perlu di set adalah Network agar semua container terhubung ke dalam network yang sama dengan menggunakan atribute `networks:`
```yml
networks:
	python_network: 
		name: python_network
```
jadi di setiap service container diatas perlu ditambahkan lagi atribute networks ini untuk connect nya.

docker-compose.yml full:
```yml
services:
	mongo:
		container_name: mongo
		image: mongo:7
		ports: 
			- 27017:27017
		environment:
			MONGO_INITDB_ROOT_USERNAME: root
			MONGO_INITDB_ROOT_PASSWORD: 123456
		networks: 
			- python_network
	app-python:
		container_name: app-python
		image: aryanda/app-python:compose
		ports: 
			- 8080:5000 
		depends_on: 
			- mongo
		environment:
			NAMA: Aryanda
			DB_HOST: mongo
			DB_PORT: 27017
			DB_USER: root
			DB_PASS: 123456
		networks: 
			- python_network
			  
networks:
	python_network: 
		name: python_network
```

>untuk identasi di .yml tidak menggunakan tab tetapi spasi 2 kali, kalo pake tab tidak bisa

sekarang kita jalankan docker compose ini untuk automisasi semuanya, dengan cara:
`docker compose up -d`
jika ketemu output begini artinya berhasil
```output
[+] up 2/2
 ✔ Container mongo      Started                                          0.3s
 ✔ Container app-python Started                                          0.4s
```

kalo ngebuka localhost:8080 di browser maka akan berhasil connect
![](img/Pasted%20image%2020260726224635.png)

Kesimpulan:
Pada praktik ini, saya mempelajari bagaimana mengintegrasikan beberapa container menggunakan Docker Compose sehingga seluruh layanan dapat dijalankan secara otomatis dalam satu konfigurasi. Aplikasi Python yang sebelumnya berjalan secara mandiri berhasil dihubungkan dengan database MongoDB melalui Docker Network tanpa perlu mengetahui alamat IP container, melainkan cukup menggunakan nama service sebagai host. Selain itu, saya juga memahami pentingnya penggunaan Environment Variable untuk mengelola konfigurasi aplikasi secara fleksibel, serta proses autentikasi MongoDB yang harus diinisialisasi sejak container pertama kali dibuat. Dengan Docker Compose, proses menjalankan aplikasi menjadi jauh lebih sederhana karena pembuatan network, konfigurasi environment, serta eksekusi beberapa container dapat dilakukan hanya dengan satu perintah (`docker compose up -d`). Praktik ini memberikan pemahaman bahwa Docker Compose merupakan solusi untuk mengelola aplikasi yang terdiri dari banyak service secara lebih terstruktur, mudah dipelihara, dan mendekati alur deployment yang digunakan pada lingkungan pengembangan maupun produksi.

