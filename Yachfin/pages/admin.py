from django.contrib import admin
from django.urls import path, reverse
from django.template.response import TemplateResponse
from django.shortcuts import redirect
from django.utils.html import format_html
from .models import Reservation

# ======================
#   CUSTOM ADMIN SITE
# ======================
class DashboardAdmin(admin.AdminSite):
    site_header = "YACHFIN"
    site_title = "Yachfin Dashboard"
    index_title = "Dashboard Overview"

    # Who can access the dashboard
    def has_permission(self, request):
        return request.user.is_active and request.user.is_staff

    # Module-level access control
    def has_module_permission(self, request, app_label):
        if request.user.is_superuser:
            return True  # Superuser sees everything
        if app_label == "auth":
            return False  # Staff cannot see users/groups
        return True

    # Filter apps for dashboard menu
    def get_app_list(self, request, app_label=None):
        app_list = super().get_app_list(request)
        if request.user.is_superuser:
            return app_list  # Superuser sees all apps
        # Staff sees all except auth
        return [app for app in app_list if app['app_label'] != "auth"]

    # Custom dashboard URLs
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('reservations-dashboard/', self.admin_view(self.dashboard), name='reservations-dashboard'),
            path('reservation/<int:reservation_id>/view/', self.admin_view(self.view_reservation),
                name='reservation-view'),
            path('reservation/<int:reservation_id>/confirm/', self.admin_view(self.confirm_reservation),
                name='reservation-confirm'),
            path('reservation/<int:reservation_id>/delete/', self.admin_view(self.delete_reservation),
                name='reservation-delete'),
        ]
        return my_urls + urls

    # =======================
    # DASHBOARD VIEW
    # =======================
    def dashboard(self, request):
        new_reservations = Reservation.objects.filter(viewed=False).count()
        confirmed_reservations = Reservation.objects.filter(status=True).count()
        total_reservations = Reservation.objects.count()
        latest_reservations = Reservation.objects.order_by('-id')[:10]

        context = dict(
            self.each_context(request),
            new_reservations=new_reservations,
            confirmed_reservations=confirmed_reservations,
            total_reservations=total_reservations,
            reservations=latest_reservations
        )
        return TemplateResponse(request, "admin/dashboard/index.html", context)

    # =======================
    # VIEW RESERVATION
    # =======================
    def view_reservation(self, request, reservation_id):
        reservation = Reservation.objects.get(pk=reservation_id)
        if not reservation.viewed:
            reservation.viewed = True
            reservation.save()

        context = dict(
            self.each_context(request),
            reservation=reservation
        )
        return TemplateResponse(request, 'admin/reservation_detail.html', context)

    # =======================
    # DELETE RESERVATION
    # =======================
    def delete_reservation(self, request, reservation_id):
        reservation = Reservation.objects.get(pk=reservation_id)
        reservation.delete()
        return redirect('admin:pages_reservation_changelist')

    # =======================
    # CONFIRM RESERVATION
    # =======================
    def confirm_reservation(self, request, reservation_id):
        reservation = Reservation.objects.get(pk=reservation_id)
        reservation.status = True
        reservation.save()
        return redirect(request.META.get('HTTP_REFERER', '/admin/'))


# =======================
# RESERVATION ADMIN
# =======================
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['names', 'emails', 'phones', 'days', 'times', 'status', 'new_status', 'dashboard_link']
    list_filter = ['status']
    search_fields = ['names', 'emails', 'phones']

    def new_status(self, obj):
        return 'New' if not obj.viewed else ''
    new_status.short_description = 'New'

    # -------------------------------
    # Add link to dashboard
    # -------------------------------
    def dashboard_link(self, obj):
        url = reverse('admin:reservations-dashboard')
        return format_html(f'<a href="{url}">Dashboard</a>')
    dashboard_link.short_description = 'Dashboard'

    # -------------------------------
    # Override changelist_view to show custom dashboard
    # -------------------------------
    def changelist_view(self, request, extra_context=None):
        from django.template.response import TemplateResponse

        new_reservations = Reservation.objects.filter(viewed=False).count()
        confirmed_reservations = Reservation.objects.filter(status=True).count()
        total_reservations = Reservation.objects.count()
        latest_reservations = Reservation.objects.order_by('-id')[:10]

        context = dict(
            self.admin_site.each_context(request),
            new_reservations=new_reservations,
            confirmed_reservations=confirmed_reservations,
            total_reservations=total_reservations,
            reservations=latest_reservations
        )
        return TemplateResponse(request, "admin/dashboard/index.html", context)


# =======================
# REGISTER CUSTOM ADMIN
# =======================
admin_site = DashboardAdmin(name='dashboard')

# Register your models
admin_site.register(Reservation, ReservationAdmin)

# Register auth models only for superuser
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin

admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
