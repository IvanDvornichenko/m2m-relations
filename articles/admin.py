from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):

    def clean(self):
        count = 0
        for form in self.forms:
            try:
                if form.cleaned_data.get('is_main'):
                    count += 1
            except AttributeError:
                pass
        if count < 1:
            raise ValidationError('Укажите основной раздел')
        elif count > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()


class ScopeInline(admin.TabularInline):
    formset = ScopeInlineFormset
    model = Scope
    extra = 3



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
        inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
