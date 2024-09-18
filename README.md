# Warung Anomali

---
##### Nama  : Andi Muhammad Adlyn Fakhreyza Khairi Putra
##### NPM   : 2306241713
##### Kelas : PBP B
##### Link  : http://andi-muhammad37-warunganomali.pbp.cs.ui.ac.id/

# Tugas 2
___
- ## Step-by-step Implementasi poin-poin yang ada pada Checklist Tugas 2
___

#### Membuat Proyek Django
1. Hal pertama yang perlu dilakukan sebelum membuat proyek Django adalah dengan membuat direktori dengan nama yang diinginkan (dalam project ini nama direktorinya adalah "```warung-anomali```"). Kemudian pergi ke terminal dan pastikan berada didalam direktori ```.\warung-anomali```, dan lakukan inisialisasi repositori git dengan menjalankan: ```git init``` <br> hal ini dilakukan untuk men-*track* perubahan dan *progress* yang ada dalam proyek.
Buat juga *remote repository* di GitHub dan hubungkan dengan repositori di lokal ini.
2. Selanjutnya buat *virtual environment* dengan menjalankan: ```python -m venv env``` <br> dan aktifkan *virtual environment*-nya dengan menjalankan: ```env\Scripts\activate``` <br> *virtual environment* ini dibuat untuk mengisolasi package dan dependencies yang digunakan pada proyek agar tidak mengganggu proyek lain, pun sebaliknya.
3. Langkah selanjutnya adalah menyiapkan *dependencies* dengan cara membuat file baru dengan nama ```requirements.txt``` pada direktori dan menuliskan *dependenciesnya* di file txt tersebut kemudian menjalankan: ```pip install -r requirements.txt ``` <br> untuk melakukan instalasi *dependencies* yang sudah dituliskan dalam ```requirements.txt```.
4. Setelah *dependencies* sudah terinstal, proyek Django dengan nama ```warung_anomali``` bisa dibuat dengan menjalankan: ```django-admin startproject warung_anomali .``` <br> <br> Untuk keperluan *deployment* di local tambahkan juga string ```"localhost"``` dan ```"127.0.0.1"``` pada list ```ALLOWED_HOSTS``` yang bisa ditemukan di ```settings.py``` di dalam direktori ```warung_anomali```. <br> <br> Tambahkan juga berkas ```.gitginore``` untuk memberitahu file/direktori yang tidak perlu di-*track* oleh ```git```. Sebelum melakukan *add* file apapun, *add*, *commit*, *push* terlebih dahulu berkas `.gitignore`.

#### Membuat Aplikasi ```main```
1. Untuk membuat aplikasi ```main```, pergi ke terminal dan jalankan perintah: ```python manage.py startapp main``` <br> sebelum menjalankannya pastikan berada pada direktori utama yaitu ```warung-anomali```. Setelah perintah dijalankan akan muncul direktori baru dengan nama ```main```.
2. Setelah itu, agar Django mengenali  aplikasi ```main``` sebagai bagian dari proyek,  daftarkan aplikasi ```main``` ke dalam proyek dengan menambahkan string ```'main'``` ke dalam list ```INSTALLED_APPS``` pada ```settings.py``` yang berada di dalam direktori ```warung_anomali```.

#### Melakukan *routing* agar dapat menjalankan aplikasi main
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

#### Membuat model
1. Untuk membuat model pada aplikasi ```main```, saya menuliskan kode berikut ke dalam ```models.py```:
    ```py
    from django.db import models

    class Product(models.Model): # model dengan nama Product
        name = models.CharField(max_length=255) # attribute nama
        price = models.IntegerField() # attribute harga
        description = models.TextField() # attribute deskripsi
    ```
2. Karena melakukan perubahan terhadap model sebelumya, saya perlu melakukan migrasi model dengan menjalankan: ```python manage.py makemigrations``` <br> untuk membuat migrasi model, kemudian melakukan migrasi dengan menjalankan: ```python manage.py migrate```

#### Membuat fungsi pada ```views.py``` untuk dikembalikan ke dalam template ```html```
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

####  Membuat *routing* pada ````urls.py```` aplikasi ```main``` untuk memetakan fungsi yang telah dibuat pada ```views.py```
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


#### Melakukan *Deployment*
1. Untuk melakukan *deployment* ke PWS, *Login* terlebih dahulu ke PWS, dan *Create New Project*.
3. Setelah itu jalankan *Project Commands*, kemudian ubah kembali nama *branch* menjadi main dengan menjalankan: `git branch -M main`
4. Apabila status *deployment* pada proyek di PWS sudah *Running*, artinya sudah berhasil di *deploy*.

#### Membuat `README.md` serta menjawab pertanyaan
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

# Tugas 3
---
- ## Mengapa *Data delivery* diperlukan dalam pengimplementasian sebuah platform?
---
Dalam pengembangan suatu platform, sering kali kita ingin mengirimkan data dari satu *stack* ke *stack* lainnya, menerima data dari *user*, dan menyajikan data untuk *user*. Pengiriman data yang efektif, efisien, dan *secure* sangat diperlukan untuk memastikan data dikirimkan dengan tepat/benar, cepat, dan aman.

*Data delivery* memiliki peran signifikan dalam pengiriman data dari satu *stack* ke *stack* lainnya. Ketika data dipindahkan antar *stack*, *Data delivery* yang efektif memastikan informasi dikirimkan dengan akurat dan cepat, yang sangat penting untuk integrasi dan interoperabilitas antar komponen platform. Dengan sistem yang optimal, proses pengiriman data dapat dilakukan dengan lancar sehingga menjaga alur kerja dan mengurangi kemungkinan kesalahan atau kehilangan data.

*Data delivery* yang baik juga sangat diperlukan dalam mendukung interaksi antar *user* dan platform. *Data delivery* memastikan *user* dapat mengakses informasi yang tersedia saat dibutuhkan. Pengiriman data yang efektif dan efisien juga memungkinkan *user* untuk berkomunikasi dengan platform tanpa gangguan, memberikan respons yang cepat dan akurat. 

- ## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
---
XML dan JSON memiliki kelebihan dan kekurangannya masing-masing, namun menurut saya JSON lebih unggul, setidaknya untuk alasan-alasan berikut, yang juga menjelaskan mengapa JSON lebih populer:
* JSON lebih ringkas, sederhana, dan mudah dipahami dibandingkan XML. Format JSON menggunakan struktur pasangan kunci-nilai yang jelas, membuat data lebih mudah dibaca dan ditulis oleh manusia serta lebih mudah diproses oleh mesin.
* Karena JSON lebih ringkas, ukuran data yang dikirim dan diterima biasanya lebih kecil dibandingkan dengan XML. Ini dapat mengurangi waktu pemrosesan.
* JSON lebih cepat diparse oleh browser dan aplikasi karena strukturnya yang sederhana dan sudah dioptimalkan. Parsing JSON biasanya memerlukan lebih sedikit waktu dibandingkan XML
* Integrasi dengan JavaScript, JSON secara bawaan didukung oleh JavaScript, menjadikannya format utama untuk aplikasi web dan API yang berbasis JavaScript. JSON dapat dengan mudah diintegrasikan dan diproses langsung oleh JavaScript.

- ## Fungsi dari method `is_valid()` pada form Django dan alasan method tersbut dibutuhkan
---
Fungsi method `is_valid()` adalah untuk memeriksa apakah data yang dimasukkan dalam form memenuhi semua aturan validasi yang telah ditentukan dalam form yang bersangkutan. Meliputi: pengecekan bahwa semua field yang diperlukan telah diisi, data yang dimasukkan sesuai dengan tipe yang diharapkan, dan apakah data memenuhi batasan atau kriteria yang telah ditetapkan.

Alasan mengapa method ini diperlukan antara lain:
    1. Memastikan data yang diisikan oleh *user* sesuai dengan format dan aturan yang telah ditetapkan.
    2. Mencegah data yang salah atau tidak sesuai dari masuk ke dalam sistem
    3. Meningkatkan keamanan aplikasi dengan memastikan bahwa data yang dimasukkan tidak mengandung nilai-nilai yang dapat membahayakan aplikasi atau database, seperti input berbahaya yang dapat menyebabkan serangan *SQL injection* atau *XSS*.

- ## Mengapa `csrf_token` dibutuhkan saat membuat form di Django? Apa yang dapat terjadi jika tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
---
#### Mengapa csrf_token Diperlukan Saat Membuat Form di Django? 
Karena `csrf_token` berfungsi untuk memverifikasi *request* yang dikirim ke server berasal dari form yang valid dan bukan dari sumber luar. Dengan memastikan bahwa permintaan hanya diproses jika token yang disertakan sesuai dengan yang ada di server, data *user* dan operasi penting dapat terlindungi dari campur tangan oknum yang tidak sah.

#### Apa yang Terjadi Jika Tidak Menambahkan csrf_token pada Form di Django dan bagaimana Hal Tersebut Dapat Dimanfaatkan oleh Penyerang?? 
Aplikasi menjadi rentan terhadap serangan CSRF. Penyerang dapat membuat form berbahaya di web yang mereka buat dan mengirimkan *request* berbahaya menggunakan kredensial *user* yang sudah *login*. Dengan begitu penyerang dapat melakukan tindakan yang merugikan seperti mulai dari mengakses data secara tidak sah, perubahan data, serta transaksi tidak sah.

- ## Step-by-step Implementasi poin-poin yang ada pada Checklist Tugas 3
---
#### Membuat input form untuk menambahkan objek model pada app sebelumnya
1. sebelum membuat form, saya mengimplementasikan *Skeleton* terlebih dahulu sebagai kerangka *Views*. Dengan cara membuat subdirektori baru dengan nama `template` di root dan menambahkan berkas `base.html` dengan isi sebagai berikut:
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```
2. Kemudian menambahkan baris berikut pada `settings.py agar `base.html` terdeteksi sebagai berkas template:
```py
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan konten baris ini
        'APP_DIRS': True,
        ...
    }
]
...
```
3. Selanjutnya saya mengubah sedikit `models.py` dan mengubah primary key dari integer menjadi UUID. Setelah melakukan perubahan saya melakukan migrasi model
```py
from django.db import models
import uuid
class Product(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    color = models.CharField(max_length=50)
    stock = models.IntegerField()
```

4. Membuat berkas baru `forms.py` untuk pada direktori `main` seperti berikut:
```py
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "color", "stock"]
```
5. Menambahkan beberapa import, fungsi `create_product_entry` dan mengubah sedikit fungsi `show_main` pada `views.py` menjadi seperti berikut:
```py
from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product

# Fungsi yang menampilkan main
def show_main(request):
    product_entries = Product.objects.all()
    
    context = {
        'project_name' : 'Warung Anomali',
        'npm' : '2306241713',
        'name': 'Andi Muhammad Adlyn Fakhreyza Khairi Putra',
        'class': 'PBP B',
        'product_entries': product_entries
    }

    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```
6. Kemudian menambahkan `url` berikut pada `urlpatterns` didalam `urls.py` yang berada di direktori `main`:
```py
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product-entry', create_product_entry, name='create_product_entry'),
    ...
]
```
7. Saya juga tidak lupa menambahkan file `create_product_entry.html` pada subdirektori templates untuk menampilkan form
```html
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Product Entry</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Product Entry" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```
8. Terakhir saya mengubah isi `main.html` menjadi seperti berikut agar menggunakan template `base.html`, menambahkan button untuk pergi ke form, serta menampilkan data product yang telah diisikan pada form
```html
{% extends 'base.html' %}
{% block content %}
<h1>{{project_name}}</h1>

<h5>NPM: </h5>
<p>{{npm}}</p>
<h5>Name: </h5>
<p>{{name}}</p> 
<h5>Class: </h5>
<p>{{class}}</p> 

{% if not product_entries %}
<p>Belum ada data product pada warung alomani.</p>
{% else %}
<table>
  <tr>
    <th>Product Name</th>
    <th>Price</th>
    <th>Descriptions</th>
    <th>Color</th>
    <th>Stock</th>    
  </tr>

  {% comment %} Berikut cara memperlihatkan data product di bawah baris ini 
  {% endcomment %} 
  {% for product_entry in product_entries %}
  <tr>
    <td>{{product_entry.name}}</td>
    <td>{{product_entry.price}}</td>
    <td>{{product_entry.description}}</td>
    <td>{{product_entry.color}}</td>
    <td>{{product_entry.stock}}</td>    
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_product_entry' %}">
  <button>Add New Product Entry</button>
</a>
{% endblock content %}

```

Dengan melakukan step - step diatas form sudah dapat digunakan

#### Menambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID
1. Untuk melihat objek yang sudah ditambahkan, saya menambahkan 4 fungsi berikut ke dalam `views.py` (`show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id`) dan juga mengimport `HttpResponse` dan `serializers`. Sehingga isi `views.py` menjadi seperti berikut:
```py
from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

# Fungsi yang menampilkan main
def show_main(request):
    product_entries = Product.objects.all()
    
    context = {
        'project_name' : 'Warung Anomali',
        'npm' : '2306241713',
        'name': 'Andi Muhammad Adlyn Fakhreyza Khairi Putra',
        'class': 'PBP B',
        'product_entries': product_entries
    }

    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

#### Membuat routing URL untuk masing-masing views yang telah ditambahkan
1. Terakhir saya melakukan routing dengan menambahkan `url` berikut ke `urlpatterns` pada `urls.py` yang berada di direktori `main`:
```py
from django.urls import path
from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product-entry', create_product_entry, name='create_product_entry'), # routing untuk form
    path('xml/', show_xml, name='show_xml'), # routing untuk melihat keseluruhan object dalam format xml
    path('json/', show_json, name='show_json'), # routing untuk melihat keseluruhan object dalam format json
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'), # routing untuk melihat object dengan id tertentu dalam format xml
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'), # routing untuk melihat object dengan id tertentu dalam format json
]
```

- ## *Screenshot* dari hasil akses URL pada *Postman*
---
**XML**
<img src="https://i.ibb.co.com/K0YW1dV/Whats-App-Image-2024-09-18-at-06-58-51-870bb0f4.jpg" alt="xml" />
  
**JSON**
<img src="https://i.ibb.co.com/1Jnsnqg/Whats-App-Image-2024-09-18-at-10-19-29-8b4ffcc2.jpg" alt="json" />

**XML by id**
<img src="https://i.ibb.co.com/6HtJzBs/Whats-App-Image-2024-09-18-at-07-00-01-44c3e2f7.jpg" alt="xml_by_id" />

**JSON by id**
<img src="https://i.ibb.co.com/B6PcNvz/Whats-App-Image-2024-09-18-at-07-00-51-bd121ce1.jpg" alt="json_by_id" />
