#!/bin/bash


# copy weight
cp -r ../../weights/rec/best_parseq.ckpt .

# Đặt tên container cần kiểm tra/xóa vào biến $container_name
container_name="parseq_container_orai_v1"

# Kiểm tra xem container đã tồn tại hay chưa
if docker ps -a --format '{{.Names}}' | grep -Eq "^${container_name}\$"; then
  # Nếu container tồn tại thì xóa container
  docker stop $container_name
  docker rm $container_name
  echo "Delete container $container_name"
else
  # Nếu container không tồn tại thì in ra thông báo
  echo "Not found container $container_name"
fi

# buiild
# docker build -t parseq_scenetext_orai:v1 .

# run 
docker run -it --name parseq_container_orai_v1 -p 4003:4003 -v $(pwd):/parseq parseq_scenetext_orai:v1