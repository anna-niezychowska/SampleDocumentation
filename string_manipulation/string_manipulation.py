"""
String Manipulation Module

This module provides a set of functions for manipulating strings. The functions
allow users to capitalize or convert strings to lowercase/uppercase, sort elements
in a list, count occurrences of a word in a list, and find and replace words in a
source string.

Functions:

    * capitalize(input_string): Capitalizes the first character of each word in the input string.
    * lowercase(input_string): Converts all characters in the input string to lowercase.
    * uppercase(input_string): Converts all characters in the input string to uppercase.
    * sort_list(word_list): Sorts the elements of the input list in ascending order.
    * count_word_occurrences(word_list, target_word): Counts the occurrences of a target word in the given word list.
    * find_and_replace(source_string, target_word, replacement_word): Finds all occurrences of the target word in the source string and replaces them with the replacement word.


Each function comes with detailed docstrings explaining their purpose, arguments, return
values, and examples of usage. Users can leverage this module to perform various string
manipulations efficiently.
"""

def capitalize(input_string):
    """Capitalizes the first character of each word in the input string.

    This function uses the title() method to capitalize the first character
    of each word in the input string, while converting the rest of the characters
    to lowercase. Words are identified by whitespace.

    Args:
        input_string (str): The input string to be capitalized.

    Returns:
        str: A new string with the first character of each word capitalized
        and the rest of the characters converted to lowercase.

    Examples:
       >>> capitalize("hello world")
        'Hello World'
       >>> capitalize("the quick BROWN fox")
        'The Quick Brown Fox'
    """

    return input_string.title()


def lowercase(input_string):
    """
    Converts all characters in the input string to lowercase.

    This function uses the lower() method to convert all characters in the
    input string to lowercase. Any uppercase characters present in the
    input string will be converted to their lowercase equivalents.

    Args:
        input_string (str): The input string to be converted to lowercase.

    Returns:
        str: A new string with all characters converted to lowercase.

    Examples:
       >>> lowercase("Hello World")
        'hello world'

       >>> lowercase("ThIs Is a MiXeD CaSe StRiNg")
        'this is a mixed case string'
    """
    return input_string.lower()


def uppercase(input_string):
    """
    Converts all characters in the input string to uppercase.

    This function uses the upper() method to convert all characters in the
    input string to uppercase. Any lowercase characters present in the
    input string will be converted to their uppercase equivalents.

    Args:
        input_string (str): The input string to be converted to uppercase.

    Returns:
        str: A new string with all characters converted to uppercase.

    Examples:
       >>> uppercase("hello world")
        'HELLO WORLD'
       >>> uppercase("ThIs Is a MiXeD CaSe StRiNg")
        'THIS IS A MIXED CASE STRING'
    """
    return input_string.upper()


def sort_list(word_list):
    """
    Sorts the elements of the input list in ascending order.

    This function uses the sorted() function to sort the elements of the
    input list in ascending order. The elements of the list must be
    comparable to each other for sorting to work correctly.

    Args:
        word_list (list): The list of elements to be sorted.

    Returns:
        list: A new list with the elements sorted in ascending order.

    Examples:
       >>> sort_list([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

       >>> sort_list(['banana', 'apple', 'orange', 'grape', 'kiwi'])
        ['apple', 'banana', 'grape', 'kiwi', 'orange']
    """
    return sorted(word_list)


def count_word_occurrences(word_list, target_word):
    """
    Counts the occurrences of a target word in the given word list.

    This function iterates through the elements of the input word_list and
    counts the number of occurrences of the target_word.

    Args:
        word_list (list): The list of words to search for occurrences.
        target_word (str): The word to be counted in the word_list.

    Returns:
        int: The number of occurrences of the target_word in the word_list.

    Examples:
       >>> count_word_occurrences(['apple', 'banana', 'orange', 'banana', 'kiwi'], 'banana')
        2

       >>> count_word_occurrences(['hello', 'world', 'hello', 'world', 'hello'], 'world')
        2

       >>> count_word_occurrences(['apple', 'banana', 'orange'], 'kiwi')
        0
    """
    word_count = 0
    for word in word_list:
        if word == target_word:
            word_count += 1
    return word_count


def find_and_replace(source_string, target_word, replacement_word):
    """
    Finds all occurrences of the target word in the source string and replaces them with the replacement word.

    This function uses the replace() method of the source string to find all occurrences
    of the target_word and replaces them with the replacement_word.

    Args:
        source_string (str): The original string to perform the replacement on.
        target_word (str): The word to be replaced in the source string.
        replacement_word (str): The word to replace the target_word with.

    Returns:
        str: A new string with all occurrences of the target word replaced with the replacement word.

    Examples:
       >>> find_and_replace("The quick brown fox jumps over the lazy dog.", "fox", "cat")
        'The quick brown cat jumps over the lazy dog.'

       >>> find_and_replace("She sells seashells by the seashore.", "seashells", "pearls")
        'She sells pearls by the seashore.'

       >>> find_and_replace("Hello, Hello, Hello!", "Hello", "Hi")
        'Hi, Hi, Hi!'
    """
    return source_string.replace(target_word, replacement_word)
