#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

__ = False


class AboutStrings(unittest.TestCase):

    # Equivalent ways of creating string objects

    # These are also referred to as string literals
    # as they are literally short cuts for:
    # >>> str('a string')
    # 'a string'

    def test_double_quoted_strings_are_strings(self):

        string = "Hello, world."

        assert isinstance(__, str)

    def test_single_quoted_strings_are_also_strings(self):

        string = 'Goodbye, world.'

        assert isinstance(__, str)

    def test_use_single_quotes_to_create_string_with_double_quotes(self):

        string = 'He said, "Go Away."'

        assert __ == string

    def test_use_double_quotes_to_create_strings_with_single_quotes(self):

        string = "Don't"

        assert __ == string

    # String methods and operations

    def test_plus_concatenates_strings(self):

        string = "Hello, " + "world"

        assert __ == string

    def test_plus_will_not_modify_original_strings(self):

        hi = "Hello, "
        there = "world"
        string = hi + there

        assert __ == hi
        assert __ == there
        assert __ == string

    def test_plus_equals_will_append_to_end_of_string(self):

        hi = "Hello, "
        there = "world"
        hi += there

        assert __ == hi

    def test_len_returns_length_of_string(self):

        hi = "hi"

        assert __ == len(hi)
