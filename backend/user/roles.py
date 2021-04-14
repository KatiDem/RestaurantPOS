from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class SuperuserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    permission_denied_message = 'Только администраторы могут выполнять это действие'

    def test_func(self):
        return self.request.user.is_active and self.request.user.is_superuser


class WaiterRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    permission_denied_message = 'Только официанты могут выполнять это действие'

    def test_func(self):
        return self.request.user.is_active and self.request.user.is_waiter


class CookRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    permission_denied_message = 'Только повара могут выполнять это действие'

    def test_func(self):
        return self.request.user.is_active and self.request.user.is_cook
