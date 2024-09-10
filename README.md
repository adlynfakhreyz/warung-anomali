# Warung Anomali

---
##### Nama  : Andi Muhammad Adlyn Fakhreyza Khairi Putra
##### NPM   : 2306241713
##### Kelas : PBP B
##### Link  : http://andi-muhammad37-warunganomali.pbp.cs.ui.ac.id/

- ## Step-by-step Implementasi poin-poin yang ada pada Checklist Tugas 2
___

### Membuat Proyek Django
1. Hal pertama yang perlu dilakukan sebelum membuat proyek Django adalah dengan membuat direktori dengan nama yang diinginkan (dalam project ini nama direktorinya adalah "```warung-anomali```"). Kemudian pergi ke terminal dan pastikan berada didalam direktori ```.\warung-anomali```, dan lakukan inisialisasi repositori git dengan menjalankan: ```git init``` <br> hal ini dilakukan untuk men-*track* perubahan dan *progress* yang ada dalam proyek.
Buat juga *remote repository* di GitHub dan hubungkan dengan repositori di lokal ini.
2. Selanjutnya buat *virtual environment* dengan menjalankan: ```python -m venv env``` <br> dan aktifkan *virtual environment*-nya dengan menjalankan: ```env\Scripts\activate``` <br> *virtual environment* ini dibuat untuk mengisolasi package dan dependencies yang digunakan pada proyek agar tidak mengganggu proyek lain, pun sebaliknya.
3. Langkah selanjutnya adalah menyiapkan *dependencies* dengan cara membuat file baru dengan nama ```requirements.txt``` pada direktori dan menuliskan *dependenciesnya* di file txt tersebut kemudian menjalankan: ```pip install -r requirements.txt ``` <br> untuk melakukan instalasi *dependencies* yang sudah dituliskan dalam ```requirements.txt```.
4. Setelah *dependencies* sudah terinstal, proyek Django dengan nama ```warung_anomali``` bisa dibuat dengan menjalankan: ```django-admin startproject warung_anomali .``` <br> <br> Untuk keperluan *deployment* di local tambahkan juga string ```"localhost"``` dan ```"127.0.0.1"``` pada list ```ALLOWED_HOSTS``` yang bisa ditemukan di ```settings.py``` di dalam direktori ```warung_anomali```. <br> <br> Tambahkan juga berkas ```.gitginore``` untuk memberitahu file/direktori yang tidak perlu di-*track* oleh ```git```. Sebelum melakukan *add* file apapun, *add*, *commit*, *push* terlebih dahulu berkas `.gitignore`.

### Membuat Aplikasi ```main```
1. Untuk membuat aplikasi ```main```, pergi ke terminal dan jalankan perintah: ```python manage.py startapp main``` <br> sebelum menjalankannya pastikan berada pada direktori utama yaitu ```warung-anomali```. Setelah perintah dijalankan akan muncul direktori baru dengan nama ```main```.
2. Setelah itu, agar Django mengenali  aplikasi ```main``` sebagai bagian dari proyek,  daftarkan aplikasi ```main``` ke dalam proyek dengan menambahkan string ```'main'``` ke dalam list ```INSTALLED_APPS``` pada ```settings.py``` yang berada di dalam direktori ```warung_anomali```.

### Melakukan *routing* agar dapat menjalankan aplikasi main
1. Buka `urls.py` pada proyek `warung_anomali` kemudian tambahkan `path('', include('main.urls'))` pada list `urlpatterns` seperti berikut:
    ```py
    from django.contrib import admin
    from django.urls import path
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')), 
    ]
    ```
    Bagian `path('', include('main.urls'))` menghubungkan root URL (yaitu, URL tanpa tambahan apapun seperti `admin/`) dengan file `urls.py` di dalam aplikasi main. Path URL dibiarkan string dibiarkan kosong agar halaman aplikasi main dapat diakses secara langsung. Sedangkan `include('main.urls')` mengarahkan Django untuk memproses URL berdasarkan pola yang didefinisikan di dalam file `urls.py` milik aplikasi main.

### Membuat model
1. Untuk membuat model pada aplikasi ```main```, saya menuliskan kode berikut ke dalam ```models.py```:
    ```py
    from django.db import models

    class Product(models.Model): # model dengan nama Product
        name = models.CharField(max_length=255) # attribute nama
        price = models.IntegerField() # attribute harga
        description = models.TextField() # attribute deskripsi
    ```
2. Karena melakukan perubahan terhadap model sebelumya, saya perlu melakukan migrasi model dengan menjalankan: ```python manage.py makemigrations``` <br> untuk membuat migrasi model, kemudian melakukan migrasi dengan menjalankan: ```python manage.py migrate```

### Membuat fungsi pada ```views.py``` untuk dikembalikan ke dalam template ```html```
1. Sebelum membuat fungsi pada ```views.py```, terlebih dahulu saya membuat direktori ```templates``` di dalam ```main```. Kemudian membuat file ```main.html``` di dalam ```templates``` dengan implementasi sebagai berikut:
    ```html
    <h1>{{project_name}}</h1>

    <h5>NPM: </h5>
    <p>{{npm}}</p>
    <h5>Name: </h5>
    <p>{{name}}</p> 
    <h5>Class: </h5>
    <p>{{class}}</p> 
    ```
    Template ini akan menggunakan data dari konteks yang dikirimkan oleh fungsi di ```views.py```.
1. Kemudian dibuat fungsi ```show_main``` pada ```views.py``` yang bertugas untuk menghasilkan respons yang menyajikan halaman HTML sesuai data yang diberikan. Fungsi ini menggunakan template ```main.html``` dan mengirimkan konteks nama proyek, NPM, nama lengkap, dan kelas.
    ```py
    from django.shortcuts import render

    # Create your views here.
    def show_main(request):
        context = {
            'project_name' : 'Warung Anomali',
            'npm' : '2306241713',
            'name': 'Andi Muhammad Adlyn Fakhreyza Khairi Putra',
            'class': 'PBP B'
        }

        return render(request, "main.html", context)
    ```

###  Membuat *routing* pada ````urls.py```` aplikasi ```main``` untuk memetakan fungsi yang telah dibuat pada ```views.py```
1. Selanjutnya, untuk membuat *routing* pada ```urls.py``` yang berada dalam aplikasi ```main``` (buat terlebih dahulu `urls.py` dahulu jika belum),  tambahkan ```path('', show_main, name='show_main')``` pada list ```urlpatterns```, seperti pada kode berikut:
    ```py
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
    Dengan menambahkan ini, tampilan yang dihasilkan fungsi `show_main` akan ditampilkan ketika aplikasi `main` diakses.


### Melakukan *Deployment*
1. Untuk melakukan *deployment* ke PWS, *Login* terlebih dahulu ke PWS, dan *Create New Project*.
3. Setelah itu jalankan *Project Commands*, kemudian ubah kembali nama *branch* menjadi main dengan menjalankan: `git branch -M main`
4. Apabila status *deployment* pada proyek di PWS sudah *Running*, artinya sudah berhasil di *deploy*.

### Membuat `README.md` serta menjawab pertanyaan
`README.md` dan jawaban ini ditulis sesuai dnegan perintah Tugas dan dengan mereka-ulang tahapan-tahapan yang sudah saya lakukan ketika membuat proyek Django , sambil membaca materi yang relevan dalam penyusunan `README.md` ini.


- ## Bagan *request client* ke web aplikasi serta kaitan antara ```urls.py```, ```views.py```, ```models.py```, dan berkas ```html```.
---
<div align="center">
  <img src="https://imgtr.ee/images/2024/09/10/2ebe9975bb81330faeb31833cc9ad7cc.png" alt="Bagan" />
</div>


- ## Fungsi ```git``` dalam pengembangan perangkat lunak
---
Dalam pengembangan perangkat lunak, `git` memainkan peran penting sebagai *version control system* yang membantu *developer* mengelola perubahan kode secara efektif dan efisien. Setiap perubahan yang dilakukan dalam proyek dapat disimpan sebagai commit, yang memungkinkan kita untuk kembali ke versi sebelumnya jika terjadi kesalahan. Ini memberikan rasa aman saat mengembangkan fitur baru atau memodifikasi yang sudah ada, karena kita tahu bahwa kita selalu bisa kembali ke titik sebelumnya tanpa harus khawatir kehilangan pekerjaan yang sudah dilakukan.

`git` juga memiliki riwayat perubahan yang sangat detil. Setiap perubahan yang dilakukan dicatat sebagai commit dengan pesan yang menggambarkan perubahan tersebut. Hal ini memudahkan pengembang untuk melacak apa yang telah diubah, siapa yang melakukan perubahan, dan kapan perubahan tersebut dilakukan. Ini sangat membantu saat perlu melakukan debugging jika terdapat masalah.

Sebagai sistem terdistribusi, `git` memungkinkan setiap kolaborator memiliki salinan lengkap suatu proyek di komputer mereka masing-masing. Sehingga jika terjadi kerusakan perangkat / data pada satu sumber, masih ada backup data dari kolaborator lainnya. Hal ini meningkatkan keamanan dan integritas data, membuat proses pengembangan terasa lebih aman dan nyaman.

Selain itu `git` juga memfasilitasi kolaborasi dan membantu manajemen proyek ketika bekerja dalam tim. Dengan adanya *branching*, anggota tim bisa dengan mudah membuat *branch* baru untuk mengerjakan fitur spesifik, sementara *branch* utama tetap stabil. Setelah fitur selesai, *branch* dapat digabungkan ke *branch* utama. Ini memungkinkan anggota tim dapat bekerja dan mengerjakan bagiannya masing-masing tanpa harus mengkhawatirkan mengganggu satu sama lain. Ini memungkinkan pengembangan yang lebih terstruktur, serta meminimalisir terjadinya kekacauan dalam kode.


- ## Mengapa *Framework* Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
---
Menurut saya, Berikut ini alasan mengapa Django cocok dijadikan permulaan pembelajaran pengembangan perangkat lunak:
1. Kemudahan, Django memudahkan pengembangan aplikasi web dengan menyediakan berbagai fitur bawaan. contohnya adalah Django admin. Kemudahan ini membantu pemula untuk lebih fokus pada logika aplikasi tanpa harus menangani aspek-aspek yang kompleks.
2. Kepopuleran dan Komunitas, Django sangat populer dan sangat banyak digunakan. Kepopuleran ini menandakan tersedianya sumber-sumber belajar seperti tutorial dan panduan yang berlimpah. Selain itu juga komunitas yang besar dan aktif dapat menjadi lingkungan yang baik bagi pemula untuk belajar, diskusi, dan berbagi pengalaman.
3. Struktur MVT, Dengan menggunakan arsitektur Model-View-Template, yang memisahkan komponen untuk data, logika aplikasi, dan tampilan, membuat struktur aplikasi terlihat lebih rapi dan mudah dipahami untuk pemula. Pembagian komponen ini memudahkan saya pribadi untuk memahami bagaimana data, logika, dan tampilan saling berinteraksi.
4. Dokumentasi, Django juga menyediakan dokumentasi yang lengkap dan mudah dipahami. Panduan dan tutorial yang jelas tentu saja adalah sumber daya yang berharga bagi pemula.


- ## Mengapa model pada Django disebut sebagai ORM?
---
Karena pada Django, *Model* adalah representasi dari tabel basis data, Setiap model adalah subclass dari `django.db.models.Model`, dan setiap atribut dari model tersebut akan menjadi kolom dalam tabel database. Django juga menyediakan API *query* yangs mengakomodasi *methods* seperti `.filter()`, `.exclude()`, dan `.aggregate()` untuk membangun *query* kompleks tanpa menulis SQL secara langsung. Django mengubah *query* ini menjadi SQL yang sesuai dan menerapkannya pada basis data. Fitur-fitur ini memungkinkan *developer* dapat berinteraksi dengan basis data melalui *code* saja tanpa harus menulis *query* SQL secara manual, spesifiknya melalui *Object Model*. Oleh karena itu, model pada Django disebut *Object-Relational-Mapping* (ORM).




