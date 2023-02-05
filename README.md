# Spring 2023 Python 🐍🌷🤓

## Week 2: Python Poem


### Concept
Reviewing Python methods for playing with strings reminded me of cut-ups, blackout poems, and other poem projects like Jen Bervin's Nets, which strategically removes words from Shakespeare's Sonnets to create new poems. 

I decided to modify the well-known villanelle [One Art](https://www.poetryfoundation.org/poems/47536/one-art) by Elizabeth Bishop, which is about gradual loss, from mundane to monumental.


### Process
I found a list of the [10,000 most common English words](https://github.com/first20hours/google-10000-english) in order of frequency, as determined by n-gram frequency analysis of the Google's Trillion Word Corpus, and cloned it to my week 2 repo. I clipped the list to 1500 words, removed single-letter words besides "a" and "i", reversed the list to start from least to most common, and checked each of the words in One Art against it. If a match was found, the word was removed and the poem reprinted.

The result is an [1,870-line poem](https://github.com/iteratiii/spring-2023-python/blob/main/week2/PythonPoem.ipynb) that gradually decays as it repeats the original work, losing parts of its structure but still standing.

I also listed the words lost in order of loss at the end of the poem.


### Struggle
I had some trouble with dealing with capitalization. For example, I and The should be replaced but are not. 

Right now, the characters in the poem aren't being stored in any way during checking, so there's no way to disassemble, remove case, and restore case and punctuation, and reassemble the poem to reprint it on each elision. This is the next step. However, the result might not be as nice; it's poetic that "I" remains while everything else is lost.

I'm sure there's also a cleaner way to refine the tester_replacer dict with RegEx.
