# -*- coding: utf-8 -*-
#
# Copyright (C) Bitergia
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import pytest

from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse


@pytest.fixture
def api_client():
    """Fixture for the API client."""

    client = Client()
    get_user_model().objects.create_user(username='testuser', password='testpassword')
    client.login(username='testuser', password='testpassword')
    return client


@pytest.mark.django_db
class TestTrustableScore:
    """Unit tests for the trustable_score view."""

    def test_trustable_score_not_found(self, api_client):
        """Test that the trustable_score view returns 404 for invalid IDs."""

        url = reverse('trustable_score', args=[1, 1])
        response = api_client.get(url)

        assert response.status_code == 404
        assert response.json() == {"error": "Not Found"}
