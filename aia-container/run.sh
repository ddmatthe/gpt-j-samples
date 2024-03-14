docker run -it --rm --privileged -v $(pwd)/../bare-metal/:/mnt/scripts -v ${HOME}/.cache/huggingface/hub:/root/.cache/huggingface/hub -e TRANSFORMERS_CACHE=/root/.cache/huggingface/hub  intel/language-modeling:centos-pytorch-cpu-bert-large-inference python /mnt/scripts/simple-gpt-j.py


#docker run -it --rm -v ${HOME}/models:/mnt/models -v $(pwd)/../bare-metal/:/mnt/scripts -v ${HOME}/.cache/huggingface:/root/.cache/huggingface/  intel/language-modeling:centos-pytorch-cpu-bert-large-inference python3 /mnt/scripts/simple-gpt-j.py /root/.cache/huggingface/hub/models--EleutherAI--gpt-j-6B/snapshots/b71ae8bc86cac13154e03e92b5855203086b722e/ #using whole cache path
#need to provide the cache location
