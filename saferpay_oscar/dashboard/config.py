from django.utils.translation import ugettext_lazy as _
from oscar.core.application import OscarConfig


class SaferpayDashboardConfig(OscarConfig):
    label = 'saferpay_oscar'
    name = 'saferpay_oscar.dashboard'
    verbose_name = _('Saferpay dashboard')
