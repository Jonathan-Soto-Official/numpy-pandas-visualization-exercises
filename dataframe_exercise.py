1. Copy the code from the lesson to create a dataframe full of student grades.
In [1]:
import pandas as pd
import numpy as np

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(df)
Out[1]:
pandas.core.frame.DataFrame
In [2]:
df.head()
Out[2]:
name	math	english	reading
0	Sally	62	85	80
1	Jane	88	79	67
2	Suzie	94	74	95
3	Billy	98	96	88
4	Ada	77	92	98
Create a column named passing_english that indicates whether each student has a passing grade in english.
In [4]:
df['english'] >= 70
Out[4]:
0      True
1      True
2      True
3      True
4      True
5      True
6     False
7     False
8     False
9      True
10     True
11    False
Name: english, dtype: bool
In [5]:
df['passing_english'] = df['english'] >= 70
In [7]:
df.head(10)
Out[7]:
name	math	english	reading	passing_english
0	Sally	62	85	80	True
1	Jane	88	79	67	True
2	Suzie	94	74	95	True
3	Billy	98	96	88	True
4	Ada	77	92	98	True
5	John	79	76	93	True
6	Thomas	82	64	81	False
7	Marie	93	63	90	False
8	Albert	92	62	87	False
9	Richard	69	80	94	True
Sort the english grades by the passing_english column. How are duplicates handled?
In [8]:
df.sort_values(by='passing_english')
Out[8]:
name	math	english	reading	passing_english
6	Thomas	82	64	81	False
7	Marie	93	63	90	False
8	Albert	92	62	87	False
11	Alan	92	62	72	False
0	Sally	62	85	80	True
1	Jane	88	79	67	True
2	Suzie	94	74	95	True
3	Billy	98	96	88	True
4	Ada	77	92	98	True
5	John	79	76	93	True
9	Richard	69	80	94	True
10	Isaac	92	99	93	True
Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)
In [14]:
df.sort_values(by=['passing_english', 'name'])
Out[14]:
name	math	english	reading	passing_english
11	Alan	92	62	72	False
8	Albert	92	62	87	False
7	Marie	93	63	90	False
6	Thomas	82	64	81	False
4	Ada	77	92	98	True
3	Billy	98	96	88	True
10	Isaac	92	99	93	True
1	Jane	88	79	67	True
5	John	79	76	93	True
9	Richard	69	80	94	True
0	Sally	62	85	80	True
2	Suzie	94	74	95	True
Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.
In [16]:
df.sort_values(by=['passing_english', 'english'], ascending = [True, False])
Out[16]:
name	math	english	reading	passing_english
6	Thomas	82	64	81	False
7	Marie	93	63	90	False
8	Albert	92	62	87	False
11	Alan	92	62	72	False
10	Isaac	92	99	93	True
3	Billy	98	96	88	True
4	Ada	77	92	98	True
0	Sally	62	85	80	True
9	Richard	69	80	94	True
1	Jane	88	79	67	True
5	John	79	76	93	True
2	Suzie	94	74	95	True
Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.
In [23]:
df['overall'] = round((df.math + df.english + df.reading)/3, 0).astype(int)
In [24]:
df.head()
Out[24]:
name	math	english	reading	passing_english	overall
0	Sally	62	85	80	True	76
1	Jane	88	79	67	True	78
2	Suzie	94	74	95	True	88
3	Billy	98	96	88	True	94
4	Ada	77	92	98	True	89
2. Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:
In [25]:
from pydataset import data

mpg = data('mpg')

mpg.head()
Out[25]:
manufacturer	model	displ	year	cyl	trans	drv	cty	hwy	fl	class
1	audi	a4	1.8	1999	4	auto(l5)	f	18	29	p	compact
2	audi	a4	1.8	1999	4	manual(m5)	f	21	29	p	compact
3	audi	a4	2.0	2008	4	manual(m6)	f	20	31	p	compact
4	audi	a4	2.0	2008	4	auto(av)	f	21	30	p	compact
5	audi	a4	2.8	1999	6	auto(l5)	f	16	26	p	compact
In [110]:
#data('mpg', show_doc = True)
How many rows and columns are there?
In [28]:
mpg.shape
Out[28]:
(234, 11)
What are the data types of each column?
In [29]:
mpg.dtypes
Out[29]:
manufacturer     object
model            object
displ           float64
year              int64
cyl               int64
trans            object
drv              object
cty               int64
hwy               int64
fl               object
class            object
dtype: object
Summarize the dataframe with .info and .describe
In [31]:
mpg.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 234 entries, 1 to 234
Data columns (total 11 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   manufacturer  234 non-null    object 
 1   model         234 non-null    object 
 2   displ         234 non-null    float64
 3   year          234 non-null    int64  
 4   cyl           234 non-null    int64  
 5   trans         234 non-null    object 
 6   drv           234 non-null    object 
 7   cty           234 non-null    int64  
 8   hwy           234 non-null    int64  
 9   fl            234 non-null    object 
 10  class         234 non-null    object 
dtypes: float64(1), int64(4), object(6)
memory usage: 21.9+ KB
In [33]:
mpg.describe()
Out[33]:
displ	year	cyl	cty	hwy
count	234.000000	234.000000	234.000000	234.000000	234.000000
mean	3.471795	2003.500000	5.888889	16.858974	23.440171
std	1.291959	4.509646	1.611534	4.255946	5.954643
min	1.600000	1999.000000	4.000000	9.000000	12.000000
25%	2.400000	1999.000000	4.000000	14.000000	18.000000
50%	3.300000	2003.500000	6.000000	17.000000	24.000000
75%	4.600000	2008.000000	8.000000	19.000000	27.000000
max	7.000000	2008.000000	8.000000	35.000000	44.000000
Rename the cty column to city.
In [38]:
mpg = mpg.rename(columns={'cty': 'city'})
In [39]:
mpg.head()
Out[39]:
manufacturer	model	displ	year	cyl	trans	drv	city	hwy	fl	class
1	audi	a4	1.8	1999	4	auto(l5)	f	18	29	p	compact
2	audi	a4	1.8	1999	4	manual(m5)	f	21	29	p	compact
3	audi	a4	2.0	2008	4	manual(m6)	f	20	31	p	compact
4	audi	a4	2.0	2008	4	auto(av)	f	21	30	p	compact
5	audi	a4	2.8	1999	6	auto(l5)	f	16	26	p	compact
In [ ]:
 
Rename the hwy column to highway.
In [40]:
mpg = mpg.rename(columns={'hwy': 'highway'})
In [41]:
mpg.head()
Out[41]:
manufacturer	model	displ	year	cyl	trans	drv	city	highway	fl	class
1	audi	a4	1.8	1999	4	auto(l5)	f	18	29	p	compact
2	audi	a4	1.8	1999	4	manual(m5)	f	21	29	p	compact
3	audi	a4	2.0	2008	4	manual(m6)	f	20	31	p	compact
4	audi	a4	2.0	2008	4	auto(av)	f	21	30	p	compact
5	audi	a4	2.8	1999	6	auto(l5)	f	16	26	p	compact
In [ ]:
 
Do any cars have better city mileage than highway mileage?
In [42]:
#True = 1, Flase = 0
mask = mpg.city > mpg.highway
In [108]:
mask
Out[108]:
1      False
2      False
3      False
4      False
5      False
       ...  
230    False
231    False
232    False
233    False
234    False
Length: 234, dtype: bool
In [44]:
len(mpg[mask])
Out[44]:
0
In [45]:
mask.sum()
Out[45]:
0
In [ ]:
 
Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
In [46]:
mpg['mileage_difference'] = round(mpg.highway - mpg.city, 2)
In [48]:
mpg[['highway', 'city', 'mileage_difference']].head()
Out[48]:
highway	city	mileage_difference
1	29	18	11
2	29	21	8
3	31	20	11
4	30	21	9
5	26	16	10
Which car (or cars) has the highest mileage difference?
In [49]:
mpg.describe()
Out[49]:
displ	year	cyl	city	highway	mileage_difference
count	234.000000	234.000000	234.000000	234.000000	234.000000	234.000000
mean	3.471795	2003.500000	5.888889	16.858974	23.440171	6.581197
std	1.291959	4.509646	1.611534	4.255946	5.954643	2.262739
min	1.600000	1999.000000	4.000000	9.000000	12.000000	2.000000
25%	2.400000	1999.000000	4.000000	14.000000	18.000000	5.000000
50%	3.300000	2003.500000	6.000000	17.000000	24.000000	7.000000
75%	4.600000	2008.000000	8.000000	19.000000	27.000000	8.000000
max	7.000000	2008.000000	8.000000	35.000000	44.000000	12.000000
In [50]:
mpg[mpg.mileage_difference == mpg.mileage_difference.max()]
Out[50]:
manufacturer	model	displ	year	cyl	trans	drv	city	highway	fl	class	mileage_difference
107	honda	civic	1.8	2008	4	auto(l5)	f	24	36	c	subcompact	12
223	volkswagen	new beetle	1.9	1999	4	auto(l4)	f	29	41	d	subcompact	12
In [ ]:
 
Which compact class car has the worst highway mileage? The best?
In [51]:
mpg[mpg['class'] == 'compact']
Out[51]:
manufacturer	model	displ	year	cyl	trans	drv	city	highway	fl	class	mileage_difference
1	audi	a4	1.8	1999	4	auto(l5)	f	18	29	p	compact	11
2	audi	a4	1.8	1999	4	manual(m5)	f	21	29	p	compact	8
3	audi	a4	2.0	2008	4	manual(m6)	f	20	31	p	compact	11
4	audi	a4	2.0	2008	4	auto(av)	f	21	30	p	compact	9
5	audi	a4	2.8	1999	6	auto(l5)	f	16	26	p	compact	10
6	audi	a4	2.8	1999	6	manual(m5)	f	18	26	p	compact	8
7	audi	a4	3.1	2008	6	auto(av)	f	18	27	p	compact	9
8	audi	a4 quattro	1.8	1999	4	manual(m5)	4	18	26	p	compact	8
9	audi	a4 quattro	1.8	1999	4	auto(l5)	4	16	25	p	compact	9
10	audi	a4 quattro	2.0	2008	4	manual(m6)	4	20	28	p	compact	8
11	audi	a4 quattro	2.0	2008	4	auto(s6)	4	19	27	p	compact	8
12	audi	a4 quattro	2.8	1999	6	auto(l5)	4	15	25	p	compact	10
13	audi	a4 quattro	2.8	1999	6	manual(m5)	4	17	25	p	compact	8
14	audi	a4 quattro	3.1	2008	6	auto(s6)	4	17	25	p	compact	8
15	audi	a4 quattro	3.1	2008	6	manual(m6)	4	15	25	p	compact	10
142	nissan	altima	2.4	1999	4	manual(m5)	f	21	29	r	compact	8
143	nissan	altima	2.4	1999	4	auto(l4)	f	19	27	r	compact	8
170	subaru	impreza awd	2.5	2008	4	auto(s4)	4	20	25	p	compact	5
171	subaru	impreza awd	2.5	2008	4	auto(s4)	4	20	27	r	compact	7
172	subaru	impreza awd	2.5	2008	4	manual(m5)	4	19	25	p	compact	6
173	subaru	impreza awd	2.5	2008	4	manual(m5)	4	20	27	r	compact	7
187	toyota	camry solara	2.2	1999	4	auto(l4)	f	21	27	r	compact	6
188	toyota	camry solara	2.2	1999	4	manual(m5)	f	21	29	r	compact	8
189	toyota	camry solara	2.4	2008	4	manual(m5)	f	21	31	r	compact	10
190	toyota	camry solara	2.4	2008	4	auto(s5)	f	22	31	r	compact	9
191	toyota	camry solara	3.0	1999	6	auto(l4)	f	18	26	r	compact	8
192	toyota	camry solara	3.0	1999	6	manual(m5)	f	18	26	r	compact	8
193	toyota	camry solara	3.3	2008	6	auto(s5)	f	18	27	r	compact	9
194	toyota	corolla	1.8	1999	4	auto(l3)	f	24	30	r	compact	6
195	toyota	corolla	1.8	1999	4	auto(l4)	f	24	33	r	compact	9
196	toyota	corolla	1.8	1999	4	manual(m5)	f	26	35	r	compact	9
197	toyota	corolla	1.8	2008	4	manual(m5)	f	28	37	r	compact	9
198	toyota	corolla	1.8	2008	4	auto(l4)	f	26	35	r	compact	9
208	volkswagen	gti	2.0	1999	4	manual(m5)	f	21	29	r	compact	8
209	volkswagen	gti	2.0	1999	4	auto(l4)	f	19	26	r	compact	7
210	volkswagen	gti	2.0	2008	4	manual(m6)	f	21	29	p	compact	8
211	volkswagen	gti	2.0	2008	4	auto(s6)	f	22	29	p	compact	7
212	volkswagen	gti	2.8	1999	6	manual(m5)	f	17	24	r	compact	7
213	volkswagen	jetta	1.9	1999	4	manual(m5)	f	33	44	d	compact	11
214	volkswagen	jetta	2.0	1999	4	manual(m5)	f	21	29	r	compact	8
215	volkswagen	jetta	2.0	1999	4	auto(l4)	f	19	26	r	compact	7
216	volkswagen	jetta	2.0	2008	4	auto(s6)	f	22	29	p	compact	7
217	volkswagen	jetta	2.0	2008	4	manual(m6)	f	21	29	p	compact	8
218	volkswagen	jetta	2.5	2008	5	auto(s6)	f	21	29	r	compact	8
219	volkswagen	jetta	2.5	2008	5	manual(m5)	f	21	29	r	compact	8
220	volkswagen	jetta	2.8	1999	6	auto(l4)	f	16	23	r	compact	7
221	volkswagen	jetta	2.8	1999	6	manual(m5)	f	17	24	r	compact	7
In [54]:
#This is a little busy, lets clean it up in the next.
mpg[(mpg['class'] == 'compact') & 
    (mpg['highway'] == mpg[mpg['class'] == 'compact'].highway.max())]
Out[54]:
manufacturer	model	displ	year	cyl	trans	drv	city	highway	fl	class	mileage_difference
213	volkswagen	jetta	1.9	1999	4	manual(m5)	f	33	44	d	compact	11
In [55]:
compacts = mpg[mpg['class'] == 'compact']
In [63]:
compacts[(compacts.highway == compacts.highway.max())]
Out[63]:
manufacturer	model	displ	year	cyl	trans	drv	city	highway	fl	class	mileage_difference
213	volkswagen	jetta	1.9	1999	4	manual(m5)	f	33	44	d	compact	11
In [64]:
compacts[(compacts.highway == compacts.highway.min())]
Out[64]:
manufacturer	model	displ	year	cyl	trans	drv	city	highway	fl	class	mileage_difference
220	volkswagen	jetta	2.8	1999	6	auto(l4)	f	16	23	r	compact	7
Create a column named average_mileage that is the mean of the city and highway mileage.
In [65]:
mpg['avg_mileage'] = (mpg.city + mpg.highway) /2
In [66]:
mpg.head()
Out[66]:
manufacturer	model	displ	year	cyl	trans	drv	city	highway	fl	class	mileage_difference	avg_mileage
1	audi	a4	1.8	1999	4	auto(l5)	f	18	29	p	compact	11	23.5
2	audi	a4	1.8	1999	4	manual(m5)	f	21	29	p	compact	8	25.0
3	audi	a4	2.0	2008	4	manual(m6)	f	20	31	p	compact	11	25.5
4	audi	a4	2.0	2008	4	auto(av)	f	21	30	p	compact	9	25.5
5	audi	a4	2.8	1999	6	auto(l5)	f	16	26	p	compact	10	21.0
Which dodge car has the best average mileage? The worst?
In [68]:
mpg.columns
Out[68]:
Index(['manufacturer', 'model', 'displ', 'year', 'cyl', 'trans', 'drv', 'city',
       'highway', 'fl', 'class', 'mileage_difference', 'avg_mileage'],
      dtype='object')
In [69]:
dodges = mpg[mpg.manufacturer == 'dodge']
In [70]:
dodges.head()
Out[70]:
manufacturer	model	displ	year	cyl	trans	drv	city	highway	fl	class	mileage_difference	avg_mileage
38	dodge	caravan 2wd	2.4	1999	4	auto(l3)	f	18	24	r	minivan	6	21.0
39	dodge	caravan 2wd	3.0	1999	6	auto(l4)	f	17	24	r	minivan	7	20.5
40	dodge	caravan 2wd	3.3	1999	6	auto(l4)	f	16	22	r	minivan	6	19.0
41	dodge	caravan 2wd	3.3	1999	6	auto(l4)	f	16	22	r	minivan	6	19.0
42	dodge	caravan 2wd	3.3	2008	6	auto(l4)	f	17	24	r	minivan	7	20.5
In [71]:
dodges[dodges.avg_mileage == dodges.avg_mileage.max()]
Out[71]:
manufacturer	model	displ	year	cyl	trans	drv	city	highway	fl	class	mileage_difference	avg_mileage
38	dodge	caravan 2wd	2.4	1999	4	auto(l3)	f	18	24	r	minivan	6	21.0
In [72]:
dodges[dodges.avg_mileage == dodges.avg_mileage.min()]
Out[72]:
manufacturer	model	displ	year	cyl	trans	drv	city	highway	fl	class	mileage_difference	avg_mileage
55	dodge	dakota pickup 4wd	4.7	2008	8	auto(l5)	4	9	12	e	pickup	3	10.5
60	dodge	durango 4wd	4.7	2008	8	auto(l5)	4	9	12	e	suv	3	10.5
66	dodge	ram 1500 pickup 4wd	4.7	2008	8	auto(l5)	4	9	12	e	pickup	3	10.5
70	dodge	ram 1500 pickup 4wd	4.7	2008	8	manual(m6)	4	9	12	e	pickup	3	10.5
3. Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
In [73]:
mams = data('Mammals')
In [111]:
mams.head()
Out[111]:
weight	speed	hoppers	specials
1	6000.0	35.0	False	False
2	4000.0	26.0	False	False
3	3000.0	25.0	False	False
4	1400.0	45.0	False	False
5	400.0	70.0	False	False
In [76]:
#data('Mammals', show_doc=True)
In [ ]:
 
How many rows and columns are there?
In [77]:
mams.shape
Out[77]:
(107, 4)
What are the data types?
In [78]:
mams.dtypes
Out[78]:
weight      float64
speed       float64
hoppers        bool
specials       bool
dtype: object
Summarize the dataframe with .info and .describe
In [79]:
mams.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 107 entries, 1 to 107
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   weight    107 non-null    float64
 1   speed     107 non-null    float64
 2   hoppers   107 non-null    bool   
 3   specials  107 non-null    bool   
dtypes: bool(2), float64(2)
memory usage: 2.7 KB
In [80]:
mams.describe()
Out[80]:
weight	speed
count	107.000000	107.000000
mean	278.688178	46.208411
std	839.608269	26.716778
min	0.016000	1.600000
25%	1.700000	22.500000
50%	34.000000	48.000000
75%	142.500000	65.000000
max	6000.000000	110.000000
What is the the weight of the fastest animal?
In [101]:
mams[mams.speed == mams.speed.max()].weight
Out[101]:
53    55.0
Name: weight, dtype: float64
What is the overal percentage of specials?
In [84]:
mams.specials.sum()
Out[84]:
10
In [86]:
len(mams)
Out[86]:
107
In [87]:
(mams.specials.sum() /len(mams))* 100
Out[87]:
9.345794392523365
In [ ]:
 
How many animals are hoppers that are above the median speed? What percentage is this?
In [88]:
mams.columns
Out[88]:
Index(['weight', 'speed', 'hoppers', 'specials'], dtype='object')
In [89]:
mams[mams.hoppers]
Out[89]:
weight	speed	hoppers	specials
82	0.056	21.0	True	False
85	0.035	32.0	True	False
86	0.035	14.0	True	False
96	4.600	64.0	True	False
97	4.400	72.0	True	False
98	4.000	72.0	True	False
99	3.500	56.0	True	False
100	2.000	64.0	True	False
101	1.900	56.0	True	False
102	1.500	50.0	True	False
103	1.500	40.0	True	False
In [90]:
mams[mams.speed > mams.speed.median()]
Out[90]:
weight	speed	hoppers	specials
5	400.0	70.0	False	False
6	350.0	70.0	False	False
7	300.0	64.0	False	False
8	260.0	70.0	False	False
11	1000.0	60.0	False	False
12	900.0	70.0	False	False
13	900.0	56.0	False	False
15	750.0	57.0	False	False
17	450.0	56.0	False	False
18	300.0	72.0	False	False
19	300.0	90.0	False	False
20	250.0	80.0	False	False
21	250.0	56.0	False	False
22	170.0	80.0	False	False
24	130.0	70.0	False	False
25	120.0	80.0	False	False
26	120.0	61.0	False	False
28	100.0	64.0	False	False
29	85.0	55.0	False	False
30	80.0	65.0	False	False
31	72.0	56.0	False	False
33	65.0	60.0	False	False
34	62.0	81.0	False	False
35	50.0	100.0	False	False
36	50.0	60.0	False	False
39	37.0	105.0	False	False
40	35.0	80.0	False	False
41	34.0	97.0	False	False
42	30.0	97.0	False	False
43	30.0	80.0	False	False
45	20.0	81.0	False	False
48	230.0	56.0	False	False
49	150.0	59.0	False	False
51	65.0	65.0	False	False
52	60.0	60.0	False	False
53	55.0	110.0	False	False
54	45.0	50.0	False	False
55	40.0	64.0	False	False
56	25.0	67.0	False	False
57	20.0	70.0	False	False
58	16.0	65.0	False	False
61	10.0	56.0	False	False
62	7.0	60.0	False	False
63	6.0	72.0	False	False
64	5.0	64.0	False	False
96	4.6	64.0	True	False
97	4.4	72.0	True	False
98	4.0	72.0	True	False
99	3.5	56.0	True	False
100	2.0	64.0	True	False
101	1.9	56.0	True	False
102	1.5	50.0	True	False
104	50.0	65.0	False	False
In [91]:
mams[(mams.hoppers == True) & (mams.speed > mams.speed.median())]
Out[91]:
weight	speed	hoppers	specials
96	4.6	64.0	True	False
97	4.4	72.0	True	False
98	4.0	72.0	True	False
99	3.5	56.0	True	False
100	2.0	64.0	True	False
101	1.9	56.0	True	False
102	1.5	50.0	True	False
In [99]:
round(len(mams[(mams.hoppers == True) & 
      (mams.speed > mams.speed.median())]) / len(mams) *100, 2)
Out[99]:
6.54
In [102]:
hoppers = mams[(mams.hoppers == True)]
In [103]:
hoppers.head()
Out[103]:
weight	speed	hoppers	specials
82	0.056	21.0	True	False
85	0.035	32.0	True	False
86	0.035	14.0	True	False
96	4.600	64.0	True	False
97	4.400	72.0	True	False
In [107]:
#CAUTION: Reference the correct dataframe when comparing a 
#subset of a data frame(hoppers) to the whole dataframe(mams)
round(len(hoppers[(hoppers.speed > mams.speed.median())]) / len(mams) *100, 2)
Out[107]:
6.54
In [ ]:
 