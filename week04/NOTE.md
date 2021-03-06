## 学习笔记
### Pandas基本数据结构
1. Series：一种类似于一维数组的对象，是由一组数据(各种NumPy数据类型)以及一组与之相关的数据标签(即索引)组成。仅由一组数据也可产生简单的Series对象。注意：Series中的索引值是可以重复的。

2. DataFrame：一个表格型的数据结构，包含有一组有序的列，每列可以是不同的值类型(数值、字符串、布尔型等)，DataFrame即有行索引也有列索引，可以被看做是由Series组成的字典。

### 数据预处理
1. 缺失值处理： (使用平均值填充/前向填充/缺失值删除)
2. 重复值处理： 删除

### jieba
中文分词库，提供三种分词模式：
1. 精确模式：试图将句子最精确地切开，适合文本分析
2. 全模式：把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义
3. 搜索引擎模式：在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。  

[学习文档](https://github.com/fxsjy/jieba/blob/master/README.md)
### SnowNLP情感倾向分析
文本情感分析是指用自然语言处理、文本挖掘以及计算机语言学等方法来识别和提取原素材中的主观信息，其主要任务就是对文本中的主观信息（如观点、情感、态度、评价、情绪等）进行提取、分析、处理、归纳和推理。  
[学习文档](https://github.com/isnowfy/snownlp/blob/master/README.md)