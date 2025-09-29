
## Solution 

### Approach & Analysis

Query Analysis:
From the query_distribution.png, it is seen that the number of times a node is called goes down rapidly and after 23, there are no nodes called with a greater value.

This is due to the fact that the distribution is exponential with parameter of 0.1.
The pmf of this distribution is: 0.1e^{-0.1x}
The CDF: F(x) = 1 - e^{-0.1x}
is the probability of getting x - 1 or less and provides us with theoretical insight behind the distribution
For example, the probability of getting node 0 is roughly F(1) = 0.095
This matches the distribution from the experiements well.
Some other values of F(x) for reference:
F(2) = 0.181
F(3) = 0.25
F(5) = 0.393
F(10) = 0.632
F(20) = 0.865
F(30) = 0.95
F(40) = 0.982
F(50) = 0.993

Also, the exponential distribution is memoryless. The application of this property is that if we can optimally check if a node is 1 to 50 and it is not 1 to 50, the same structure can be used to check if a node is 51 to 100 except replace n with n + 50. This suggests that a recursive structure could be effective.

Initial ideas:
Idea 1:
Have the nodes in a line graph. Lower nodes with higher probability first.
Pros:
All nodes will be visited
Cons:
There are several random walks per query that could be used to reduce number of nodes visited

Even though the line idea may seem to not be effective because it does not take advantage of multiple random walks, the fact that it does not miss a node could be a useful property.

Idea 2:
Have several line graphs
Pros:
Good chance all nodes are visited up to a certain number of lines while significantly reducing query.

Cons:
If one line is missed, it could miss the node

Probability of missing a line given n lines:
h(n) = (1 - sum_{j is 0 to n} (-1)^{n-j} (n choose j) j^10)/n^10

h(1) = 0
h(2) = 0.00195
h(3) = 0.05197
h(4) = 0.21940
h(5) = 0.47745
h(6) = 0.72819
h(7) = 0.89509
h(8) = 0.97184

The probability of missing a line is super low with 2 and still low with 3.

Idea 3:
Multiple lines with fail-safes for missing line

Connect the end of the lines with the start of another line in case one is missed.

Design:
Have n lines. If more than 3, split into 3 and split some of the split nodes in a way such that the probability of going to each line is the same. Line i will have values i more than a multiple of n up to a certain number k. It will be from smallest to largest number The end of each line will connect to the start of another line cyclically. There is also a chance that it goes to another graph with a similar design for larger numbers.

Initial:
There are 5 lines with length of around 8 (around 40 nodes). The end of each line will have a 95% of going to next line and 5% chance of going to graph for larger numbers.


### Optimization Strategy
What needs to be optimized:
Number of lines
Length of the lines
Probability of going to the other graph for larger numbers (not used)

Testing Results:
initial testing (5 lines): length 8
SUCCESS RATE:
  Optimized: 100.0% (200/200)
  ✅ Improvement: 20.5%

PATH LENGTHS (successful queries only):
  Optimized: 143.25 (200/200 queries)
  ✅ Improvement: 75.1%

COMBINED SCORE (success rate × path efficiency):
  Score: 261.22

Note, including many nodes will be difficult since nodes start at random positions and it will be optimal to make those point to 0 for super large numbers.

Results after making large numbers point to 0 (length 8):
These results are from a code that had a bug, but fixing the bug gave lower results
SUCCESS RATE:
  Initial:   79.5% (159/200)
  Optimized: 100.0% (200/200)
  ✅ Improvement: 20.5%

PATH LENGTHS (successful queries only):
  Initial:   538.0 (159/200 queries)
  Optimized: 19.0 (200/200 queries)
  ✅ Improvement: 96.5%

COMBINED SCORE (success rate × path efficiency):
  Score: 437.81


length 4
SUCCESS RATE:
  Initial:   80.5% (161/200)
  Optimized: 100.0% (200/200)
  ✅ Improvement: 19.5%

PATH LENGTHS (successful queries only):
  Initial:   595.0 (161/200 queries)
  Optimized: 15.0 (200/200 queries)
  ✅ Improvement: 97.5%

COMBINED SCORE (success rate × path efficiency):
  Score: 470.54

length 5
SUCCESS RATE:
  Initial:   79.5% (159/200)
  Optimized: 100.0% (200/200)
  ✅ Improvement: 20.5%

PATH LENGTHS (successful queries only):
  Initial:   612.5 (159/200 queries)
  Optimized: 15.5 (200/200 queries)
  ✅ Improvement: 97.5%

COMBINED SCORE (success rate × path efficiency):
  Score: 470.17


length 6
SUCCESS RATE:
  Initial:   80.0% (160/200)
  Optimized: 100.0% (200/200)
  ✅ Improvement: 20.0%

PATH LENGTHS (successful queries only):
  Initial:   610.5 (160/200 queries)
  Optimized: 16.0 (200/200 queries)
  ✅ Improvement: 97.4%

COMBINED SCORE (success rate × path efficiency):
  Score: 466.76

length 7
SUCCESS RATE:
  Initial:   79.5% (159/200)
  Optimized: 100.0% (200/200)
  ✅ Improvement: 20.5%

PATH LENGTHS (successful queries only):
  Initial:   555 (159/200 queries)
  Optimized: 18.0 (200/200 queries)
  ✅ Improvement: 96.8%

COMBINED SCORE (success rate × path efficiency):
  Score: 446.05

length 8 (above)

length 9

SUCCESS RATE:
  Optimized: 100.0% (200/200)
  ✅ Improvement: 20.5%

PATH LENGTHS (successful queries only):
  Optimized: 21.75 (200/200 queries)
  ✅ Improvement: 96.1%

COMBINED SCORE (success rate × path efficiency):
  Score: 427.26



3 Lines
length 5
SUCCESS RATE:
  Initial:   80.5% (161/200)
  Optimized: 100.0% (200/200)
  ✅ Improvement: 19.5%

PATH LENGTHS (successful queries only):
  Initial:   496.0 (161/200 queries)
  Optimized: 269.75 (200/200 queries)
  ✅ Improvement: 45.6%

COMBINED SCORE (success rate × path efficiency):
  Score: 204.34

length 6
SUCCESS RATE:
  Initial:   79.5% (159/200)
  Optimized: 100.0% (200/200)
  ✅ Improvement: 20.5%

PATH LENGTHS (successful queries only):
  Initial:   555.5 (159/200 queries)
  Optimized: 195.25 (200/200 queries)
  ✅ Improvement: 64.9%

COMBINED SCORE (success rate × path efficiency):
  Score: 234.68

length 7

SUCCESS RATE:
  Initial:   80.5% (161/200)
  Optimized: 100.0% (200/200)
  ✅ Improvement: 19.5%

PATH LENGTHS (successful queries only):
  Initial:   551.5 (161/200 queries)
  Optimized: 170.75 (200/200 queries)
  ✅ Improvement: 69.0%

COMBINED SCORE (success rate × path efficiency):
  Score: 244.22

length 8

SUCCESS RATE:
  Initial:   80.0% (160/200)
  Optimized: 100.0% (200/200)
  ✅ Improvement: 20.0%

PATH LENGTHS (successful queries only):
  Initial:   587.75 (160/200 queries)
  Optimized: 17.75 (200/200 queries)
  ✅ Improvement: 97.0%

COMBINED SCORE (success rate × path efficiency):
  Score: 452.97

length 9
SUCCESS RATE:
  Initial:   79.5% (159/200)
  Optimized: 100.0% (200/200)
  ✅ Improvement: 20.5%

PATH LENGTHS (successful queries only):
  Initial:   545.5 (159/200 queries)
  Optimized: 21.5 (200/200 queries)
  ✅ Improvement: 96.1%

COMBINED SCORE (success rate × path efficiency):
  Score: 427.23

length 10
SUCCESS RATE:
  Initial:   79.0% (158/200)
  Optimized: 100.0% (200/200)
  ✅ Improvement: 21.0%

PATH LENGTHS (successful queries only):
  Initial:   655.75 (158/200 queries)
  Optimized: 17.75 (200/200 queries)
  ✅ Improvement: 97.3%

COMBINED SCORE (success rate × path efficiency):
  Score: 463.61

length 11

SUCCESS RATE:
  Initial:   79.0% (158/200)
  Optimized: 100.0% (200/200)
  ✅ Improvement: 21.0%

PATH LENGTHS (successful queries only):
  Initial:   584.0 (158/200 queries)
  Optimized: 19.75 (200/200 queries)
  ✅ Improvement: 96.6%

COMBINED SCORE (success rate × path efficiency):
  Score: 442.00


length 12

SUCCESS RATE:
  Initial:   79.5% (159/200)
  Optimized: 100.0% (200/200)
  ✅ Improvement: 20.5%

PATH LENGTHS (successful queries only):
  Initial:   595.5 (159/200 queries)
  Optimized: 18.5 (200/200 queries)
  ✅ Improvement: 96.9%

COMBINED SCORE (success rate × path efficiency):
  Score: 450.22

6 Lines

### Implementation Details

My final implementation is a graph where 0 points to 1,2, and 3. 1 points to 4, 5, and 6. After this, each number starting from 4 points to the number that is 5 after it, so each number with the same value mode 5 are in a line. The intended solution should have be each number starting from 2. However, starting from 4 gave better results. After the nodes reach 20 to 24, they go back nodes 1, 2, 3, but generally one that did not contain the line graph containing that number so the random walk could visit other numbers. The only exception is 21 going back to 1 since both 2 and 3 were taken. All of the other numbers point to 0. This is using the fact that the exponential distribution rarely gives large numbers.

### Results

5 lines and length 5
SUCCESS RATE:
  Initial:   80.5% (161/200)
  Optimized: 100.0% (200/200)
  ✅ Improvement: 19.5%

PATH LENGTHS (successful queries only):
  Initial:   649.0 (161/200 queries)
  Optimized: 15.5 (200/200 queries)
  ✅ Improvement: 97.6%

COMBINED SCORE (success rate × path efficiency):
  Score: 475.82

This is the best result I have seen. The results to sometimes vary.

### Trade-offs & Limitations

The main limitation of this approach is that this approach is unlikely to hit numbers greater than 26 unless the random walk starts there. However, it is likely going to hit numbers 0 to 25 well. Since there still is 5 to 13.5% chance of getting 26 or more, it may be worth considering making the graphs cover more numbers. However, this will slow down in the likely case that the query is for a smaller node. The two possible problems is if the line with the number we are looking for is missed or the random walk start in a line without the number or after it. Using 3 lines will make the first problem of missing the line less likely, but it will make the second problem worse.

### Iteration Journey

I first thought of making the graph 1 line which will mean all of the numbers will be hit and the nodes in order. However, this would not use the fact that there are many random walks. Also, the start of the random walk can not be chosen. However, this idea provided some sort of way to help make sure all nodes were visited. I then decided to include many lines to use the fact that there are many random walks meaning several paths could be explored at once. I then tested different lengths of lines and a few different number of lines. If I have more time, in addition to doing more testing with different number of lines, I could have considered a tree structure. It might be able to use the fact that there are many random walks more effectively. However, it might have more variance in the time taken. Random walks will likely miss the path with the query, but it would take less time to go to the root.

### Credits
Cursor was used for some parts of coding and sorting out github issues
Desmos was used for some calculations
Gemini was used to get equation for h(n)

---

* Be concise but thorough - aim for 500-1000 words total
* Include specific data and metrics where relevant
* Explain your reasoning, not just what you did