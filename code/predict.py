import numpy as np
import pickle as pkl
from sklearn.metrics import classification_report, confusion_matrix 

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

# predict category label of test data
y_pred = clf.predict(X_test.todense())

# print classification report
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print("Test accuracy: {}".format(round(clf.score(X_test.toarray(), y_test),2)))