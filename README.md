# AUTO-metal-hardness
 Automatic generation of metal hardness (anchors and clips)

本代码适合那些做建筑工程材料检测的人员使用
能够自动生成符合实际的数据。

本人实测了工程材料中的锚具和夹片的硬度，一共测了300多个样品。
将这些结果进行了基本的统计分析，发现基本符合正态分布
然后我就再也没做过硬度试验了，hhhhhhhhhh

本代码由Python编写，直接用Python运行即可
所有的平均值，方差都是我实测再统计得到的，
运行的时候只用输入HRA79_85，HRC22_34和HRC59_64 其中的一个，再输入组数即可。
每组有3个试样

工程检测太假了，我只是假得严谨一点。
20201123
对程序进行了封装，现在只需要运行 run_gossdis.py即可
