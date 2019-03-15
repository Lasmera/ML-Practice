# Overview

This section contains information on anomaly detection in datasets.

---

## Описание

В этом разделе Вы узнаете как можно находить _аномалии_ в данных.
В качестве набора данных используется набор данных _Сбербанка_.

Здесь Вы будете применять такие методы и техники как:
* Кодирование строковых значений (_регионов_) в числовые.
* Преобразования _MinMax_, _StandartScaler_.
* Заполнение пустых значений.
* Уменьшение размерности данных с помощью _principal component analysis_ (_PCA_) и _t-distributed Stochastic Neighbor Embedding_ (_t-SNE_).
* Визуализация данных с помощью _обычных_ и _интерактивных_ графиков.

Ниже показано несколько примеров:

Обнаружение аномалий на плоскости после уменьшения размерности методами _PCA_ и _t-SNE_ для региона _Москва_:

![anomaly detection after pca and tsne for Moscow-01](../images/part06/anomaly_detection_pca_tsne_moscow-01.png)

Обнаружение аномалий в начальном пространстве и отображение на плоскости методами _PCA_ и _t-SNE_ для региона _Москва_:

![anomaly detection after pca and tsne for Moscow-02](../images/part06/anomaly_detection_source_pca_tsne_moscow-01.png)

Проверка исходных данных по региону _Москва_:
* _MinMax_:

![anomaly detection source for Moscow (MinMax)-01](../images/part06/anomaly_detection_source_moscow_minmax-01.png)

* _STD_:

![anomaly detection source for Moscow (STD)-01](../images/part06/anomaly_detection_source_moscow_std-01.png)

Проверка исходных данных по региону _Санкт-Петербург_:
* _MinMax_:

![anomaly detection source for Saint-Petersburg (MinMax)-01](../images/part06/anomaly_detection_source_stpeterburg_minmax-01.png)

* _STD_:

![anomaly detection source for Saint-Petersburg (STD)-01](../images/part06/anomaly_detection_source_stpeterburg_std-01.png)

Пример интерактивного графика:

![anomaly-01](../images/part06/anomaly-02.gif)

Пример аномалии на наборе данных **MNIST Fashion**:

![t-SNE MNIST Fashion-01](../images/part06/tsne_mnist_fashion-02.gif)
