#!/bin/bash

# copy weight
cp -r ../../weights/detect/model_yolov8.pt .

# Đặt tên container cần kiểm tra/xóa vào biến $container_name
container_name="yolov8_container_orai_v1"

# Kiểm tra xem container đã tồn tại hay chưa
if docker ps -a --format '{{.Names}}' | grep -Eq "^${container_name}\$"; then
  docker stop $container_name
  docker rm $container_name
  echo "Delete container $container_name"
else
  echo "Not found container $container_name"
fi

# buiild
docker build -t yolov8_scenetext_orai:v1 .

# run 
docker run -it --name yolov8_container_orai_v1 -p 4001:4001 yolov8_scenetext_orai:v1