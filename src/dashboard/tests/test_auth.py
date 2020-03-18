# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import json

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from tastypie.models import ApiKey

from components import helpers
from components.administration import views as admin_views
from components.api import views as api_views
from components.helpers import generate_api_key
from components.ingest.views import ingest_grid as ingest_grid_view
from components.transfer.views import grid as transfer_grid_view


class TestAuth(TestCase):
    """Authentication sanity checks."""

    fixtures = ["test_user"]

    API_URLS = (
        reverse(api_views.completed_transfers),
        reverse(api_views.completed_ingests),
        reverse(api_views.get_levels_of_description),
    )

    def setUp(self):
        helpers.set_setting("dashboard_uuid", "test-uuid")

    def authenticate(self):
        self.client = Client()
        self.client.login(username="test", password="test")

    def test_site_requires_auth(self):
        for url in [
            reverse(transfer_grid_view),
            reverse(ingest_grid_view),
            reverse(admin_views.api),
            reverse(admin_views.general),
            reverse(admin_views.premis_agent),
            # Verify that exempted URLs cannot be used to access other areas
            # that are restricted.
            "{}/{}".format(settings.LOGIN_URL.rstrip("/"), "transfer/"),
            "{}/{}".format(settings.LOGIN_URL.rstrip("/"), "abcdefgh/api/"),
            "{}/{}".format(settings.LOGIN_URL.rstrip("/"), "version"),
        ]:
            response = self.client.get(url)

            self.assertRedirects(response, settings.LOGIN_URL)

    def test_site_performs_session_auth(self):
        self.authenticate()

        for url in [
            reverse(transfer_grid_view),
            reverse(ingest_grid_view),
            reverse(admin_views.api),
        ]:
            response = self.client.get(url, follow=False)

            self.assertEqual(response.status_code, 200)

    def test_api_requires_auth(self):
        for url in self.API_URLS:
            response = self.client.get(url)

            self.assertEqual(response.status_code, 403)
            self.assertEqual(
                response.content,
                json.dumps({"message": "API key not valid.", "error": True}),
            )

    def test_api_authenticates_via_key(self):
        user = get_user_model().objects.get(pk=1)
        generate_api_key(user)
        key = ApiKey.objects.get(user=user).key

        for url in self.API_URLS:
            response = self.client.get(
                url, HTTP_AUTHORIZATION="ApiKey test:{}".format(key), follow=False
            )

            self.assertEqual(response.status_code, 200)

    def test_api_authenticates_via_session(self):
        self.authenticate()

        for url in self.API_URLS:
            response = self.client.get(url, follow=False)

            self.assertEqual(response.status_code, 200)
