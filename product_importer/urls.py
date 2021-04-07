from django.conf.urls import url
from product_importer import views
 
app_name = 'product_importer'
urlpatterns = [
    # url(r'^$', views.HomePageView.as_view()),
    url(r'^$', views.upload_csv, name='upload_csv'),
    url(r'sign_s3', views.sign_s3, name='sign_s3'),
    url(r'products', views.ProductsView.as_view()),
    url(r'delete', views.delete_records, name='delete_records')
]