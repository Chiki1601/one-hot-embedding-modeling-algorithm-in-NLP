#one hot encoding

import numpy as np
samples = {&#39;Jupiter has 79 known moons .&#39;, &#39;Neptune has 14 confirmed
moons !&#39;} # Sample set for our example
# Create an empty dictionary
token_index = {}
#Create a counter for counting the number of key-value pairs in the
token_length
counter = 0

# Select the elements of the samples which are the two sentences
for sample in samples:
for considered_word in sample.split():
if considered_word not in token_index:

# If the considered word is not present in the dictionary token_index,
add it to the token_index
# The index of the word in the dictionary begins from 1

NLP(2170723)Enrollment_no.:181010107008
token_index.update({considered_word : counter + 1})

# updating the value of counter
counter = counter + 1

print(token_index)
