# Udacity nd009

## Install Udacity

* pip + virtualenv
  ```
  virtualenv --python=python2 env
  source env/bin/activate
  export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.11.0rc2-py2-none-any.whl
  pip install -U $TF_BINARY_URL
  pip install -U 'ipython[notebook]'
  pip install scikit-learn pyreadline Pillow matplotlib scipy
  ```

* docker
  ```
  docker pull gcr.io/tensorflow/tensorflow
  git clone git@github.com:tensorflow/tensorflow.git
  cp tensorflow/tensorflow/examples/udacity/*.ipynb ./
  cp tensorflow/tensorflow/examples/udacity/Dockerfile ./
  docker build -t nd009 .
  ```

## Get data

on macOS, for example
```
$ wget -c http://commondatastorage.googleapis.com/books1000/notMNIST_large.tar.gz
$ shasum notMNIST_large.tar.gz
  342702831f08438e1fc830ca0f016ec7bc5ab2e8  notMNIST_large.tar.gz
$ wget -c http://commondatastorage.googleapis.com/books1000/notMNIST_small.tar.gz
$ shasum notMNIST_small.tar.gz
  23db76a71f83982f18a51b855b5746bd52e01f1c  notMNIST_small.tar.gz
```

## Run

* ipython notebook
  ```
  $ ipython notebook
  ```

* docker
  ```
  docker run -it --name tensorflow-udaicty --rm -p 8888:8888 -v `pwd`:/notebooks nd009
  ```

## References

* [TensorFlow Installation](https://www.tensorflow.org/versions/master/get_started/os_setup.html)
* [notMNIST Datasets](http://yaroslavvb.blogspot.co.uk/2011/09/notmnist-dataset.html)
* [Udacity Docker on TensorFlow Installation](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/udacity/README.md)
