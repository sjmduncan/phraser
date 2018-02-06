#!/usr/bin/python

import markov
model3=markov.phraser('english.txt',order=3, norepeat=True, norepeat_buffer=300)
phrases=model3.genPhrases(25)
for phrase in phrases:
    print(phrase)
