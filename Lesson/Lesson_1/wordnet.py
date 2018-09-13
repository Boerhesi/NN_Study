from nltk.corpus import wordnet as wn

panda = wn.synset('panda.n.01')
hyper = lambda s: s.hypernyms()
results = list(panda.closure(hyper))
for result in results:
    print result
