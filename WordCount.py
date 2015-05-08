from pyspark import SparkContext

inputFile = "file:/wordcount/input/Had*"
sc = SparkContext("local", "Simple App")
inputData = sc.textFile(inputFile).cache()

counts = inputData.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)

counts.saveAsTextFile("file:/wordcount/output/counts")
