from django.contrib import admin

from backoffice.models import Genre, Editeur, Auteur, Livre, Usure, Exemplaire, Adherent, emprunt, Stock

# Register your models here.

admin.site.register(Genre)
admin.site.register(Editeur)
admin.site.register(Auteur)
admin.site.register(Livre)
admin.site.register(Usure)
admin.site.register(Exemplaire)
admin.site.register(Adherent)
admin.site.register(emprunt)
admin.site.register(Stock)

