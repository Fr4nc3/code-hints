Fr4nc3
==========
SpellChecker.java
words.txt
filetospellcheck.txt
KBestCounter.java
TestKBest.java
README.txt


Programming Question 1
======================
from the book
5.21 Implement a spelling checker by using a hash table. Assume that the dictionary
comes from two sources: an existing large dictionary and a second file containing
a personal dictionary. Output all misspelled words and the line numbers in which
they occur. Also, for each misspelled word, list any words in the dictionary that are
obtainable by applying any of the following rules:
a. Add one character.
b. Remove one character.
c. Exchange adjacent characters.

from HW4 description:
Based on Weiss Exercise 5.21 implement
this problem as described with the
exception of the secondary dictionary.

text example from here
http://www.mrc-cbu.cam.ac.uk/people/matt.davis/cmabridge/

to clean up accents from the dictionary string // I didn't used it
http://stackoverflow.com/questions/3322152/is-there-a-way-to-get-rid-of-accents-and-convert-a-whole-string-to-regular-lette
Input:  orčpžsíáýd
Output: orcpzsiayd


https://piazza.com/class/ijfyurrye2g1oc?cid=515
I will return a list of suggestions for a misspelled word.
http://stackoverflow.com/questions/5057156/merging-lists-into-a-single-array-with-unique-elements
just in case I got the same string of suggestion

at last I used this to convert my list to string, at the end I did same TestKBest []
http://stackoverflow.com/questions/599161/best-way-to-convert-an-arraylist-to-a-string


Programming Question 2
======================

conver priority queue to list
http://stackoverflow.com/questions/12779839/convert-a-queue-to-list
sort the list
http://stackoverflow.com/questions/18073590/sort-list-in-reverse-order