from django.urls import path

from .views import (ArticleList, ArticleDetail, ArticleDelete, 
                    ArticleCreate, ArticleUpdate)




urlpatterns = [
    path("", ArticleList.as_view(), name="article_list"),
    path("<int:pk>", ArticleDetail.as_view(), name="article_detail"),
    path("update/<int:pk>/", ArticleUpdate.as_view(), name="article_update"),
    path("delete/<int:pk>/", ArticleDelete.as_view(), name="article_delete"),
    path("create", ArticleCreate.as_view(), name="article_create"),
]