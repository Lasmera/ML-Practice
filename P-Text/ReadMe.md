# Overview

In this section, you will learn how to train a model that determines whether an expression is positive or negative.

In the process of achieving this goal, you will learn about the following things:
1. Preprocessing of data.
1. The use of stop words.
1. Converting text to numeric characters (vectorization). In this case, you will get acquainted with the algorithms:
  1. Bag of words (BoW)
  1. TF-IDF
  1. word2vec
1. Confusion matrix
1. Latent Dirichlet allocation (LDA)

---

## Подробности

В данном разделе Вы построите модель, которая, по произвольному тексту, будет определять контекст переданного текста (_негативный_ или _позитивный_).

Во время предобработки данных, Вы будете использовать такие вещи как _стоп-слова_, _токенизация_, _нормализация_.

А также познакомитесь с такой вещью как ___векторизация___ и с методами её достижения (одни из них так называемый ___мешок слов___).
Научитесь строить ___матрицу неточностей___ (___confusion matrix___).
