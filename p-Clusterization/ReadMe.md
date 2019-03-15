# Overview
---

This section contains information about **clustering** on the example of an interesting data set - **MNIST-Fashion**.
It will also consider ways to reduce the dimension of space with the help of such tools as:
1. **PCA**
1. **Multidimensional scaling (MDS)**
1. **t-SNE**
1. **Uniform Manifold Approximation and Projection (UMAP)**


## Preparations
---

Before you run it, you should check and, if necessary, change the paths in the following files:
>1. Configs\MNIST_Fashion\configs.py:  
    - `ROOT_DIR` (full path to the folder with the main file).  
>
>2. Configs\MNIST_Fashion\helper.py:  
    - You must specify the path to the file "**configs.py**", from which the necessary variables are taken (`LOG_PATH`, `ROOT_DIR`, `ENABLE_LOGS`, etc.).

---

## Описание

В этом разделе Вы познакомитесь с таким набором данных как **MNIST Fashon**.
Это тот же самый **MNIST**, только вместо цифр используются предметы гардероба (_пальто, футболки, кеды, сумки и т.п._):

![t-shirt-01](../images/part04/mnist_tshirt-01.png)

Здесь Вы узнаете о нескольких вариантах цветовых отображений:

![some color visualization ways-01](../images/part04/some_color_visualization_ways-01.png)

Также Вы познакомитесь с такой полезной техникой как ___уменьшение размерности___ (___dimensionality reduction___).
Здесь находится несколько примеров _уменьшения размерности_ с применением таких алгоритмов как:
* ___Principal Component Analysis___ (___PCA___) - ___Метод главных компонент___.
* ___Multidimensional Scaling___ (___MDS___) - ___Многомерное шкалирование___.
* ___t-Distributed Stochastic Neighbor Embedding___ (___t-SNE___) - ___Стохастическое вложение соседей с t-распределением___.
* ___Uniform Manifold Approximation and Projection___ (___UMAP___).

Примеры работы алгоритмов _уменьшения размерности_:

**PCA**:

![PCA-01](../images/part04/pca-01.png)

**MDS**:

![MDS-01](../images/part04/mds-01.png)

**t-SNE**:

![t-SNE-01](../images/part04/tsne-01.png)

**UMAP**:

![UMAP-01](../images/part04/umap-01.png)

Здесь Вы научитесь визуализировать данные в виде _дендрограммы_:

![dendrogramm-01](../images/part04/dendrogram-03.png)

В этом разделе Вы научитесь вычислять такие метрики качества как:
* ___homogeneity___
* ___completeness___
* ___V-Measure___

Также Вы изобразите график зависимости значений этих метрик от количества кластеров и проследите за тем как меняются показатели _homogeneity, completeness, V-Measure_ с ростом числа кластеров:

![metrics values dependence of count of clusters-01](../images/part04/metrics_values_dependence_clusters_count-01.png)

В конце данного раздела Вы познакомитесь с таким понятием как ___коэффициент силуэта___ (___silhouette___) и узнаете для чего он нужен:

![silhouette-01](../images/part04/silhouette-02.png)
