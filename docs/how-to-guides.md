# How-to Guide: Using Python String Manipulation Functions

In this how-to guide, you will learn how to use a collection of Python functions for string manipulation. These functions will help you capitalize words, convert strings to lowercase or uppercase, sort elements in a list, count word occurrences, and find and replace words in a string. Let's dive in!

## 1. `capitalize(input_string)`

- **Purpose:** Capitalizes the first character of each word in the input string.

**Example:**

### Step 1: Import the function from the module
```
   from string_manipulation import capitalize
```
### Step 2: Call the function with your input string
```
   input_string = "hello world"
   result = capitalize(input_string)
```
### Step 3: Print the result
```
   print(result)  # Output: 'Hello World'
```
