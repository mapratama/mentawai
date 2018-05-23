from django.contrib import admin

from .models import PaymentHistory


@admin.register(PaymentHistory)
class PaymentHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_id', 'status', 'created')
    list_filter = ('status',)
    search_fields = ('payment_id', )
    ordering = ('created',)
