## INSTALLATION

After testing, PaddleOCR can run on glibc 2.23. You can also test other glibc versions or install glic 2.23 for the best compatibility.

PaddleOCR working environment:

- PaddlePaddle 2.0.0
- python3.7
- glibc 2.23

It is recommended to use the docker provided by us to run PaddleOCR, please refer to the use of docker [link](https://www.runoob.com/docker/docker-tutorial.html/).

**1. Prepare the docker environment**

```
# Switch to the working directory
cd /home/Projects

# Create a docker container named ppocr and map the current directory to the /paddle directory of the container
# If using CPU, use docker instead of nvidia-docker to create docker
sudo nvidia-docker run --name ppocr -v $PWD:/paddle --network=host -it  paddlepaddle/paddle:latest-dev-cuda10.1-cudnn7-gcc82 /bin/bash
```

If using CUDA10, please run the following command to create a container.
It is recommended to set a shared memory greater than or equal to 32G through the --shm-size parameter:

```
sudo nvidia-docker run --name ppocr -v $PWD:/paddle --shm-size=64G --network=host -it paddlepaddle/paddle:latest-dev-cuda10.1-cudnn7-gcc82 /bin/bash
```

You can also visit [DockerHub](https://hub.docker.com/r/paddlepaddle/paddle/tags/) to get the image that fits your machine.

```
# ctrl+P+Q to exit docker, to re-enter docker using the following command:
sudo docker container exec -it ppocr /bin/bash
```

**2. Install the latest PaddlePaddle**

```
pip3 install --upgrade pip

# If you have cuda9 or cuda10 installed on your machine, please run the following command to install
python3 -m pip install paddlepaddle-gpu==2.0.0 -i https://mirror.baidu.com/pypi/simple

# If you only have cpu on your machine, please run the following command to install
python3 -m pip install paddlepaddle==2.0.0 -i https://mirror.baidu.com/pypi/simple
```

For more software version requirements, please refer to the instructions in [Installation Document](https://www.paddlepaddle.org.cn/install/quick) for operation.

**3. Clone the PaddleOCR repo**

```
# Recommend
git clone https://github.com/PaddlePaddle/PaddleOCR

# If you cannot pull successfully due to network problems, you can also choose to use the code hosting on gitee:

git clone https://gitee.com/paddlepaddle/PaddleOCR

# Note: The cloud-hosting code may not be able to synchronize the update with this GitHub project in real time. There might be a delay of 3-5 days.
```

**4. Install the third-party libraries**

```
cd PaddleOCR
pip3 install -r requirements.txt
```

