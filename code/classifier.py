from sklearn.naive_bayes import GaussianNB
import pickle as pkl

# load training data
fileObject = open(r"C:\Users\Magdalena Deschner\git_project_newsarticles\articles_preprocessed_df.p", "rb")
X_train = pkl.load(fileObject)
fileObject.close()

fileObject = open(r"C:\Users\Magdalena Deschner\git_project_newsarticles\y_train.p", "rb")
y_train = pkl.load(fileObject)
fileObject.close()

# inspect training data
# print(X_train.head()
# print(X_train.info())
# print(X_train.shape)
# print(y_train)
# print(y_train.shape)

# fit classifier
clf = GaussianNB()
clf.fit(X_train, y_train)

# pickle classifier
fileObject = open(r"C:\Users\Magdalena Deschner\git_project_newsarticles\clf.p", "wb")
pkl.dump(clf, fileObject)
fileObject.close()