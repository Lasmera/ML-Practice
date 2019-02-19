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

## Описание

В данном разделе Вы построите модель, которая, по произвольному тексту, будет определять контекст переданного текста (_негативный_ или _позитивный_).

Для предобработки данных, Вы будете использовать такие вещи как _стоп-слова_, _токенизация_, _нормализация_ и увидите как они влияют на конечный результат.

Также Вы познакомитесь с такой вещью как ___векторизация___ и с методами её реализации (___мешок слов___ (_bag of words_), ___TF-IDF___, ___Word2vec___, ___Doc2vec___).
Научитесь строить ___матрицу неточностей___ (___confusion matrix___):

![confusion_matrix-01](../images/part02/confusion_matrix01.png)

Создадите процедуру выявления наиболее значительных слов отражающих _позитивный_ и _негативный_ контексты:

![important_words-01](../images/part02/important_words01.png)

Узнаете, что такое ___латентное размещение Дирихле___ (_Latent Dirichlet allocation_ - _LDA_), зачем оно нужно и как оно может помочь.
Попробуете сгруппировать исходный текст по нескольким темам, а также узнаете как можно найти оптимальное их количество.

![optimal_themes-01](../images/part02/optimal_themes01.png)

Проведём анализ количества документов которые попали в определённую тему.
Создадим процедуру для отображения, через которую визуализируем количество _позитивных_ и _негативных_ отзывов в каждой теме.

![result-01](../images/part02/result01.png)
