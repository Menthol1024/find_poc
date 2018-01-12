from django.contrib import admin
from .models import Audit, Poc, ExchangeCode
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.contrib.admin import SimpleListFilter

# Register your models here.

admin.site.register(Poc)
admin.site.register(ExchangeCode)


class AuditFilter(SimpleListFilter):
    parameter_name = '审核'
    title = _('审核状态')

    def lookups(self, request, model_admin):
        return (
             ('0', _('未审核')),
             ('1', _('已审核')),
        )

    def queryset(self, request, queryset):
        if self.value() in ('0', '1'):
            return queryset.filter(review=self.value())
        elif self.value() is None:
            return queryset.filter(review=0)


class AuditAdmin(admin.ModelAdmin):
    list_display = ('another', 'email', 'package', 'version', 'desc', 'time', 'bugtype','audit','delete')
    list_filter = [AuditFilter]
    actions = ['delete_model']

    def get_queryset(self, request):
        qs = super(AuditAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(review=0)

    def audit(self, obj):
        return mark_safe(
            '<a href="/admin/{0}/1/audit/">{1}</a>'.format(
                obj.id,
                _("通过")
            )
        )

    def delete(self,obj):
        return mark_safe('<a href="{id}/delete/"/>删除</a>'.format(id=obj.id))

    delete.allow_tags = True
    delete.short_description = _("删除")
    audit.allow_tags = True
    audit.short_description = _("通过")


admin.site.register(Audit, AuditAdmin)
