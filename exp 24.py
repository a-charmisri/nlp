import spacy

nlp = spacy.load("en_core_web_sm")

def recognize_dialog_acts(dialog):
    doc = nlp(dialog)
    dialog_acts = []
    for sent in doc.sents:
        if "?" in sent.text:
            dialog_acts.append("question")
        elif "!" in sent.text:
            dialog_acts.append("exclamation")
        else:
            dialog_acts.append("statement")
    return dialog_acts
