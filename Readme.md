# Markov phraser

Generate words/phrases from a list of other words. Demo [here](https://boulder.pythonanywhere.com).


# How To

    >git clone git@github.com:sjmduncan/phraser.git
	>cd phraser
	>python console.py

Look at console.py for an example of how to use the `markov.phraser`
class. Also look at the `norepeat` and `norepeat_buffer` parameters of
the constructor - they can be used to avoid generating the same
phrases repeatedly and phrases which are in the original list.

## Web

	>pip install bottle
	>git clone git@github.com:sjmduncan/phraser.git
	>cd phraser
	>python web.py

Navigate to [localhost:8080](http://localhost:8080/).

## Requirements

* Python (2 or 3)
* A text file with a list of phrases (one per line)
* bottle

A list of english words is used for the examples in this repository
(`english.txt`. You can use any file containing arbitrary lines of
text. The [demo](https://boulder.pythonanywhere.com) model was built
from a list of the names of boulder problems in the castle hill basin
(NZ).
