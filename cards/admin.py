from django.contrib import admin
from .models import Category, Item
from adminsortable2.admin import SortableAdminMixin
from modeltranslation.admin import TabbedTranslationAdmin

@admin.register(Category)
class SortAdminCategory(SortableAdminMixin, TabbedTranslationAdmin):
    pass


@admin.register(Item)
class SortAdminitems(SortableAdminMixin, admin.ModelAdmin):
    pass
