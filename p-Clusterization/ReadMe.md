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
    - ROOT_DIR (full path to the folder with the main file).
>
>2. Configs\MNIST_Fashion\helper.py:
    - You must specify the path to the file "configs.py", from which the necessary variables are taken (LOG_PATH, ROOT_DIR, ENABLE_LOGS, etc.).
