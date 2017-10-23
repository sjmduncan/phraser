import markov
model4=markov.phraser('english.txt', 4,700)
phrases=model4.genPhrases(25)
for phrase in phrases:
    print(phrase)
