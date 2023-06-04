# Use the nvidia/cuda:10.2-devel-ubuntu18.04 base image
FROM nvidia/cuda:10.2-devel-ubuntu18.04

# Set the time zone to Ho Chi Minh City, Vietnam
ENV TZ=Asia/Ho_Chi_Minh
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Update the package list and install Python 3.8 and pip
RUN apt-get update && apt-get install -y python3.8 python3-pip

# Set Python 3.8 as the default python version
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1


# Set environment variables for Python 3.8
ENV PATH="/usr/bin/python3.8:${PATH}"


scenetext-v1/detection/yolov8/api.py# Install other dependencies
RUN pip3 install --upgrade pip

COPY . /craft
WORKDIR /craft

RUN pip3 install -r requirements.txt
RUN apt-get install -y libgl1-mesa-glx 
RUN ldconfig
RUN pip3 install "fastapi[all]"

EXPOSE 4002

CMD ["uvicorn", "api:app", "--reload", "--host", "0.0.0.0", "--port", "4002"]
