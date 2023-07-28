# How-to Guide: Using Python String Manipulation Functions

In this how-to guide, you will learn how to use a collection of Python functions for string manipulation. These functions will help you capitalize words, convert strings to lowercase or uppercase, sort elements in a list, count word occurrences, and find and replace words in a string. Let's dive in!

## 1. `capitalize(input_string)`

- **Purpose:** Capitalizes the first character of each word in the input string.

**Example:**

```
# Step 1: Import the function from the module

   from string_manipulation import capitalize
   
# Step 2: Call the function with your input string

   input_string = "hello world"
   result = capitalize(input_string)
   
# Step 3: Print the result 

print(result)  # Output: 'Hello World'
```

## 2. `lowercase(input_string)`

- **Purpose:** Converts all characters in the input string to lowercase.

**Example:**


```
# Step 1: Import the function from the module
from string_manipulation import lowercase

# Step 2: Call the function with your input string
input_string = "ThIs Is a MiXeD CaSe StRiNg"
result = lowercase(input_string)

# Step 3: Print the result
print(result)  # Output: 'this is a mixed case string'

```
## 3. `uppercase(input_string)`

- **Purpose:** Converts all characters in the input string to uppercase.

**Example:**


```
# Step 1: Import the function from the module
from string_manipulation import uppercase

# Step 2: Call the function with your input string
input_string = "hello world"
result = uppercase(input_string)

# Step 3: Print the result
print(result)  # Output: 'HELLO WORLD'

```

## 4. `sort_list(word_list)`

- **Purpose:** Sorts the elements of the input list in ascending order.

**Example:**


```
# Step 1: Import the function from the module
from string_manipulation import sort_list

# Step 2: Call the function with your input list
word_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = sort_list(word_list)

# Step 3: Print the result
print(result)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

```

## 5. `count_word_occurrences(word_list, target_word)`

- **Purpose:** Counts the occurrences of a target word in the given word list.

**Example:**

```
# Step 1: Import the function from the module
from string_manipulation import count_word_occurrences

# Step 2: Call the function with your input word list and target word
word_list = ['apple', 'banana', 'orange', 'banana', 'kiwi']
target_word = 'banana'
result = count_word_occurrences(word_list, target_word)

# Step 3: Print the result
print(result)  # Output: 2

```

## 6. `find_and_replace(source_string, target_word, replacement_word)`

- **Purpose:** Finds all occurrences of the target word in the source string and replaces them with the replacement word.

**Example:**


```
# Step 1: Import the function from the module
from string_manipulation import find_and_replace

# Step 2: Call the function with your input source string, target word, and replacement word
source_string = "The quick brown fox jumps over the lazy dog."
target_word = "fox"
replacement_word = "cat"
result = find_and_replace(source_string, target_word, replacement_word)

# Step 3: Print the result
print(result)  # Output: 'The quick brown cat jumps over the lazy dog.'

```

Congratulations! You've learned how to use the Python String Manipulation Functions to perform various string manipulations. By incorporating these functions into your work, you can efficiently handle daunting text-related tasks. Happy writing!