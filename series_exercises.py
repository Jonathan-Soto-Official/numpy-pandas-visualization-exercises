exercises part 1
Use pandas to create a Series named fruits from the following list:
["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

In [1]:
import pandas as pd
In [2]:
my_list = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
In [5]:
type(my_list)
Out[5]:
list
In [6]:
# referencing the library pandas via the pd call, casting the data type interpreted as a list into a Series
fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])
In [7]:
type(fruits)
Out[7]:
pandas.core.series.Series
Use Series attributes and methods to explore your fruits Series.
Determine the number of elements in fruits.
In [8]:
len(my_list)
Out[8]:
17
In [9]:
len(fruits)
Out[9]:
17
In [10]:
fruits.size
Out[10]:
17
In [11]:
fruits.shape
Out[11]:
(17,)
Output only the index from fruits.
In [14]:
fruits
Out[14]:
0                 kiwi
1                mango
2           strawberry
3            pineapple
4           gala apple
5     honeycrisp apple
6               tomato
7           watermelon
8             honeydew
9                 kiwi
10                kiwi
11                kiwi
12               mango
13           blueberry
14          blackberry
15          gooseberry
16              papaya
dtype: object
In [20]:
# if we want the index, do what it says on the tin:
# fruits.index will display a range object, if I want to turn that into something more legible,
# then we can just cast it into a python list
list(fruits.index)
Out[20]:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
In [21]:
# what casting a range as a list looks like: list(range(0,17))
Output only the values from fruits.
In [25]:
fruits.values
Out[25]:
array(['kiwi', 'mango', 'strawberry', 'pineapple', 'gala apple',
       'honeycrisp apple', 'tomato', 'watermelon', 'honeydew', 'kiwi',
       'kiwi', 'kiwi', 'mango', 'blueberry', 'blackberry', 'gooseberry',
       'papaya'], dtype=object)
In [23]:
len(fruits.values)
Out[23]:
17
Confirm the data type of the values in fruits.
In [28]:
fruits.dtype
Out[28]:
dtype('O')
Output only the first five values from fruits. Output the last three values. Output two random values from fruits.
In [ ]:
 
In [30]:
# if I want the docstring output,
# use a function call but instead of using parenthesis, replace with a ? symbol
pd.Series.head?
Signature: pd.Series.head(self: 'FrameOrSeries', n: 'int' = 5) -> 'FrameOrSeries'
Docstring:
Return the first `n` rows.

This function returns the first `n` rows for the object based
on position. It is useful for quickly testing if your object
has the right type of data in it.

For negative values of `n`, this function returns all rows except
the last `n` rows, equivalent to ``df[:-n]``.

Parameters
----------
n : int, default 5
    Number of rows to select.

Returns
-------
same type as caller
    The first `n` rows of the caller object.

See Also
--------
DataFrame.tail: Returns the last `n` rows.

Examples
--------
>>> df = pd.DataFrame({'animal': ['alligator', 'bee', 'falcon', 'lion',
...                    'monkey', 'parrot', 'shark', 'whale', 'zebra']})
>>> df
      animal
0  alligator
1        bee
2     falcon
3       lion
4     monkey
5     parrot
6      shark
7      whale
8      zebra

Viewing the first 5 lines

>>> df.head()
      animal
0  alligator
1        bee
2     falcon
3       lion
4     monkey

Viewing the first `n` lines (three in this case)

>>> df.head(3)
      animal
0  alligator
1        bee
2     falcon

For negative values of `n`

>>> df.head(-3)
      animal
0  alligator
1        bee
2     falcon
3       lion
4     monkey
5     parrot
File:      /opt/homebrew/anaconda3/envs/homebase/lib/python3.9/site-packages/pandas/core/generic.py
Type:      function
In [29]:
fruits.head()
Out[29]:
0          kiwi
1         mango
2    strawberry
3     pineapple
4    gala apple
dtype: object
In [31]:
len?
Signature: len(obj, /)
Docstring: Return the number of items in a container.
Type:      builtin_function_or_method
In [33]:
len([1,2,3])
Out[33]:
3
In [35]:
capitalize('hello')
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-35-f83428c0b56c> in <module>
----> 1 capitalize('hello')

NameError: name 'capitalize' is not defined
In [36]:
str.capitalize?
Signature: str.capitalize(self, /)
Docstring:
Return a capitalized version of the string.

More specifically, make the first character have upper case and the rest lower
case.
Type:      method_descriptor
In [32]:
'hello'.capitalize()
Out[32]:
'Hello'
In [38]:
fruits.tail(3)
Out[38]:
14    blackberry
15    gooseberry
16        papaya
dtype: object
In [39]:
# sample will be great for you in the future as you utilize more beefy data sets.
# sample will allow us to get a random subset of our information that we can plot and render more easily 
# once we examine the various data visualization libraries
fruits.sample(2)
Out[39]:
4     gala apple
14    blackberry
dtype: object
Run the .describe() on fruits to see what information it returns when called on a Series with string values.
In [40]:
# examining the describe on a Series is beholden to the data type of the elements inside of
# the Series itself! We will observe different stats for continuous numerical information
fruits.describe()
Out[40]:
count       17
unique      13
top       kiwi
freq         4
dtype: object
Run the code necessary to produce only the unique string values from fruits.
In [44]:
#  we can use set casting on the values, ooooor: set(fruits.values)
In [45]:
fruits.unique()
Out[45]:
array(['kiwi', 'mango', 'strawberry', 'pineapple', 'gala apple',
       'honeycrisp apple', 'tomato', 'watermelon', 'honeydew',
       'blueberry', 'blackberry', 'gooseberry', 'papaya'], dtype=object)
Determine how many times each unique string value occurs in fruits.
In [46]:
fruits.nunique()
Out[46]:
13
Determine the string value that occurs most frequently in fruits.
In [47]:
fruits.value_counts()
Out[47]:
kiwi                4
mango               2
pineapple           1
honeycrisp apple    1
watermelon          1
blueberry           1
strawberry          1
blackberry          1
gooseberry          1
gala apple          1
honeydew            1
tomato              1
papaya              1
dtype: int64
In [54]:
# value_counts() will output a new pandas Series
# the content (values) of this value counts series is now  the number of times an element pops up,
# and the index is the original thing that it was counting from our origin series
# (in this case, value_counts gives us a Series of string literal indexes associated with integer values)
fruits.value_counts().head(1)
Out[54]:
kiwi    4
dtype: int64
Determine the string value that occurs least frequently in fruits.
In [57]:
fruits.value_counts().tail(1)
Out[57]:
papaya    1
dtype: int64
In [73]:
fruits.value_counts().nsmallest(keep='all')
Out[73]:
pineapple           1
honeycrisp apple    1
watermelon          1
blueberry           1
strawberry          1
blackberry          1
gooseberry          1
gala apple          1
honeydew            1
tomato              1
papaya              1
dtype: int64
exercises part 2
Explore more attributes and methods while you continue to work with the fruits Series.
Capitalize all the string values in fruits.
In [74]:
'mango'.capitalize()
Out[74]:
'Mango'
In [76]:
# we can tell pandas to use a string method on its values by specifying what data type object's
# method that we want to utilize:
fruits.str.capitalize()
Out[76]:
0                 Kiwi
1                Mango
2           Strawberry
3            Pineapple
4           Gala apple
5     Honeycrisp apple
6               Tomato
7           Watermelon
8             Honeydew
9                 Kiwi
10                Kiwi
11                Kiwi
12               Mango
13           Blueberry
14          Blackberry
15          Gooseberry
16              Papaya
dtype: object
Count the letter "a" in all the string values (use string vectorization).
In [77]:
# we know that we have a count method call beholden to the String object type in Python,
# lets use that on our Series
'banana'.count('a')
Out[77]:
3
In [78]:
str.count?
Docstring:
S.count(sub[, start[, end]]) -> int

Return the number of non-overlapping occurrences of substring sub in
string S[start:end].  Optional arguments start and end are
interpreted as in slice notation.
Type:      method_descriptor
In [80]:
# use that string method:
fruits.str.count('a').head(5)
Out[80]:
0    0
1    1
2    1
3    1
4    3
dtype: int64
In [83]:
# here we use an apply with a lambda function:
# the lambda function is taking in the value x from the Series' cell,
# outputting that value, concatenating it with a hardcoded string literal, and then concatenating
# those values with the string-cast version of the count of the letter a
fruits.apply(lambda x: x + ' count of a: ' + str(x.count('a')))
Out[83]:
0                 kiwi count of a: 0
1                mango count of a: 1
2           strawberry count of a: 1
3            pineapple count of a: 1
4           gala apple count of a: 3
5     honeycrisp apple count of a: 1
6               tomato count of a: 1
7           watermelon count of a: 1
8             honeydew count of a: 0
9                 kiwi count of a: 0
10                kiwi count of a: 0
11                kiwi count of a: 0
12               mango count of a: 1
13           blueberry count of a: 0
14          blackberry count of a: 1
15          gooseberry count of a: 0
16              papaya count of a: 3
dtype: object
Output the number of vowels in each and every string value.
In [84]:
# define vowels
vowels = ['a', 'e', 'i', 'o', 'u']
In [85]:
fruit = 'persimmon'
In [88]:
vowel_count = 0
for let in fruit.lower():
    if let in vowels:
        vowel_count += 1
In [89]:
vowel_count
Out[89]:
3
In [93]:
# every letter inside of our fruit variable, but only if it falls in our defined list
# of vowels that we establish
# then take the length of that thing
len([let for let in fruit.lower() if let in ['a', 'e', 'i', 'o', 'u']])
Out[93]:
3
In [96]:
# lets repeat that with list comprehension as well as putting it into a function:
def count_vowels(some_word):
    return len([let for let in some_word.lower() if let in ['a', 'e', 'i', 'o', 'u']])
In [97]:
count_vowels('grape')
Out[97]:
2
In [98]:
fruits.apply(count_vowels)
Out[98]:
0     2
1     2
2     2
3     4
4     4
5     5
6     3
7     4
8     3
9     2
10    2
11    2
12    2
13    3
14    2
15    4
16    3
dtype: int64
Write the code to get the longest string value from fruits.
In [108]:
# get all the lengths of strings from our fruits
# fruits.str.len()
# get the biggest of those:
# fruits.str.len().max()
# use that for comparison to get a boolean:
bool_mask = fruits.str.len() == fruits.str.len().max()
# think about the use of square brackets as the english word "where"
fruits[bool_mask]
Out[108]:
5    honeycrisp apple
dtype: object
In [109]:
bool_mask = fruits.str.len().max()
In [110]:
bool_mask
Out[110]:
16
In [114]:
# fruits where fruit 16
fruits[16]
Out[114]:
'papaya'
Write the code to get the string values with 5 or more letters in the name.
In [115]:
# let's make a new comparison for our string lengths:
# examining str.len() values that are >= 5:
# instead of ==.max(), >= 5:
# fruits, where fruits' string value length is five or more characters:
fruits[fruits.str.len() >= 5]
Out[115]:
1                mango
2           strawberry
3            pineapple
4           gala apple
5     honeycrisp apple
6               tomato
7           watermelon
8             honeydew
12               mango
13           blueberry
14          blackberry
15          gooseberry
16              papaya
dtype: object
Find the fruit(s) containing the letter "o" two or more times.
In [117]:
# let's just use a different string method here:
# instead of len(), we can use count()
# fruits, where fruits string count of the character o is 2 or greater
# if I want to use two string methods, make sure you specify .str ahead of each invocation
fruits[fruits.str.lower().str.count('o') >= 2]
Out[117]:
6         tomato
15    gooseberry
dtype: object
Write the code to get only the string values containing the substring "berry".
In [121]:
'berry' in 'banana'
Out[121]:
False
In [123]:
# fruits, where
# fruits.apply: 'berry' is a substring inside of the fed-in value of x
fruits[fruits.apply(lambda x: 'berry' in x)]
Out[123]:
2     strawberry
13     blueberry
14    blackberry
15    gooseberry
dtype: object
Write the code to get only the string values containing the substring "apple".
In [125]:
'blueberry'.contains('berry')
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-125-91724ae1fc97> in <module>
----> 1 'blueberry'.contains('berry')

AttributeError: 'str' object has no attribute 'contains'
In [124]:
fruits.str.contains('berry')
Out[124]:
0     False
1     False
2      True
3     False
4     False
5     False
6     False
7     False
8     False
9     False
10    False
11    False
12    False
13     True
14     True
15     True
16    False
dtype: bool
In [127]:
bool_mask = fruits.str.contains('apple')
fruits[bool_mask]
Out[127]:
3           pineapple
4          gala apple
5    honeycrisp apple
dtype: object
Which string value contains the most vowels?
In [135]:
# establish a new boolean mask that compares our pre-established vowel count to the max version
new_mask_who_dis = fruits.apply(count_vowels) == fruits.apply(count_vowels).max()
In [136]:
fruits[new_mask_who_dis]
Out[136]:
5    honeycrisp apple
dtype: object
In [132]:
fruits.apply(count_vowels).max()
Out[132]:
5
exercises part III
Use pandas to create a Series named letters from the following string. The easiest way to make this string into a Pandas series is to use list to convert each individual letter into a single string on a basic Python list.

'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
In [138]:
letters = 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
In [141]:
# we can cast a string literal into a list, and then cast that list into a Series
# list(letters)
In [143]:
letters = pd.Series(list(letters))
Which letter occurs the most frequently in the letters Series?
In [152]:
letters.value_counts().max()
Out[152]:
13
In [151]:
# idxmax will give us the index associated with 
letters.value_counts().idxmax()
Out[151]:
'y'
In [145]:
letters.value_counts().head(1)
Out[145]:
y    13
dtype: int64
Which letter occurs the Least frequently?
In [148]:
letters.value_counts().nsmallest(n=1,keep='all')
Out[148]:
l    4
dtype: int64
How many vowels are in the Series?
In [153]:
def is_vowel(some_word):
    return some_word in ['a', 'e', 'i', 'o', 'u']
In [155]:
is_vowel('w')
Out[155]:
False
In [157]:
letters.str.lower().apply(is_vowel).sum()
Out[157]:
34
In [ ]:
 
How many consonants are in the Series?
In [161]:
# using some logical statements will trip up pandas
not letters.str.lower().apply(is_vowel)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-161-427f8af8ee8f> in <module>
      1 # using some logical statements will trip up pandas
----> 2 not letters.str.lower().apply(is_vowel)

/opt/homebrew/anaconda3/envs/homebase/lib/python3.9/site-packages/pandas/core/generic.py in __nonzero__(self)
   1440     @final
   1441     def __nonzero__(self):
-> 1442         raise ValueError(
   1443             f"The truth value of a {type(self).__name__} is ambiguous. "
   1444             "Use a.empty, a.bool(), a.item(), a.any() or a.all()."

ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
In [164]:
# looking at square brackets being "where" statements, this gets useful
# you may use & for 'and' and | for 'or' in comparisons of two Series (hint for later down the line)
In [163]:
# apply the idea of 'not' to every instance in the Series output by my vowel check
(~letters.str.lower().apply(is_vowel)).sum()
Out[163]:
166
Create a Series that has all of the same letters but uppercased.
In [165]:
# use a differenter string method on it
letters.str.upper()
Out[165]:
0      H
1      N
2      V
3      I
4      D
      ..
195    R
196    O
197    G
198    U
199    Y
Length: 200, dtype: object
Create a bar plot of the frequencies of the 6 most commonly occuring letters.
In [171]:
import matplotlib.pyplot as plt
In [172]:
letters.value_counts().head(6).plot(kind='barh')
plt.title('top six all time letters objective best, do not dispute please and thank you')
plt.show()

Use pandas to create a Series named numbers from the following list:

['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
In [174]:
numbers = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
In [175]:
type(numbers)
Out[175]:
list
In [177]:
numbers = pd.Series(numbers)
What is the data type of the numbers Series?
In [178]:
type(numbers)
Out[178]:
pandas.core.series.Series
How many elements are in the number Series?
In [180]:
numbers.nunique()
Out[180]:
20
In [179]:
numbers.size
Out[179]:
20
Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers Series to a numeric data type.
In [184]:
float('1651.50')
Out[184]:
1651.5
In [187]:
numbers = numbers.str.replace('$', '').str.replace(',','').astype(float)
<ipython-input-187-dfa212c903ed>:1: FutureWarning: The default value of regex will change from True to False in a future version. In addition, single character regular expressions will*not* be treated as literal strings when regex=True.
  numbers = numbers.str.replace('$', '').str.replace(',','').astype(float)
In [186]:
numbers.dtype
Out[186]:
dtype('O')
Run the code to discover the maximum value from the Series.
In [188]:
numbers.max()
Out[188]:
4789988.17
Run the code to discover the minimum value from the Series.
In [189]:
numbers.min()
Out[189]:
278.6
What is the range of the values in the Series?
In [191]:
numbers.max() - numbers.min()
Out[191]:
4789709.57
In [192]:
(numbers.max(), numbers.min())
Out[192]:
(4789988.17, 278.6)
In [190]:
numbers.describe()
Out[190]:
count    2.000000e+01
mean     2.284406e+06
std      1.735261e+06
min      2.786000e+02
25%      7.259403e+05
50%      1.940065e+06
75%      4.188482e+06
max      4.789988e+06
dtype: float64
Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
In [195]:
pd.cut(numbers, 4).value_counts().sort_index()
Out[195]:
(-4511.11, 1197705.993]       7
(1197705.993, 2395133.385]    4
(2395133.385, 3592560.778]    3
(3592560.778, 4789988.17]     6
dtype: int64
Plot the binned data in a meaningful way. Be sure to include a title and axis labels.
In [196]:
pd.cut(numbers, 4).value_counts().sort_index().plot(kind='barh')
plt.title('4 bins')
plt.xlabel('count')
plt.ylabel('$ bins')
plt.show()

Use pandas to create a Series named exam_scores from the following list:

[60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
In [197]:
exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])
In [198]:
type(exam_scores)
Out[198]:
pandas.core.series.Series
How many elements are in the exam_scores Series?
In [199]:
exam_scores.size
Out[199]:
20
In [200]:
exam_scores.nunique()
Out[200]:
18
Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.
In [201]:
exam_scores.dtype
Out[201]:
dtype('int64')
In [202]:
exam_scores.max(), exam_scores.min(), exam_scores.mean(), exam_scores.median()
Out[202]:
(96, 60, 78.15, 79.0)
Plot the Series in a meaningful way and make sure your chart has a title and axis labels.
In [205]:
exam_scores.plot.hist()
plt.title('Distribution of Exam Scores')
plt.xlabel('Scores')
plt.show()

Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. Add the necessary points to the highest grade to make it 100, and add the same number of points to every other score in the Series as well.
In [208]:
100 - exam_scores.max()
Out[208]:
4
In [211]:
exam_scores.min()
Out[211]:
60
In [209]:
# curved grades will be assigned the original scores
# plus the difference between the highest grade and a perfect score
curved_grades = exam_scores + (100 - exam_scores.max())
In [212]:
curved_grades.min()
Out[212]:
64
Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.
In [ ]:
# maybe most intuitive way:
# use a .apply with a function that has a conditional flow
In [214]:
bin_edges = [0, 70, 75, 80, 90, 100]
bin_labels = ['F', 'D', 'C', 'B', 'A']
letter_grades = pd.cut(curved_grades, bins=bin_edges, labels=bin_labels)
In [215]:
letter_grades
Out[215]:
0     F
1     B
2     C
3     F
4     A
5     D
6     F
7     B
8     A
9     B
10    F
11    C
12    D
13    B
14    A
15    B
16    B
17    A
18    B
19    B
dtype: category
Categories (5, object): ['F' < 'D' < 'C' < 'B' < 'A']
Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.
In [218]:
letter_grades.value_counts().sort_index().plot.barh()
plt.title('Curved Letter Grade Distribution')
plt.show()

In [ ]:
 