from nltk.tokenize import sent_tokenize
import pandas as pd
import pickle as pkl 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# load articles from stored pickle file
fileObject = open(r"C:\Users\Magdalena Deschner\git_project_newsarticles\articles.p", "rb")
articles = pkl.load(fileObject)
fileObject.close()

# check size of data
print(articles.shape)

# split news articles into sentences
# articles["body_sent"] = articles.body.apply(sent_tokenize)
# print(articles.iloc[9,:])

# get distribution of category labels
print(articles.category.value_counts())

# split data into body and label
body = articles.body
label = articles.category

# split data into train and test
X_train, X_test, y_train, y_test = train_test_split(body, label, stratify=label)

fileObject = open(r"C:\Users\Magdalena Deschner\git_project_newsarticles\X_test.p", "wb")
pkl.dump(X_test, fileObject)
fileObject.close()

fileObject = open(r"C:\Users\Magdalena Deschner\git_project_newsarticles\y_train.p", "wb")
pkl.dump(y_train, fileObject)
fileObject.close()

fileObject = open(r"C:\Users\Magdalena Deschner\git_project_newsarticles\y_test.p", "wb")
pkl.dump(y_test, fileObject)
fileObject.close()

# fit tfidf on training data
tfidf = TfidfVectorizer()
tfidf_fitted = tfidf.fit(X_train)
X_train_vect = tfidf_fitted.transform(X_train)

# store fitted tfidf vectorizer
fileObject = open(r"C:\Users\Magdalena Deschner\git_project_newsarticles\tfidf_vectorizer.p", "wb")
pkl.dump(tfidf_fitted, fileObject)
fileObject.close()

# store as dataframe
articles_preprocessed_df = pd.DataFrame(X_train_vect.todense())
articles_preprocessed_df.columns = tfidf.get_feature_names()

fileObject = open(r"C:\Users\Magdalena Deschner\git_project_newsarticles\articles_preprocessed_df.p", "wb")
pkl.dump(articles_preprocessed_df, fileObject)
fileObject.close()