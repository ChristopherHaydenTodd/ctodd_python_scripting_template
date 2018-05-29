#!/usr/bin/env python3
"""
    Purpose:
        Template Class to Build on when building a Python
        Project

    Examples of Create Object of Class:
        class_template_object = ClassTemplate('some_param')
        class_template_object =\
            ClassTemplate('some_param', 'not_needed')
"""

class ClassTemplate(object):
    """
        ClassTemplate Class
    """

    def __init__(self, necessary_param, optional_param=None):
        """
        Purpose:
            Initilize the ClassTemplate Class.
        Args:
            fqdn (string): hostname or fqdn
        """

        self.property_a = necessary_param
        self.property_b = optional_param
        self.not_set_property = None

    # Some Static Method
    @staticmethod
    def some_static_method():
        """
            Stuf Static Method
        """

        # Do Something Without needed the class to be instantiated
        return None

    # Some Class Method
    def some_class_method():
        """
        Purpose:
            Initilize the ClassTemplate Class.
        Args:
            None
        Returns:
            property_b (string): value stored in self.property_b 
        """

        return self.property_b
