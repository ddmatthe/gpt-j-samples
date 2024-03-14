
## Installing stage: ROOT
### Execute custom commands for ROOT
### Update packages and create Downloads directory for files
FROM ubuntu:22.04 as root
RUN apt-get update
RUN mkdir -p ${HOME}/Downloads
## Installing stage: python
FROM root AS python

#install compiler
RUN apt-get -y install wget gnupg && wget https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB && apt-key add GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB && rm GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB && echo "deb https://apt.repos.intel.com/oneapi all main" |tee /etc/apt/sources.list.d/oneAPI.list &&apt update && apt-get -y install intel-oneapi-compiler-dpcpp-cpp


### Setting dynamic arguments for python
ARG RECIPE_PYTHON_VERSION_ARG="3.10.9"
ENV RECIPE_PYTHON_VERSION="${RECIPE_PYTHON_VERSION_ARG}"
### Installing required packages for python
RUN apt-get -y install pkg-config make libffi-dev wget libssl-dev zlib1g-dev 
### Execute custom commands for python
RUN cd ${HOME}/Downloads && wget https://www.python.org/ftp/python/${RECIPE_PYTHON_VERSION}/Python-${RECIPE_PYTHON_VERSION}.tgz && tar -xf Python-${RECIPE_PYTHON_VERSION}.tgz && cd Python-${RECIPE_PYTHON_VERSION} && ./configure --enable-optimizations && make -j8 && make install && cd ${HOME}/Downloads && wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py && rm -rf /usr/lib/python${RECIPE_PYTHON_VERSION}/EXTERNALLY-MANAGED && ln -sf $(which python${RECIPE_PYTHON_VERSION}) /usr/local/bin/python && ln -sf $(which python${RECIPE_PYTHON_VERSION}) /usr/local/bin/python3 && ln -sf $(which python${RECIPE_PYTHON_VERSION}) /usr/bin/python

RUN apt-get -y install cmake && export CMAKE_LIBRARY_PATH=/opt/intel/oneapi/mkl/latest/lib && . /opt/intel/oneapi/setvars.sh --force &&  mkdir -p ${HOME}/Downloads/pytorch && cd ${HOME}/Downloads/pytorch && apt-get -y install intel-oneapi-mkl-devel git  && git clone  https://github.com/pytorch/pytorch.git && cd pytorch && git checkout tags/v2.2.0 && git submodule update --init --recursive && pip3 install -r requirements.txt && python3 setup.py install


RUN mkdir -p ${HOME}/Downloads/transformers && cd ${HOME}/Downloads/transformers && wget https://github.com/huggingface/transformers/archive/refs/tags/v4.38.2.tar.gz && tar xf v4.38.2.tar.gz && cd transformers-4.38.2 && python3 setup.py install

RUN mkdir -p ${HOME}/Downloads/ipex && cd ${HOME}/Downloads/ipex && wget  https://github.com/intel/intel-extension-for-pytorch/archive/refs/tags/v2.2.0+cpu.tar.gz && tar xf v2.2.0+cpu.tar.gz && cd && pip3 install -r requirements.txt && python3 setup.py install