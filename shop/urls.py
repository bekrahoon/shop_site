from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import IndexView, CategoryDetailView, ProductDetailView, SearchResultsView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "category/<int:category_id>/",
        CategoryDetailView.as_view(),
        name="category_detail",
    ),
    path(
        "product/<int:product_id>/", ProductDetailView.as_view(), name="product_detail"
    ),
    path("search/", SearchResultsView.as_view(), name="search_results"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
