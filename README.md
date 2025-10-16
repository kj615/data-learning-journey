# data-learning-journey

## My daily learning journey

10/14/2025
 - installed Python + jupyter notebooks
   - pip
     - pip install jupyterlabs
 - Jupyter shortcuts
   - running from cmd:
     - cd (drag exercise folder for directory) [enter]
     - jupyter lab
   - shift + enter
     - within box will run code
     - outside box will add new row
     - a will also add new row above
     - b will add new row below

10/15/2025
  - Variables & types
    - Variable names can't start with a number, can't include special characters other than underscore, start with lowercase letters.
    * type(variable) will give you the type of the variable

    - Numbers - int & float
    - String - using single quotes
      - concatenate: '1' + '1' will result in '11'
    - Boolean - True/False (using uppercase)
      - used in comparisons/statements such as 1 == 1 results in True
      
  - Data Structures
    - Lists [] brackets
      - order matters and is static
      - lists within lists is OK
      - function: length can show the length of list
        - len(list_name)
    - Sets {} curly brackets
      - order doesn't matter and isn't static
      - every element in set needs to be unique
      - can use len function
    - Tuples () parentheses
      - order matters and is static
      - can't append Tuples (can append lists)
      - saves memory because it's defined and can never increase in size
    - Dictionaries {} curly brackets
      - order doesn't matter
      - 'key': 'value' sets
      - each key needs to be unique or will overwrite old value for same key
      - call value from key: variable_name['key']
      - creating dictionary:
      -   variable = {
      -     'key1': 'definition',
      -     'key2': 'definition2'
      -   }
