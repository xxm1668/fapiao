#/bin/sh

HOST_ROOT_DIR=`pwd`
docker_img=$3


docker network create --subnet=11.10.10.0/24 onlyou_network

NV_GPU=$2 nvidia-docker run --runtime=nvidia -it --net onlyou_network  --ip $1 --shm-size=16G -v /ds/:/ds -v $HOST_ROOT_DIR/model:/s/model  -v $HOST_ROOT_DIR/api:/s/api $docker_img

