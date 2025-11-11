import joblib
import pandas as pd

p = joblib.load('models/career_classifier.pkl')
clf = p.named_steps['clf']
print('Classifier classes:', clf.classes_)
print('Num classes:', len(clf.classes_))
print('Pipeline steps:', [name for name,_ in p.steps])
prep = p.named_steps['preprocessor']
print('\nPreprocessor transformers:')
for t in prep.transformers:
    print('-', t[0], '->', type(t[1]), getattr(t[1], '__class__', t[1]))

# show a sample prediction
X = pd.DataFrame([{'degree':'B.Tech','branch':'CSE','skills':'Python|ML|SQL'}])
print('\nSample input prediction:', p.predict(X))
