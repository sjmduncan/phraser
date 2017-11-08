# Markov phraser

Generate words/phrases from a list of other words.  [Demo
here](https://boulder.pythonanywhere.com) (based on the names of
boulder problems in the castle hill basin in NZ).


# How To

This is a demo which will build a 4th order markov model from a list
of english words. It'll print 25 generated words

    git clone git@github.com:sjmduncan/phraser.git
    cd phraser
    python console.py

There's also a demo which uses bottle so you can generate words from a
web browser.

	pip install bottle
	git clone https://github.com/sjmduncan/phraser.git
	cd phraser
	python web.py

Navigate to [localhost:8080](http://localhost:8080/).

For an example of how to use this have a look at `console.py`. The
model is build assuming one word or phrase per line of the input file
(in this case `english.txt`) where each line can include pretty much
any word/phrase/punctuation that you want.

There's also a **`norepeat`** option to be used with the
**`norepeat_buffer`** option which means that words/phrases in the
training and anything in the `norepeat_buffer` will be rejected. It's
off by default, and it should be used with caution, because it can
make things really slow, particularly for higher order models.

## Requirements

* Python (2 or 3, for the web demo make sure bottle is installed correctly)
* A text file with a list of phrases (one per line)
* bottle

A list of english words is used for the examples in this repository
(`english.txt`). You can use any file containing arbitrary lines of
text. The [demo](https://boulder.pythonanywhere.com) model was built
from a list of boulder problem names.
