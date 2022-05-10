from django.contrib import admin
from .models import BookCompra, BookVenda, BookVendaMerc, BookCompraMerc

# Register your models here.
admin.site.register(BookCompra)
admin.site.register(BookVenda)
admin.site.register(BookCompraMerc)
admin.site.register(BookVendaMerc)





