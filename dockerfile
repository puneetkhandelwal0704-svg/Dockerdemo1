FROM python:3.11-slim

# Java Installation
RUN apt-get update && apt-get install -y \
    openjdk-17-jdk \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Java Home
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

# Spark Version
ENV SPARK_VERSION=3.5.1
ENV HADOOP_VERSION=3

# Download Spark
RUN wget https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.tgz \
    && tar -xzf spark-${SPARK_VERSION}-bin-hadoop3.tgz \
    && mv spark-${SPARK_VERSION}-bin-hadoop3 /opt/spark \
    && rm spark-${SPARK_VERSION}.tgz

ENV SPARK_HOME=/opt/spark

ENV PATH=$PATH:$SPARK_HOME/bin

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["spark-submit", "app.py"]