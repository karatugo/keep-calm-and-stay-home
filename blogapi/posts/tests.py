from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post


class BlogTests(TestCase):
    username = 'testuser1'
    password = 'abc123'
    title = 'Blog title'
    body = 'Body content...'

    @classmethod
    def setUpTestData(cls):
        create_test_user()
        create_test_post()
        
        testuser1 = User.objects.create_user(
            username=BlogTests.username, password=BlogTests.password)
        testuser1.save()

        test_post = Post.objects.create(
            author=testuser1, title=BlogTests.title, body=BlogTests.body)
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, BlogTests.username)
        self.assertEqual(title, BlogTests.title)
        self.assertEqual(body, BlogTests.body)
