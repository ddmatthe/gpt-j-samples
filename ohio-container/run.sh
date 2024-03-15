docker build -t mytorch:latest .
docker run -it --rm --privileged -v $(pwd)/../bare-metal/:/mnt/scripts -v ${HOME}/.cache/huggingface/hub:/root/.cache/huggingface/hub -e TRANSFORMERS_CACHE=/root/.cache/huggingface/hub mytorch:latest  python /mnt/scripts/simple-gpt-j.py
