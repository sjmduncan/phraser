import random
import json
import operator
from collections import OrderedDict

class phraser:
    def __init__(self, filename='', order=1, norepeat_buffer=10,norepeat=False):
        if not filename == '':
            self.filename=filename
            self.genModel(filename, order)
        
        # Store recent phrases to avoid repeating too often
        self.recents=[]
        self.recent_max_count=norepeat_buffer
        self.norepeat=norepeat
    
    def load(self, jsonfile):
        # Create/clear the recent phrase list. Also clear any existing
        # phrases (e.g. from an existing learned model)
        self.recents=[]
        self.phrases=[]

        # Loading a model (instead of learning from a phrase list)
        # means that there is no list of phrases for rejecting
        # non-unique phrases
        self.loaded=True
        
        f=open(jsonfile, 'r')

        # Use OrderedDict because the character prediction expects
        # cumulative counts when iterating through keys
        self.model=json.loads(f.read(), object_pairs_hook=OrderedDict)

        # Use a really long key to store the markov order (surely
        # nobody wants a 22nd-order markov filter)
        self.order=self.model['dict-hack-markov-order']
        
    def save(self, filename):
        f=open(filename, 'w')
        f.write(json.dumps(self.model))
        
    def genModel(self,filename, markov_ord=1):
        # Not loading a JSON model, so there's a phrase list to reject from
        self.loaded=False
        self.phrases = []
        self.order=markov_ord
        self.recents=[]
        
        f=open(filename,'r')
        lines = f.read().split('\n')
            
        # Model is stored as a dict-of-dicts, create the base dict here
        model = {}

        # Empty char denotes the start of a phrase, create 
        model[''] = {}

        for l in lines:
            phrase=''
            line=l.lower()+'\n'
            for c in line:
                k=phrase[-self.order:]
                if k not in model:
                    model[k] = {}
                    
                if c not in model[k]:
                    model[k][c] = 0
                
                model[k][c] += 1

                phrase = phrase + c

            # Trim the newline off the end of the phrase
            if(len(phrase)>2):
                self.phrases.append(phrase[:-1])

        # Convert char-count for each key to the cumulative count
        # (order is now important)
        for d in model:
            total=0
            for c in model[d]:
                total += model[d][c]
                model[d][c] = total
        model['dict-hack-markov-order']=self.order
        self.model=model

    def genLetter(self,phrase):
        k=phrase[-self.order:]
        cran=random.randint(1,max(self.model[k].values()))
        for c in self.model[k]:
            if self.model[k][c] >= cran:
                return c
        print("--------something broke-------")
        return '\n'

    def genPhrase(self,min=1, max=-1):
        while True:
            letter=''
            phrase=''
            while True:
                letter = self.genLetter(phrase);
                if letter == '\n':
                    break;
                phrase = phrase + letter
            exists=False
            l=len(phrase)

            # If this was loaded instead of learned then there is no
            # word list to check against. So don't check
            if self.norepeat:
                for ph in self.phrases:
                    if (phrase in ph) or (ph in phrase):
                        exists=True
                        break;

            if (l>=min and (max<0 or l<=max)):
                if (not self.norepeat) or ((not exists) and (phrase not in self.recents)):
                    self.recents.append(phrase)
                    if len(self.recents)>self.recent_max_count:
                        self.recents.remove(self.recents[0])
                    return phrase

    def genPhrases(self,n, min=-1, max=-1, v=False):
        phrases=[]
        for i in range(n):
            phrase=self.genPhrase(min,max)
            phrases.append(phrase)
            if v:
                print(phrases)
        return phrases


