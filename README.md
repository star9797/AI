# Artificial-Identification
目录
1.目前进度	1
2.目前代码的思路	1
3.python模块	1
4.后续代码思路	5
5.完善	5

人脸识别
1.目前进度
可以对文件夹下的人脸进行检测，并且提取关键点，描出人脸。并且能判断被识别的人脸与人脸库中的人脸进行对比，得出与其最像的人或者说是同一个人。
2.目前代码的思路
先对候选人进行人脸检测、关键点提取、描述子生成后，把候选人描述子保存起来。
然后对测试人脸进行人脸检测、关键点提取、描述子生成。
最后求测试图像人脸描述子和候选人脸描述子之间的欧氏距离，距离最小者判定为同一个人。
3.python模块
运用到的模块：os, dlib, glob, numpy
os：语义为操作系统，是操作系统相关的功能，可以处理文件和目录这些我们日常手动需要做的操作，就比如说：显示当前目录下所有文件/删除某个文件/获取文件大小……
另外，os模块不受平台限制，也就是说：当我们要在linux中显示当前路径时就要用到pwd命令，而Windows中cmd命令行下就要用到这个，这时候我们使用python中os模块的os.path.abspath(name)功能，无论是linux或者Windows都可以获取当前的绝对路径。
也就是说如果你希望你的程序能够与平台无关的话，这个模块是尤为重要的。
os模块的常用功能：
os.name      #显示当前使用的平台
os.getcwd()      #显示当前python脚本工作路径
os.listdir('dirname')        #返回指定目录下的所有文件和目录名
os.remove('filename')       #删除一个文件
 os.makedirs('dirname/dirname')     #可生成多层递规目录
os.rmdir('dirname')     #删除单级目录
os.rename("oldname","newname")    #重命名文件
os.system()    #运行shell命令,注意：这里是打开一个新的shell，运行命令，当命令结束后，关闭shell
os.sep    #显示当前平台下路径分隔符
os.linesep    #给出当前平台使用的行终止符
os.environ    #获取系统环境变量
os.path.abspath(path)    #显示当前绝对路径
os.path.dirname(path)    #返回该路径的父目录
os.path.basename(path)    #返回该路径的最后一个目录或者文件,如果path以／或\结尾，那么就会返回空值。
os.path.isfile(path)     #如果path是一个文件，则返回True
os.path.isdir(path)    #如果path是一个目录，则返回True
os.stat()    #获取文件或者目录信息
os.path.split(path)  #将path分割成路径名和文件名。（事实上，如果你完全使用目录，它也会将最后一个目录作为文件名而分离，同时它不会判断文件或目录是否存在）
os.path.join(path,name)   #连接目录与文件名或目录 结果为path/name
Dlib：Dlib是一个包含机器学习算法的C++开源工具包。Dlib可以帮助您创建很多复杂的机器学习方面的软件来帮助解决实际问题。目前Dlib已经被广泛的用在行业和学术领域，包括机器人，嵌入式设备，移动电话和大型高性能计算环境。
Dlib是开源的、免费的；官网和gitbi地址；官网：
http://dlib.net/#githubhttps://github.com/davisking/dlib 
Dlib的主要特点:
文档齐全
不像很多其他的开源库一样，Dlib为每一个类和函数提供了完整的文档说明。同时，还提供了debug模式；打开debug模式后，用户可以调试代码，查看变量和对象的值，快速定位错误点。另外，Dlib还提供了大量的实例。
高质量的可移植代码
Dlib不依赖第三方库，无须安装和配置，这部分可参照(官网左侧树形目录的how to compile的介绍)。Dlib可用在window、Mac OS、Linux系统上。
提供大量的机器学习 / 图像处理算法
>> 深度学习
>> 基于SVM的分类和递归算法
>> 针对大规模分类和递归的降维方法
>> 相关向量机(relevance vector machine);是与支持向量机相同的函数形式稀疏概率模型,对未知函数进行预测或分类。其训练是在贝叶斯框架下进行的,与SVM相比,不需要估计正则化参数,其核函数也不需要满足Mercer条件,需要更少的相关向量,训练时间长,测试时间短。
>> 聚类: linear or kernel k-means, Chinese Whispers, and Newman clustering. Radial Basis Function Networks
>> 多层感知机
Glob：glob.glob()返回的是列表 list类型。是所有路径下的符合条件的文件名的列表。可以为相对路径，也可以为绝对路径要对某个文件进行处理，需要使用改函数，得到文件名。
Numpy：NumPy系统是Python的一种开源的数值计算扩展。这种工具可用来存储和处理大型矩阵，比Python自身的嵌套列表(nested list structure)结构要高效的多(该结构也可以用来表示矩阵(matrix))。一个用python实现的科学计算包。包括:
一个强大的N维数组对象Array；
比较成熟的(广播)函数库；
用于整合C/C++和Fortran代码的工具包；
实用的线性代数、傅里叶变换和随机数生成函数。numpy和稀疏矩阵运算包scipy配合使用更加方便。
NumPy(Numeric Python)提供了许多高级的数值编程工具，如:矩阵数据类型、矢量处理，以及精密的运算库。专为进行严格的数字处理而产生。多为很多大型金融公司使用，以及核心的科学计算组织如:Lawrence Livermore，NASA用其处理一些本来使用C++，Fortran或Matlab等所做的任务。
OpenCV：是一个基于BSD许可(开源)发行的跨平台计算机视觉库，可以运行在Linux、Windows、Android和Mac OS操作系统上。它轻量级而且高效--由一系列 C 函数和少量 C++ 类构成，同时提供了Python、Ruby、MATLAB等语言的接口，实现了图像处理和计算机视觉方面的很多通用算法。
OpenCV用C++语言编写，它的主要接口也是C++语言，但是依然保留了大量的C语言接口。该库也有大量的Python、Java and MATLAB/OCTAVE(版本2.5)的接口。这些语言的API接口函数可以通过在线文档获得。如今也提供对于C#、Ch、Ruby,GO的支持。
所有新的开发和算法都是用C++接口。一个使用CUDA的GPU接口也于2010年9月开始实现。

cv2.line():划线。Eg:
import cv2
import numpy as np
img = np.zeros((512,512,3), dtype = np.uint8)
建立一张空白的图像
cv2.line(img, (10,10), (510,510), (0, 255,0),5)
# img:图像，起点坐标，终点坐标，颜色，线的宽度
cv2.circle()：画圆
cv2.circle(img, (50,50), 10, (0,0,255),-1)
#img:图像，圆心坐标，圆半径，颜色，线宽度(-1：表示对封闭图像进行内部填满)
cv2.rectangle()：画矩形
cv2.rectangle(img,(70,80),(90,100), (255,0,0),-1)
# img:图像,起点坐标,终点坐标,颜色,线宽度
cv2.ellipse()：画椭圆
cv2.ellipse(img, (150,150),(10,5),0,0,180,(0,127,0),-1)
# img:图像,中心坐标，长短轴长度(长轴长度,短轴长度),旋转角度,显示的部分(0:起始角度,180:终点角度),颜色，线宽度
cv2.polylines()：画多边形
Pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
Pts=Pts.reshape((-1,1,2))
cv2.polylines(img,[Pts],True,(0,255,255),33)
 #img:图像,顶点集，是否闭合，颜色，线宽度
cv2.putText():写入字符
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, ‘HXH’,(50,300),font,4,(255,0,255),2,cv2.LINE_A4)
#img：图像，输入字符串，坐标，字体，字号，颜色，颜色，线宽度，线条种类。
cv2.imshow(‘drawing.png’, img)
cv2.waitKey(0)
4.后续代码思路
提取人脸库中人脸重要部位的描述点，建造一个库存放不同类型五官以及脸型，例如丹凤眼、肿泡眼，厚嘴唇，薄嘴唇，挺鼻梁，塌鼻梁。将描述子转换为数组形式，以便以后画人脸时调用。
建造了五官库之后，手动输入五官脸型特征，先画出68特征点连线进一步补全，经过函数画出人脸。
将人脸与（公安）人脸库进行对比，找出与其最像的一个人。
Or将人脸与各公共场合下的视频录像所能框出的人脸进行对比
表情
 5.完善
如果可以，实现语音输入，不用手动输入人脸特征。（直接外接语音识别系统）
