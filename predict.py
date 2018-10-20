import numpy as np
import pickle as pkl
from sklearn.metrics import classification_report 

# load test data
fileObject = open(r"C:\Users\Magdalena Deschner\git_project_newsarticles\X_test.p", "rb")
X_test = pkl.load(fileObject)
fileObject.close()

fileObject = open(r"C:\Users\Magdalena Deschner\git_project_newsarticles\y_test.p", "rb")
y_test = pkl.load(fileObject)
fileObject.close()

# load fitted tfidf vectorizer to transform test data
fileObject = open(r"C:\Users\Magdalena Deschner\git_project_newsarticles\tfidf_vectorizer.p", "rb")
tfidf = pkl.load(fileObject)
fileObject.close()

# load fitted classifier to predict category of test data
fileObject = open(r"C:\Users\Magdalena Deschner\git_project_newsarticles\clf.p", "rb")
clf = pkl.load(fileObject)
fileObject.close()

# transform test data with tfidf vectorizer
X_test = tfidf.transform(X_test)
print(X_test.shape)
print(y_test.shape)

# predict category label of test data
y_pred = clf.predict(X_test.todense())

# print classification report
#print(classification_report(y_test, y_pred))
for item1, item2 in zip(np.array(y_test), y_pred):
    print(item1, item2)