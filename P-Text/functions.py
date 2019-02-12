# -*- coding: utf-8 -*-

from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.tokenize import RegexpTokenizer
import numpy as np
import matplotlib.pyplot as plt


def split_vectorize(X, y, method, n=None):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    
    if method == 'bow':
        vectorizer = CountVectorizer()
        X_train_vec = vectorizer.fit_transform(X_train)
        X_test_vec = vectorizer.transform(X_test)
    
    if method == 'tfidf':
        vectorizer = TfidfVectorizer()
        X_train_vec = vectorizer.fit_transform(X_train)
        X_test_vec = vectorizer.transform(X_test)
    
    if method == 'doc2vec':
        tokenizer = RegexpTokenizer(r'\w+')          
        
        tagged_values = [TaggedDocument(words=tokenizer.tokenize(x.lower()), tags=[tag]) for (x, tag) in zip(X, y)]       
        doc2vec_model = Doc2Vec(tagged_values, window=10, vector_size=20, dm=0, hs=1, workers=4)
        
        descriptions_train = [doc2vec_model.infer_vector(tokenizer.tokenize(doc.lower()), steps=20) for doc in X_train]
        X_train_vec = np.vstack(descriptions_train)
        descriptions_test = [doc2vec_model.infer_vector(tokenizer.tokenize(doc.lower()), steps=20) for doc in X_test]
        X_test_vec = np.vstack(descriptions_test)
        
        vectorizer = doc2vec_model
    
    if method == 'ngramm':
        vectorizer = CountVectorizer(ngram_range=(n, n))
        X_train_vec = vectorizer.fit_transform(X_train)
        X_test_vec = vectorizer.transform(X_test)
    
    return vectorizer, X_train_vec, X_test_vec, y_train, y_test

	
def get_important_words(vectorizer, clf, x_train, n=10):
    tokenizer = RegexpTokenizer(r'\w+')   
    words = set(tokenizer.tokenize(" ".join(x_train).lower()))
    
    if type(vectorizer) == type(Doc2Vec()):
        word_vecs = [([vectorizer.infer_vector([word], steps=20)], word) for word in words]
    else:
        word_vecs = [(vectorizer.transform([word]), word) for word in words]
        
    probas = [(clf.predict_proba(word_vec)[0, 1], word) for (word_vec, word) in word_vecs]	
    probas.sort(key=lambda x: x[0], reverse=True)
    
    top = probas[:n]
    bottom = probas[-n:]
	
    return top, bottom


def plot_important_words(vectorizer, model, x_train, n=10):    
    importance = get_important_words(vectorizer, model, x_train, n)
    
    top_scores = [a[0] for a in importance[0]]
    top_words = [a[1] for a in importance[0]]
    bottom_scores = [1 - a[0] for a in importance[1]]
    bottom_words = [a[1] for a in importance[1]]
    
    y_pos = np.arange(len(top_words))
    top_pairs = [(a, b) for a,b in zip(top_words, top_scores)]
    top_pairs = sorted(top_pairs, key=lambda x: x[1])
    
    bottom_pairs = [(a, b) for a,b in zip(bottom_words, bottom_scores)]
    
    top_words = [a[0] for a in top_pairs]
    top_scores = [a[1] for a in top_pairs]
    
    bottom_words = [a[0] for a in bottom_pairs]
    bottom_scores = [a[1] for a in bottom_pairs]
    
    fig = plt.figure(figsize=(8, 8))  

    plt.subplot(121)
    plt.barh(y_pos, bottom_scores, align='center', alpha=0.5)
    plt.title("Негативные", fontsize=20)
    plt.yticks(y_pos, bottom_words, fontsize=14)
    plt.xlabel("Вероятность", fontsize=20)
    
    plt.subplot(122)
    plt.barh(y_pos,top_scores, align='center', alpha=0.5)
    plt.title("Позитивные", fontsize=20)
    plt.yticks(y_pos, top_words, fontsize=14)
    plt.suptitle("Самые важные слова", fontsize=16)
    plt.xlabel("Вероятность", fontsize=20)
    
    plt.subplots_adjust(wspace=0.8)
    plt.show()


def get_important_words_2(vectorizer, model, n=10):
    index_to_word = {v: k for k, v in vectorizer.vocabulary_.items()}
    
    word_importances = [(el, index_to_word[i]) for (i, el) in enumerate(model.coef_[0])]
    sorted_coeff = sorted(word_importances, key=lambda x : x[0], reverse=True)
    top = sorted_coeff[:n]
    bottom = sorted_coeff[-n:]

    return top, bottom


def plot_important_words_2(vectorizer, model, n=10):
    importance = get_important_words_2(vectorizer, model, n)
    
    top_scores = [a[0] for a in importance[0]]
    top_words = [a[1] for a in importance[0]]
    bottom_scores = [a[0] for a in importance[1]]
    bottom_words = [a[1] for a in importance[1]]
    
    y_pos = np.arange(len(top_words))
    top_pairs = [(a, b) for a, b in zip(top_words, top_scores)]
    top_pairs = sorted(top_pairs, key=lambda x: x[1])
    
    bottom_pairs = [(a, b) for a, b in zip(bottom_words, bottom_scores)]
    bottom_pairs = sorted(bottom_pairs, key=lambda x: x[1], reverse=True)
    
    top_words = [a[0] for a in top_pairs]
    top_scores = [a[1] for a in top_pairs]
    
    bottom_words = [a[0] for a in bottom_pairs]
    bottom_scores = [a[1] for a in bottom_pairs]
    
    fig = plt.figure(figsize=(10, 10))  

    plt.subplot(121)
    plt.barh(y_pos, bottom_scores, align='center', alpha=0.5)
    plt.title("Негативные", fontsize=20)
    plt.yticks(y_pos, bottom_words, fontsize=14)
    plt.xlabel("Значимость", fontsize=20)
    
    plt.subplot(122)
    plt.barh(y_pos, top_scores, align='center', alpha=0.5)
    plt.title("Позитивные", fontsize=20)
    plt.yticks(y_pos, top_words, fontsize=14)
    plt.suptitle("Самые важные слова", fontsize=16)
    plt.xlabel("Значимость", fontsize=20)
    
    plt.subplots_adjust(wspace=0.8)
    plt.show()

	
def vectorize(vectorizer, text):    
    if type(vectorizer) == type(Doc2Vec()):
        tokenizer = RegexpTokenizer(r'\w+')   
        words = tokenizer.tokenize(text.lower())
        
        word_vecs = [vectorizer.infer_vector(words, steps=20)]
    else:
        word_vecs = vectorizer.transform([text])
    
    return word_vecs
