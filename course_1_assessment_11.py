# q1. Which of these is a correct reference diagram following the execution of the following code?
lst = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
lst.remove('pluto')
first_three = lst[:3]

# A. 1.

# q2. What will be the value of a after the following code has executed?
a = ["holiday", "celebrate!"]
quiet = a
quiet.append("company")

# a = ["holiday", "celebrate!", "company!"]

# q3. Could aliasing cause potential confusion in this problem?
b = ['q', 'u', 'i']
z = b
b[1] = 'i'
z.remove('i')
print(z)

# A. yes

# q4. Given that we want to accumulate the total sum of a list of numbers, which of the following accumulator patterns would be appropriate?
## 1
nums = [4, 5, 2, 93, 3, 5]
s = 0
for n in nums:
    s = s + 1

## 2
nums = [4, 5, 2, 93, 3, 5]
s = 0
for n in nums:
    s = n + n

## 3
nums = [4, 5, 2, 93, 3, 5]
s = 0
for n in nums:
    s = s + n

# C. 3.

# q5. Given that we want to accumulate the total number of strings in the list, which of the following accumulator patterns would be appropriate?
## 1
lst = ['plan', 'answer', 5, 9.29, 'order, items', [4]]
s = 0
for n in lst:
    s = s + n

## 2
lst = ['plan', 'answer', 5, 9.29, 'order, items', [4]]
for item in lst:
    s = 0
    if type(item) == type("string"):
        s = s + 1

## 3
lst = ['plan', 'answer', 5, 9.29, 'order, items', [4]]
s = ""
for n in lst:
    s = s + n

## 4   
lst = ['plan', 'answer', 5, 9.29, 'order, items', [4]]
s = 0
for item in lst:
    if type(item) == type("string"):
        s = s + 1

# D. 4.

# q6. Which of these are good names for an accumulator variable? Select as many as apply.
A. sum
B. x
C. total
D. accum
E. none of the above

# C. total; D. accum

# q7. Which of these are good names for an iterator (loop) variable? Select as many as apply.
A. item
B. y
C. elem
D. char
E. none of the above

# A. item; C. elem; D. char

# q8. Which of these are good names for a sequence variable? Select as many as apply.
A. num_lst
B. p
C. sentence
D. names
E. none of the above

# A. num_list; C. sentence; D. names

# q9. Given the following scenario, what are good names for the accumulator variable, iterator variable, and sequence variable? You are writing code that uses a list of sentences and accumulates the total number of sentences that have the word ‘happy’ in them.
A. accumulator variable: x | iterator variable: s | sequence variable: lst
B. accumulator variable: total | iterator variable: s | sequence variable: lst
C. accumulator variable: x | iterator variable: sentences | sequence variable: sentence_lst
D. accumulator variable: total | iterator variable: sentence |sequence variable: sentence_lst
E. none of the above

# D

# q10. For each character in the string saved in ael, append that character to a list that should be saved in a variable app.
ael = "python!"
lst = []
for i in ael:
    lst.append(i)
app = lst

# q11. For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense). Save these past tense words to a list called past_wrds.
wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
lst = []
for i in wrds:
    i = i + "ed"
    lst.append(i)
past_wrds = lst 