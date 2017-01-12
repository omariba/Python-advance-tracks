#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The path to enlightenment starts with the following:

import unittest

from koans.about_how_the_lesson_works import AboutHowTheTrackWorks
from koans.about_expressions_and_statements import AboutExpressionsAndStatements
from koans.about_integer_operations import AboutIntegerOperations
from koans.about_multiples import AboutMultiples
from koans.about_prime_factor import AboutPrimeFactors
from koans.about_strings_count import AboutStringsCount
from koans.about_more_string_practice import AboutMoreStringPractice
from koans.about_even_more_about_strings import AboutEvenMoreStringPractice
from koans.about_portia import AboutPortia
from koans.about_dictionary_practice import AboutDictionaryPractice
from koans.about_email_dictionary_practice import AboutEmailDictionaryPractice
from koans.about_integral_number import AboutIntegralNumber
from koans.about_passwords import AboutPasswords
from koans.about_fibonnacci import AboutFibonnacci


def koans():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    loader.sortTestMethodsUsing = None
    suite.addTests(loader.loadTestsFromTestCase(AboutHowTheTrackWorks))
    suite.addTests(loader.loadTestsFromTestCase(AboutIntegerOperations))
    suite.addTests(loader.loadTestsFromTestCase(AboutMultiples))
    suite.addTests(loader.loadTestsFromTestCase(AboutPrimeFactors))
    suite.addTests(loader.loadTestsFromTestCase(AboutExpressionsAndStatements))
    suite.addTests(loader.loadTestsFromTestCase(AboutStringsCount))
    suite.addTests(loader.loadTestsFromTestCase(AboutMoreStringPractice))
    suite.addTests(loader.loadTestsFromTestCase(AboutEvenMoreStringPractice))
    suite.addTests(loader.loadTestsFromTestCase(AboutPortia))
    suite.addTests(loader.loadTestsFromTestCase(AboutDictionaryPractice))
    suite.addTests(loader.loadTestsFromTestCase(AboutEmailDictionaryPractice))
    suite.addTests(loader.loadTestsFromTestCase(AboutIntegralNumber))
    suite.addTests(loader.loadTestsFromTestCase(AboutPasswords))
    suite.addTests(loader.loadTestsFromTestCase(AboutFibonnacci))
    
    return suite
