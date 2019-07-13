from joblib import dump,load

def init(): 
	Classifier = load('model/spamModel/spamPredict.joblib');
	Vectorizer = load('model/spamModel/vectroizer.pk1');
	return Classifier, Vectorizer