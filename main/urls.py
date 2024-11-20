from django.urls import path
from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user, edit_product, delete_product, add_product_entry_ajax, add_product_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product-entry', create_product_entry, name='create_product_entry'), # routing untuk form
    path('xml/', show_xml, name='show_xml'), # routing untuk melihat keseluruhan object dalam format xml
    path('json/', show_json, name='show_json'), # routing untuk melihat keseluruhan object dalam format json
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'), # routing untuk melihat object dengan id tertentu dalam format xml
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'), # routing untuk melihat object dengan id tertentu dalam format json
    path('register/', register, name='register'), # routing untuk ke halaman register
    path('login/', login_user, name='login'), # routing untuk ketika ingin login
    path('logout/', logout_user, name='logout'), # routing untuk ketika ingin logout
    path('edit_product/<uuid:id>', edit_product, name='edit_product'),
    path('delete_product/<uuid:id>', delete_product, name='delete_product'),
    path('create-product-entry-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('create-flutter/', add_product_flutter, name='add_product_flutter'),
]