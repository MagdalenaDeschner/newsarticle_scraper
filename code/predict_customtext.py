import pickle as pkl

# load fitted tfidf vectorizer to transform test data
fileObject = open(r"C:\Users\Magdalena Deschner\git_project_newsarticles\tfidf_vectorizer.p", "rb")
tfidf = pkl.load(fileObject)
fileObject.close()

# load fitted classifier to predict category of test data
fileObject = open(r"C:\Users\Magdalena Deschner\git_project_newsarticles\clf.p", "rb")
clf = pkl.load(fileObject)
fileObject.close()

# write to be classified text
text = "bayern hat gestern gespielt, der gang ins stadion war umsonst. wieder bundesliga geschaut"

# transform text with tfidf vectorizer
text = tfidf.transform(text)

# predict category label of test data
pred = clf.predict(text.todense())
print(pred)