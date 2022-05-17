import unittest
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(PROJECT_ROOT)

from machinetranslation.translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("Hello world"), "Bonjour le monde")
        self.assertEqual(english_to_french("This is a test"), "Il s'agit d'un test")
        with self.assertRaises(ValueError):
            english_to_french(None)

class TestFrenchToEnglish(unittest.TestCase):
    def test(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Bonjour le monde"), 'Hello World')
        self.assertEqual(french_to_english("Il s'agit d'un test"), 'This is a test')
        with self.assertRaises(ValueError):
            french_to_english(None)

unittest.main()
