#!/bin/bash

# Đặt tên container cần kiểm tra/xóa vào biến $container_name
container_name="craft_container_orai_v2"

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
docker build -t craft_scenetext_orai:v1 .

# run 
docker run -it --name craft_container_orai_v2 -p 4002:4002 craft_scenetext_orai:v1