# Markov phraser

Generate phrases with a character-level Markov model trained on an existing phrase list. See a [demo here](https://boulder.pythonanywhere.com) with a model trained on the names of boulder problems in the Castle Hill basin, New Zealand.

# How?

Included examples create a 3rd-order model from the included list of english words.


In the console:

	git clone git@github.com:sjmduncan/phraser.git
	cd phraser
	python console.py

Or with ```bottle```:

	pip install bottle
	git clone https://github.com/sjmduncan/phraser.git
	cd phraser
	python web.py

Then navigate to [localhost:8080](http://localhost:8080/) to see generated phrases.


Look at either ```web.py``` or ```console.py``` for usage examples.

# Requirements

* Python (2 or 3)
* A text file with a list of phrases (one per line)
* **Optional:** [bottle](http://bottlepy.org/docs/dev/index.html)
