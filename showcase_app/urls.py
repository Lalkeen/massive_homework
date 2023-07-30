from django.urls import path

from .views import (
    ProductListView,
    ProductCreateView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
    QuestionDetailView,
    QuestionDeleteView,
    QuestionListView,
)


app_name = "showcase_app"

urlpatterns = [
    path("products/", ProductListView.as_view(), name="index"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product"),
    path("product/create/", ProductCreateView.as_view(), name="create-product"),
    path(
        "product/<int:pk>/update/", ProductUpdateView.as_view(), name="update-product"
    ),
    path(
        "product/<int:pk>/delete/", ProductDeleteView.as_view(), name="delete-product"
    ),
    path("question/<int:pk>", QuestionDetailView.as_view(), name="question"),
    path(
        "question/<int:pk>/delete/",
        QuestionDeleteView.as_view(),
        name="delete-question",
    ),
    path(
        "product/<int:pk>/questions", QuestionListView.as_view(), name="question-list"
    ),
]
