# 第3.3课内容
滑动窗口目标检测法：
	首先选定一个特定大小的窗口，将这个窗口（从图片左上角开始）输入卷积网络，卷积网络开始进行预测，即判断该窗口内有没有汽车，
	然后将窗口稍向右滑动，并输入给卷积网络，检测这一个窗口内有没有汽车。即每次输入进卷积网络的只是这张大图片的某个小窗口范围内
	的图片。依次重复操作直到这个窗口滑过图像的每一个角落，对每个窗口位置的图片按0和1进行分类（即有或没有目标）。
	为了滑动得更快，可以选用较大的步幅。
	也可以选取更大的窗口进行滑动。
	
滑动窗口目标检测法有很明显的缺点，就是计算成本。因为你在图片中剪切出太多小方块，卷积网络要一个一个地处理。如果选用的步幅很大，
显然会减少输入卷积神经网络的窗口个数，但是粗粒度可能会影响性能。反之，如果采用小粒度或小步幅，传递给卷积网络的小窗口会特别多，
这意味着超高的计算成本。

所以在神经网络兴起之前，人们通常采用更简单的分类器进行对象检测，比如简单的线性分类器。至于误差，因为每个分类器的计算成本都很低，
它只是一个线性函数，所以滑动窗口目标检测算法表现很好。然而，卷积网络运行单个分类任务的成本却高得多，像这样滑动窗口太慢了。除非
采用超细力度或极小步幅，否则无法准确定位图片中的对象。不过，庆幸的是，计算成本问题已经有了很好的解决方案，大大提高了在卷积层上
应用滑动窗口目标检测器的效率。