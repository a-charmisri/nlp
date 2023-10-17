import spacy

nlp = spacy.load("en_core_web_sm")

def evaluate_coherence(text):
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    similarities = []
    for i in range(len(sentences) - 1):
        sim = sentences[i].similarity(sentences[i+1])
        similarities.append(sim)
    coherence_score = sum(similarities) / len(similarities)
    return coherence_score
