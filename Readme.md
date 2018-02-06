# Markov phraser

Generate words/phrases with a character-level Markov model built from a list of other words/phrases. [Demo here](https://boulder.pythonanywhere.com) (based on the names of
boulder problems in the castle hill basin/NZ).


# How?

This is a demo which will build a 3rd order markov model from a list
of english words. It'll print 25 generated words:

	git clone git@github.com:sjmduncan/phraser.git
	cd phraser
	python console.py

There's also a demo which will run a `bottle` server so you can generate words via a web page.

	pip install bottle
	git clone https://github.com/sjmduncan/phraser.git
	cd phraser
	python web.py

Then navigate to [localhost:8080](http://localhost:8080/), click 'more' or refresh the page to generate a new list.

# Usage
Have a look at `console.py` for a simple example. The
model is build assuming one word or phrase per line of the input file
(in this case `english.txt`) where each line can include pretty much
any word/phrase/punctuation that you want.

There's a `norepeat` option to be used with the
`norepeat_buffer` option which rejects words/phrases in the
training and anything in the `norepeat_buffer`. It's
disabled by default and it should be used with caution because it can
make things really slow - particularly for higher order models and lists with more entries and/or shorter phrases.

# Requirements

* Python (2 or 3)
* A text file with a list of phrases (one per line)
* **Optional:** [bottle](http://bottlepy.org/docs/dev/index.html)

A list of english words is used for the examples in this repository (`english.txt`). You can use any list you want assuming you use one phrase/word per line. Most punctuation should work.
