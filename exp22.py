import spacy
import neuralcoref

nlp = spacy.load("en_core_web_sm")
neuralcoref.add_to_pipe(nlp)

def resolve_references(text):
    doc = nlp(text)
    resolved_text = doc._.coref_resolved
    return resolved_text
