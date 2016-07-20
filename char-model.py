# Original article at http://nbviewer.jupyter.org/gist/yoavg/d76121dfde2618422139
#
#	Python code to implement character level language model
# to generate Shakespeare style text.

from collections import *

def train_char_lm(fname, order=4):
    data = file(fname).read()
    lm = defaultdict(Counter)
    pad = "~" * order
    data = pad + data
    for i in xrange(len(data)-order):
        history, char = data[i:i+order], data[i+order]
        lm[history][char]+=1
    def normalize(counter):
        s = float(sum(counter.values()))
        return [(c,cnt/s) for c,cnt in counter.iteritems()]
    outlm = {hist:normalize(chars) for hist, chars in lm.iteritems()}
    return outlm
    
from random import random

def generate_letter(lm, history, order):
        history = history[-order:]
        dist = lm[history]
        x = random()
        for c,v in dist:
            x = x - v
            if x <= 0: return c
            
def generate_text(lm, order, nletters=1000):
    history = "~" * order
    out = []
    for i in xrange(nletters):
        c = generate_letter(lm, history, order)
        history = history[-order:] + c
        out.append(c)
    return "".join(out)
    

print "Training model to write like Shakespeare..."
lm = train_char_lm("shakespeare-input.txt", order=10)
print "Done training."
print "Generated text:"
print generate_text(lm, 10)


"""
Training model to write like Shakespeare...
Done training.
Generated text:
First Citizen:
The king, sir, hath
danced before the Roman?

Lieutenant, is your grace's part; black and blue, that you'll make, advise me like a Fury crown'd with simular proof enough to purchase out abuses:
Therefore I'll watch you for this once. What, hast
smutch'd thy nose?
They say Edgar, his banished son, is with their power i' the eyes, but with my soul delights,
But with him.

PROSPERO:
Come forth.

MECAENAS:
We have strength can give you: live,
And bear his mind, be Edward England's coat one half-penny-worth of bread to
this intolerable.

YORK:
I am thine own so proper as to waste
His borrow'd flaunts, behold
Their infancy again
And knit our powers, with smiling rogues as these
Have moved his highness: my best train
I have from the English beach
Pales in the mask.
The heavens
Reveal the damn'd contriver; and, you know, is haunted
With a reed voice, and that will give us
Some faults to make good time!

Clown:
'O no, no, no.

EROS:
Sir, his wife and doth affliction of her tears;
"""
