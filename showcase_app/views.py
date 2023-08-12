from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from pathlib import Path
import os

from django.views.generic.edit import FormMixin

from .models import Product, Question, Answer
from .forms import ProductForm, QuestionForm, AnswerForm
from massive_homework.settings import BASE_DIR

# Create your views here.

### PRODUCTS VIEWS ###


class ProductListView(ListView):
    queryset = Product.objects.all()


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("showcase_app:index")


class ProductDetailView(FormMixin, DetailView):
    model = Product
    path_input_image = Product.images
    path_input_image_abs = f"{BASE_DIR}/{path_input_image}"
    form_class = QuestionForm

    def get_context_data(self, **kwargs):
        question = Question.objects.filter(
            ~Q(archived=True), product_id=self.get_object()
        ).order_by("created_at")
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context["form"] = QuestionForm(initial={"product": self.object})
        context["question"] = question
        return context

    def post(self, request, *args, **kwargs):
        new_question = Question(
            header=request.POST.get("header"),
            body=request.POST.get("body"),
            product_id=self.get_object(),
        )
        new_question.save()
        return self.get(self, request, *args, **kwargs)


class ProductUpdateView(UpdateView):
    template_name_suffix = "_update_form"
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse("showcase_app:product", kwargs={"pk": self.object.pk})


class ProductDeleteView(DeleteView):
    success_url = reverse_lazy("showcase_app:index")
    queryset = Product.objects.filter(~Q(archived=True)).all()


### QUESTION VIEWS ###


class QuestionDetailView(FormMixin, DetailView):
    model = Question
    form_class = AnswerForm

    def get_context_data(self, **kwargs):
        answer = Answer.objects.filter(question_id=self.get_object()).order_by("id")
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        context["form"] = AnswerForm(initial={"question": self.object})
        context["answer"] = answer
        return context

    def post(self, request, *args, **kwargs):
        new_answer = Answer(
            body=request.POST.get("body"),
            question_id=self.get_object().id,
        )
        new_answer.save()
        return self.get(self, request, *args, **kwargs)


class QuestionDeleteView(DeleteView):
    queryset = Question.objects.filter(~Q(archived=True)).all()

    def get_success_url(self):
        return reverse("showcase_app:product", kwargs={"pk": self.object.product.pk})


class QuestionListView(ListView):
    model = Question

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(product_id=self.kwargs["pk"])


class AnswerDeleteView(DeleteView):
    queryset = Answer.objects.filter(~Q(archived=True)).all()

    def get_success_url(self):
        return reverse("showcase_app:question", kwargs={"pk": self.object.question.pk})
