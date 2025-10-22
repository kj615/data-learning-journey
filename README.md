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

10/17/2025
 Today I learned about Operators, Control Flow, and Functions.
 The first operator I learned are Arithmatic (-, +, %, //, etc), which can be used with both numbers and strings.
  Using + or * on numbers will perform math. Using these on strings will concatenate or repeat, respectively. 
 I also learned about Comparison, Logical, and Membership operators. ==, <, >; and, or, not; in, not in.

 Control Flow refers to If/Else statements as well as For and While Loops. 
  When using While Loops, you need to be careful to not get stuck in an endless loop. Typically these are used when conditions are changing or the loop is affected by code within the loop. 

 Finally, Functions. 
  Defining a function is releatively easy and can be defined for many things. 
   An example is 
     def multiply_by_3(val):
      return val * 3
   You can give multiple arguments by separating with a comma. If there is a defult value for an argument it can also be defined.
    A good example of this was in the Kaggle exercise where 3 friends pool their candy and agree to smash any remainders if not split evenly. You can use arguments to define the total_candy but also the total_friends should it not always be 3...but can default to 3.
     def to_smash(total_candies, total_friends=3):
      return total_candies % total_friends
    In this example, if you run to_smash(91) it would return the number of "extra" candies after deviding equally amongst 3 people. 
    If you run to_smash(91,4), it changes the number of friends to 4 and would now return the number of "extra" candies after diving equally amongst 4 people.
In additional to my learnings/videos, I completed the Kaggle exercise in the Python course for both functions and the intro Hello,Python which covered some basic syntax usage.

10/22/2025
Today's entry looks a bit different - it's more of "where have I been" than "what I learned today"
As I continued working through the Python Essentials LL course I became increasingly frustrated with the built-in coderPad challenges and the level of difficulty of said challenges. There were many concepts that well may have been talked about in the LL course, it was by no means enough to know how and where to correctly apply and even combine multiple of these concepts to solve a problem. Thus is the issue I see with this course so far. 

Today, I decided to pivot and take a stab at the course "Python for non coders" which covers many of the same concepts but in a more basic manner. I also am appreciating how this course has you pause and apply each basic concept on your own at the end of a video and then hit play and cover it together to ensure you have some understanding. While the first coderPad challenge was yet again a bit challenging, I was able to solve it in my own way...and then eventually get it to pass with a little correction caught in the solution video. I think the key here is that while I'm eager to learn and be able to apply Python knowledge, I also need to be able to understand what I'm learning and learn at a pace that makes sense for me so I don't just become frustrated and give up like I have so many times in the past. 

So, today, I guess I learned what I need to be able to stay consistent on this learning journey and it's just to slow down, take a step back so I can continue taking steps forward. And so...the journey continues :) Stay tuned.
