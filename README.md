# Spring 2023 Python 🐍🌷🤓

## Week 14: OpenCV
Too busy, did not do the homework.

## Week 12–13: Raspberry Pi
We adapted the speech-to-text function from the class demo as input to a Python ASCII text and art generator library and presented it in class.

## Week 11: Fine-Tune
I [fine-tuned GPT](https://github.com/iteratiii/spring-2023-python/blob/main/week11/homework-finetune-redacted.ipynb) with state / transphobic bill data from my main project.

## Week 10: GPT Instructions
I was kind of pressed for time this week and asked GPT to tell me [how to make a plaster hand](https://github.com/iteratiii/spring-2023-python/blob/main/week10/homework-GPT%20Instructions.ipynb), which I needed for my main project.

## Week 9: Explore ML Tools
I [messed around](https://github.com/iteratiii/spring-2023-python/blob/main/week9/homework-Explore%20ML%20Platforms.ipynb) with DALL-E, Runway, and Playform.

## Week 8: Spring Break

## Week 7: Scrape It
I [scraped](https://github.com/iteratiii/spring-2023-python/blob/main/week7/homework-Scrape%20It.ipynb) some [beautiful collages](https://github.com/iteratiii/spring-2023-python/tree/main/week7/blood_book) from Public Domain Review.

## Week 6: API
I've been using the [Legiscan API](https://github.com/iteratiii/spring-2023-python/blob/main/week6/homework-APIs.ipynb) to access legal texts and information for another project.

## Week 5: Map It
I made [visualizations of the distances](https://github.com/iteratiii/spring-2023-python/blob/main/week5/homework-MapIt.ipynb) of my favorite places from week 4.

## Week 4: Objects of Desire
I made a class to hold [some of my favorite places](https://github.com/iteratiii/spring-2023-python/blob/main/week4/homework-ObjectsOfDesire.ipynb) in New York City. I learned to use the googlemaps library (after jumping between geocoder, geomaps, etc. I went straight to the source). Today I learned that instead of having to go and get my own key and so on, I could have tried using Beautiful Soup and Selenium. Maybe in the future!

## Week 3: Creative Calculator
I felt so bored by math, but then I realized I can do operations on language.

I added strings together and multipled vowels in a name to create [some cute meme generators](https://github.com/iteratiii/spring-2023-python/blob/main/week3/homework-CreativeCalculator.ipynb).

I also learned more about using libraries and manipulating strings.

## Week 2: Python Poem


### Concept
Reviewing Python methods for playing with strings reminded me of cut-ups, blackout poems, and other poem projects like [Jen Bervin's Nets](https://www.jenbervin.com/img/projects/_gallery_2x/Work_Nets_06.jpg), which strategically removes words from Shakespeare's Sonnets to create new poems. 

I decided to modify the well-known villanelle [One Art](https://www.poetryfoundation.org/poems/47536/one-art) by Elizabeth Bishop, which is about gradual loss, from mundane to monumental.


### Process
I found a list of the [10,000 most common English words](https://github.com/first20hours/google-10000-english) in order of frequency, as determined by n-gram frequency analysis of the Google's Trillion Word Corpus, and cloned it to my week 2 repo. I clipped the list to 1500 words, removed single-letter words besides "a" and "i", reversed the list to start from least to most common, and checked each of the words in One Art against it. If a match was found, the word was removed and the poem reprinted.

The result is an [1,870-line poem](https://github.com/iteratiii/spring-2023-python/blob/main/week2/homework-PythonPoem.ipynb) that gradually decays as it repeats the original work, losing parts of its structure but still standing.

I also listed the words lost in order of loss at the end of the poem.

I made a shorter version that's <500 lines, but it doesn't have the same effect of gradual, incremental loss. I think some of the best web art takes advantage of the infinite scroll; that's part of the grain of the web, a unique affordance of the material. So perhaps the long one is the more pure version, just more difficult to present.


### Struggle
I had some trouble with dealing with capitalization. For example, I and The should be replaced but are not. 

Right now, the characters in the poem aren't being stored in any way during checking, so there's no way to disassemble, remove case, and restore case and punctuation, and reassemble the poem to reprint it on each elision. This is the next step. However, the result might not be as nice; it's poetic that "I" remains while everything else is lost.

I'm sure there's also a cleaner way to refine the tester_replacer dict with RegEx.
