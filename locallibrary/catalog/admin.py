from django.contrib import admin
from .models import Book, Author, Genre, Language, BookInstance


# Register your models here.
# admin.site.register(Book)
admin.site.register(Language)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)

class BookInline(admin.TabularInline):
    model = Book

# this is for modeladmin registeration for Author
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    
    # this handle the detail_view of the fields of each authors
    fields = ["first_name", "last_name", ("date_of_birth", "date_of_death")]
    inlines = [BookInline]
    
admin.site.register(Author, AuthorAdmin)

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    model = BookInstance
    list_filter = ('status', 'due_back') 
    list_display = ("id", "book", "due_back", "status")
    
    # this handle the detail_view of the fields of each bookinstances
    fieldsets = [
        (None, {
            'fields': ('book', 'imprint')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')    
        }),
    ]