import pandas as pd
import pickle as pkl 
from sklearn.feature_extraction.text import TfidfVectorizer

# load articles from stored pickle file
fileObject = open(r"C:\Users\Magdalena Deschner\git_project_newsarticles\articles.p", "rb")
articles = pkl.load(fileObject)
fileObject.close()

# check size of data
print(articles.shape)

# todo: fit tfidf on training data

# transform article bodies to list
corpus = [body for body in articles.loc[:,"body"]]

# vectorize corpus with tfidf
tfidf = TfidfVectorizer()
articles_vectorized = tfidf.fit_transform(corpus)

# store as dataframe
articles_preprocessed_df = pd.DataFrame(articles_vectorized.todense())
articles_preprocessed_df.columns = tfidf.get_feature_names()

fileObject = open(r"C:\Users\Magdalena Deschner\git_project_newsarticles\articles_preprocessed_df.p", "wb")
pkl.dump(articles_preprocessed_df, fileObject)
fileObject.close()

# store as sparse matrix
articles_preprocessed_mat = articles_vectorized

fileObject = open(r"C:\Users\Magdalena Deschner\git_project_newsarticles\articles_preprocessed_mat.p", "wb")
pkl.dump(articles_preprocessed_df, fileObject)
fileObject.close()