# Django
from django.contrib.auth.models import User
from django.test import TestCase

# Local Django
from .models import Impression


# Impression Creation Testing
class CreateImpressionTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(id=1)
        Impression.objects.create(
            owner_id=1,
            title="Верхняя Пышма",
            content="Манин Парк",
            address="Верхняя Пышма, Манин Парк",
            location="56.986634, 60.592123",
        )

    def test_title(self):
        impression = Impression.objects.get(pk=1)
        title = impression.title

        self.assertEqual(title, "Верхняя Пышма")

    def test_content(self):
        impression = Impression.objects.get(pk=1)
        content = impression.content

        self.assertEqual(content, "Манин Парк")

    def test_address(self):
        impression = Impression.objects.get(pk=1)
        address = impression.address

        self.assertEqual(address, "Верхняя Пышма, Манин Парк")

    def test_location(self):
        impression = Impression.objects.get(pk=1)
        location = impression.location

        self.assertEqual(location, "56.986634, 60.592123")

    def test_impression_owner(self):
        impression = Impression.objects.get(pk=1)
        impression_owner = impression.owner
        user = User.objects.get(pk=1)

        self.assertEquals(impression_owner, user)


# Testing getting a list of impressions
class GetImpressionListTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(id=1, username="user1")
        User.objects.create(id=2, username="user2")
        Impression.objects.create(
            owner_id=1,
            title="Верхняя Пышма",
            content="Манин Парк",
            address="Верхняя Пышма, Манин Парк",
            location="56.986634, 60.592123",
        )
        Impression.objects.create(
            owner_id=1,
            title="Верхняя Пышма",
            content="Парк УГМК",
            address="Верхняя Пышма, Парк УГМК",
            location="56.96",
        )
        Impression.objects.create(
            owner_id=2,
            title="Верхняя Пышма",
            content="Манин Парк",
            address="Верхняя Пышма, Манин Парк",
            location="56.986634, 60.592123",
        )

    def test_get_impression_list(self):
        user = User.objects.get(pk=1)
        impressions = Impression.objects.filter(owner=user)
        len_impressions_list = len(impressions)

        self.assertEqual(len_impressions_list, 2)
