from django.urls import path

from .views import (
    ProductListView,
    ProductCreateView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
)


app_name = "showcase_app"

urlpatterns = [
    path("products/", ProductListView.as_view(), name="index"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product"),
    # path('product/<int:pk>/',CommentSubmit.as_view(),name='post_comment'),
    path("product/create/", ProductCreateView.as_view(), name="create-product"),
    path(
        "product/<int:pk>/update/", ProductUpdateView.as_view(), name="update-product"
    ),
    path(
        "products/<int:pk>/delete/", ProductDeleteView.as_view(), name="delete-product"
    ),
]
