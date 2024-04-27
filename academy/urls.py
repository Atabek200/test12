from django.urls import path
from .views import ProductImageView, CommentView, RatingView, MyModelSet

urlpatterns = [
    path('product-images/', ProductImageView.as_view(), name='product-images'),
    path('comments/', CommentView.as_view(), name='comments'),
    path('ratings/', RatingView.as_view(), name='ratings'),
    path('MyModel/', MyModelSet.as_view(), name='MyMode'),
]