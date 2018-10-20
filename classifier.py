import pickle as pkl

fileObject = open(r"C:\Users\Magdalena Deschner\git_project_newsarticles\articles_preprocessed_df.p", "rb")
articles_preprocessed_df = pkl.load(fileObject)
fileObject.close()

print(articles_preprocessed_df.head())
print(articles_preprocessed_df.info())