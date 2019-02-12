"""
MNIST dimensionality reduction with TensorFlow and TensorBoard.
This demonstrates the functionality of the TensorBoard Embedding Visualization dashboard using MNIST.
https://www.tensorflow.org/versions/r0.12/how_tos/embedding_viz/index.html#tensorboard-embedding-visualization
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys

import os
import numpy as np
import pandas as pd

import tensorflow as tf
from tensorflow.contrib.tensorboard.plugins import projector
# from tensorflow.examples.tutorials.mnist import input_data

import matplotlib.pyplot as plt
from configs_MNIST_Fashion import DATA_DIR, LOG_DIR
from libs.MNIST_Fashion import mnist_reader
from libs.MNIST_Fashion.helper import get_sprite_image

FLAGS = None


def get_data():
    # Import data
    X, Y = mnist_reader.load_mnist(path=FLAGS.data_dir, kind='t10k')

    labels = ['t_shirt_top', 'trouser', 'pullover', 'dress', 'coat', 'sandal', 'shirt', 'sneaker', 'bag', 'ankle_boots']
    Y_str = np.array([labels[j] for j in Y])

    columns = ['X', 'Y', 'Y_str']
    df = pd.DataFrame(columns=columns)
    df_tmp = pd.DataFrame(columns=columns)

    df_tmp['X'] = X[:].tolist()
    df_tmp['Y'] = Y[:]
    df_tmp['Y_str'] = Y_str[:]

    df_tmp.sort_values(['Y'], ascending=[True], inplace=True, axis=0)
    labels_ids = df_tmp['Y'].unique()
    line_index = 0

    for cur_id in sorted(labels_ids):
        for cur_line in df_tmp[df_tmp['Y'] == cur_id][:100].values:
            df.loc[line_index] = [cur_line[i] for i in range(3)]
            line_index += 1

    # np.savetxt(FLAGS.data_dir + '/Xtest.tsv', X, fmt='%.6e', delimiter='\t')
    # plt.imsave(FLAGS.data_dir + '/mnist-fashion-sprite.png', get_sprite_image(X), cmap='gray')

    X = np.array([line for line in df['X'].values])

    plt.imsave(FLAGS.data_dir + '/mnist-fashion-sprite.png', get_sprite_image(X), cmap='gray')
    return df, X


def generate_embeddings():
    # Import data
    df, X = get_data()

    sess = tf.InteractiveSession()

    # Input set for Embedded TensorBoard visualization
    # Performed with cpu to conserve memory and processing power
    with tf.device("/cpu:0"):
        # tensors = tf.stack(mnist.test.images[:FLAGS.max_steps], axis=0)
        tensors = X
        # embedding = tf.Variable(tensors, trainable=False, name='MNIST-Fashion')
        embedding = tf.Variable(tensors, trainable=True, name='MNIST-Fashion')

    tf.global_variables_initializer().run()

    saver = tf.train.Saver()
    writer = tf.summary.FileWriter(FLAGS.log_dir + r'/projector', sess.graph)

    # Add embedding tensorboard visualization. Need tensorflow version
    # >= 0.12.0RC0
    config = projector.ProjectorConfig()
    embed = config.embeddings.add()
    embed.tensor_name = embedding.name
    embed.metadata_path = os.path.join(FLAGS.log_dir + r'/projector/metadata.tsv')
    embed.sprite.image_path = os.path.join(FLAGS.data_dir + '/mnist-fashion-sprite.png')

    # Specify the width and height of a single thumbnail.
    embed.sprite.single_image_dim.extend([28, 28])
    projector.visualize_embeddings(writer, config)

    saver.save(sess, os.path.join(
        FLAGS.log_dir, r'projector/a_model.ckpt'), global_step=FLAGS.max_steps)


def generate_metadata_file():
    # Import data
    df, X = get_data()

    # np.savetxt(FLAGS.data_dir + '/Ytest.tsv', Y_str, fmt='%s')
    np.savetxt(FLAGS.log_dir + r'/projector/metadata.tsv', df['Y_str'], fmt='%s')

    # def save_metadata(file):
    #     with open(file, 'w', encoding='utf-8') as f:
    #         for i in range(FLAGS.max_steps):
    #             c = np.nonzero(mnist.test.labels[::1])[1:][0][i]
    #             f.write('{}\n'.format(c))
    #
    # save_metadata(FLAGS.log_dir + r'/projector/metadata.tsv')


def main(_):
    pathToDir = FLAGS.log_dir + r'/projector'

    if tf.gfile.Exists(pathToDir):
        tf.gfile.DeleteRecursively(pathToDir)
        tf.gfile.MkDir(pathToDir)
    tf.gfile.MakeDirs(pathToDir)  # fix the directory to be created
    generate_metadata_file()
    generate_embeddings()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--fake_data', nargs='?', const=True, type=bool,
                        default=False,
                        help='If true, uses fake data for unit testing.')
    parser.add_argument('--max_steps', type=int, default=10000,
                        help='Number of steps to run trainer.')
    parser.add_argument('--data_dir', type=str,
                        default=DATA_DIR,
                        help='Directory for storing input data')
    parser.add_argument('--log_dir', type=str,
                        default=LOG_DIR,
                        help='Summaries log directory')
    FLAGS, unparsed = parser.parse_known_args()
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
