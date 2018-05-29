#!/usr/bin/python3 -u
"""
    Purpose:
        Test File Can be used as a basis for unittesting classes
        and other Python constructs

    Example call:
        python3 -m pytest test_template.py
"""

import os
from datetime import datetime
import inspect
import pytz
import pytest

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture
def class_template():
    """
        Returns a Remedy object that can be used in tests
    """
    from classes.class_template import ClassTemplate
    return ClassTemplate('necessary_param')


def test_check_class_template_properties_exist(class_template):
    """
        Ensure all expected properties exist within
        the class
    """

    expected_properties = [
        'property_a',
        'property_b',
        # 'propety_that_doesnt_exist', # Uncomment to Fail Test
        'not_set_property',
    ]

    attributes = class_template.__dict__

    for attribute in expected_properties:
        assert (attribute in attributes)


def test_check_class_template_properties_initiated_properly(class_template):
    """
        Ensure all expected properties are set with the correct
        value as expected
    """

    expected_property_values = {
        'property_a': 'necessary_param',
        'property_b': None,
        # 'property_b': 'Somethign It Doesnt Equal', # Uncomment to Fail Test
        'not_set_property': None,
    }

    attributes = class_template.__dict__

    for attribute, value in expected_property_values.items():
        assert (value == getattr(class_template, attribute))


def test_check_class_template_methods_exist(class_template):
    """
        Ensure all expected methods exist within
        the class
    """

    expected_methods = [
        'some_class_method',
        # 'some_class_method_not_existing', # Uncomment to Fail Test
    ]

    class_methods_info = inspect.getmembers(
        class_template,
        predicate=inspect.ismethod
    )

    class_methods =\
        [info_point[0] for info_point in class_methods_info]

    for method in expected_methods:
        assert (method in class_methods)
