from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Article



class ArticleTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.article = Article.objects.create(
            title = "A proper title for blog API",
            author = "Mayor Boxi",
            content = "A detailed content",
            tag = "blog_post"
        )
        
    def test_created_article_content(self):
        self.assertEqual(self.article.title, "A proper title for blog API")
        self.assertEqual(self.article.author, "Mayor Boxi")
        self.assertEqual(self.article.content, "A detailed content")
        self.assertEqual(self.article.tag, "blog_post")


    def test_api_article_list(self):
        response = self.client.get(reverse("article_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Article.objects.count(), 1)
        self.assertContains(response, self.article)

    def test_api_article_detail(self):
        response = self.client.get(reverse("article_detail", kwargs={"pk": self.article.id}), 
                                   format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Article.objects.count(), 1)
        self.assertContains(response, "Mayor Boxi")


    def test_api_article_create(self):
        url = reverse("article_create")
        data = {
            "title": "New Article Title",
            "author": "New Author",
            "content": "New Content",
            "tag": "new-tag"
            }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['author'], data['author'])
        self.assertEqual(response.data['content'], data['content'])
        self.assertEqual(response.data['tag'], data['tag'])
        
        

    

    def test_api_update(self):
        url = reverse("article_update", kwargs={"pk": self.article.id})
        data = {
            'title': 'updated title',
            "author": "Mayor Lee",
            "content" : "Updating old title",
            "tag": "updated tag",
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['author'], data['author'])
        self.assertEqual(response.data['content'], data['content'])
        self.assertEqual(response.data['tag'], data['tag'])
        
        

    def test_api_article_delete(self):
        response = self.client.delete(reverse("article_delete", kwargs={"pk": self.article.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Article.objects.count(), 0)
        