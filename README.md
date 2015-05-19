# WordCount example application 

## **Pre-requisites**:

#### **Install docker**: 
[Docker Installation](https://docs.docker.com/installation/)

#### **Download WordCount.py**: 
[WordCount.py](https://github.com/ksriraman/cdh5-spark-wordcount-docker/blob/master/WordCount.py)

#### **Pull Docker image**:
```docker pull karthicks/cdh5-spark-docker```

## **Execution**:

### **Run image in background and mount WordCount.py**:
As needed, replace '/root' below with folder containing WordCount.py

```docker run -td -v /root/WordCount.py:/WordCount.py karthicks/cdh5-spark-docker:latest```

#### **Enter docker bash shell (Replace CONTAINERID from above output)**:
```docker exec -i -t CONTAINERID bash -l```

#### **Run WordCount application**:
```python WordCount.py```

####**Verify Output**:
```more /wordcount/output/counts/part-0000*```

-----------------------------------------------------------------------------------------------------------

##### This example uses the [cdh-spark image](https://registry.hub.docker.com/u/ypandit/cdh-spark/) contributed by [ypandit ](https://hub.docker.com/u/ypandit/):
