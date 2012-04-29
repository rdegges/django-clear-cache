from time import sleep

from django.conf import settings
from django.core.cache import cache
from django.core.management import call_command
from django.test import TestCase


class ClearCache(TestCase):

    def test_caching_works_as_expected(self):
        self.assertFalse(cache.get('woot'))
        cache.set('woot', 'woot', 1)
        self.assertTrue(cache.get('woot'))
        sleep(1)
        self.assertFalse(cache.get('woot'))

    def test_clears_cache(self):
        cache.set('omg', 'omg', 1)
        self.assertTrue(cache.get('omg'))
        call_command('clear_cache')
        self.assertFalse(cache.get('omg'))

    def test_fails_if_no_cache_is_configured(self):
        settings.CACHES = {}
        self.assertRaises(AssertionError, call_command, 'clear_cache')
