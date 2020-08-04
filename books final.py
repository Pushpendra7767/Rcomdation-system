# import packages
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
# prin dataset
book = pd.read_csv("C:\\Users\\ACER\\Desktop\\scrap\\1 SC\\Recommendation system\\books.csv",encoding = "ISO-8859-1")
book.shape
book.columns
# function for book rating
def rate(m):
    h=book['Book.Rating']
    reco=book[book['Book.Rating']==m]
    return reco
v=rate(5)
# function for book title
def boo(name):
    k=book['Title']
    l=book['Book.Rating']
    ind=0
    for i in range(len(k)):
        if(name==k[i]):
            ind=i
    r=l[ind]
    reco=book[book['Book.Rating']==r]
    return reco
# print according to rating
m='More Cunning Than Man: A Social History of Rats and Man'
f=boo(m)
print(f)





