# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, TemplateView
from django.shortcuts import render
# Local Django
from .forms import CreateImpressionForm
from .models import Impression
from .utils import DataMixin


class MainPageView(DataMixin, TemplateView):
    template_name = "PR/main_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная страница"
        context_mixin = self.get_user_context()
        context = dict(list(context.items()) + list(context_mixin.items()))
        return context


class PageStorageView(LoginRequiredMixin, DataMixin, ListView):
    model = Impression
    template_name = "PR/stoargepage.html"
    context_object_name = "imps"
    login_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Хранилище"
        context_mixin = self.get_user_context()
        context = dict(list(context.items()) + list(context_mixin.items()))
        return context

    def get_queryset(self):
        request_user = self.request.user
        return Impression.objects.filter(owner=request_user)


class AddImpressionView(LoginRequiredMixin, DataMixin, CreateView):
    form_class = CreateImpressionForm
    template_name = "PR/create_impres.html"
    success_url = "/storage/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Добавить впечатление"
        context_mixin = self.get_user_context()
        context = dict(list(context.items()) + list(context_mixin.items()))
        return context

    def form_valid(self, form):
        request_user = self.request.user
        form.instance.owner = request_user
        return super().form_valid(form)

