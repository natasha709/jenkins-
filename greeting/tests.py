"""Unit tests for greeting application views and functionality.

This module contains test cases that verify:
- HTTP response status codes
- Template rendering
- Context data
- View functionality
"""
from django.test import TestCase, Client
from django.urls import reverse


class GreetingTests(TestCase):
    """Test cases for the greeting page rendering and basic functionality."""

    def setUp(self):
        """Initialize test client before each test method."""
        self.client = Client()

    def test_index_page(self):
        """Verify the index page returns correct response and content.
        
        Tests:
        - Status code is 200 (OK)
        - Response contains 'Hello' text
        - Correct template is used (index.html)
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello')
        self.assertTemplateUsed(response, 'index.html')


class GreetingFunctionalityTests(TestCase):
    """Test cases for greeting view's business logic and context data."""

    def test_greeting_context(self):
        """Verify the greeting context data is correctly passed to template.
        
        Tests:
        - Context contains 'greeting' key
        - 'greeting' value equals 'Hello'
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.context['greeting'], 'Hello')