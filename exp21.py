import nltk
from textblob import TextBlob
from nltk.corpus import wordnet

def extract_noun_phrases(sentence):
    blob = TextBlob(sentence)
    noun_phrases = []
    for np in blob.noun_phrases:
        words = nltk.word_tokenize(np)
        pos_tags = nltk.pos_tag(words)
        noun_tags = [tag[0] for tag in pos_tags if tag[1].startswith('N') or tag[1].startswith('J')]
        if len(noun_tags) > 0:
            synsets = []
            for noun in noun_tags:
                synsets += wordnet.synsets(noun)
            if len(synsets) > 0:
                meanings = set([synset.definition() for synset in synsets])
                noun_phrases.append((np, meanings))
    return noun_phrases
