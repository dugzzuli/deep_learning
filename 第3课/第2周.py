【1】误差分析
	总结一下，进行误差分析，你应该找一组错误里子，可能在你的开发集里、或者测试集里，观察所无标记的例子，看看假阳性和假阴性，
	统计属于不同错误类型的错误数量。在这个过程中，你可能会得到启发，归纳出新的误差类型，就像我们看到的那样，如果你过了一遍
	错误例子，然后说，天，有这么多Instagram（一款图像分享应用）滤镜，或Snapchat(照片分享平台)，这些滤镜干扰了我的分类器，
	你就可以在途中新建一个错误类型。总之，通过统计不同标记类型占总数的百分比，可以帮你发现哪些问题需要优先解决，或者给你构
	思新优化方向的灵感。
	
	例如，识别猫的算法中，误差率为10%。如果在100个错误标记的开发集例子中，有5个是狗。这意味着在典型的100个出错的例子中，即
	使你完全解决了狗的问题，你也只能修正这100个错误中的5个。或者换句话说，如果你只有5%的错误是狗图片，那么你在狗的问题上花
	了很多时间，那么你最多只能希望你的误差从10%下降到9.5% (10%-10%*5%=9.5%)。误差下降了5%，那就是10%下降到9.5%。
	

	事实证明，深度学习算法对于【训练集】中的随机误差是相当鲁棒的。只要你的标记出错的例子，只要这些错误例子离随机误差不太远，有
	时可能做标记的人没有注意，或者不小心按错键了。如果误差足够随机，那么放着这些误差不管可能也没问题，而不要花费太多时间修
	复它们。当然你浏览以下训练集，检查一下这些标签，并修正它们也没什么害处。只要总数据集足够大，实际误差可能不会太高。
	
	但是深度学习对系统性的错误就没那么鲁棒了。比如说，如果做标记的人一直把白色的狗标记成猫，那就成问题了。因为你的分类器学
	习之后，会把所有白色的狗都分类为猫，但是随机误差或近似随机误差对于大多数深度学习算法来说，不成问题。
	
	上面是针对【训练集】中标记出错来说明的。那么如果是【开发集和测试集】中有这些标记出错的例子呢？
	如果你担心开发集和测试集中标记出错的例子带来的影响，一般建议你在误差分析时，添加一个额外的列，这样你也可以统计标签Y错误的
	例子数。比如说，你可能统计对100个标记出错的例子的影响，所以你会找到100个例子，其中你的分类器的输出和开发集的标签不一致，
	有时对于其中的少数例子，你的分类器输出和标签不同，是因为标签错了，而不是你的分类器出错。在这个例子中，你发现标记的人漏了
	背景里的一只猫，所以那里打个勾，来表示例子98标签出错了，也许这张图实际上是猫的样子，而不是一只真正的猫，也许你希望标记Y
	=0，而不是Y=1，然后再在那里打个勾。当你统计出其他错误类型的百分比后，就像我们在之前的视频中看到的那样，你还可以统计因为
	标签错误所占的百分比，你的开发集里的Y值是错误的，这就解释了，为什么你的学习算法做出和数据集里的标记不一样的预测。
	
	所以现在问题是，是否值得修正这6%标记出错的例子。我的建议是，如果这些标记错误，严重影响了你在开发集上评估算法的能力，那么
	就应该花时间修正错误的标签。但是如果它们没有严重影响到你用开发集评估成本偏差的能力，那么就不应该花宝贵的时间去处理。
	我建议你看三个数字来确定是否值得去人工修正标记出错的数据：
	整体的开发集误差:之前的视频中，我们说也许我们的系统达到了90%的整体准确度，所以有10%误差。那么你应该看看错误标记引起的
	错误的数量或者百分比。所以在这种情况下，6%的错误来自标记出错，所以10%的6%就是0.6%，也许你应该看看其他原因导致的错误。如
	果你的开发集上有10%的错误，其中0.6%是因为标记出错，剩下的占9.4%是其他原因导致的，比如把狗误认为猫。所以在这种情况下，我
	说有9.4%误差需要集中精力修正，而标记出错导致的错误是总体错误的一小部分而已。所以如果你一定要这么做，你也可以手工修正各种
	错误标签，但也许这并不是当下最重要的任务。
	
	我们再看另一个例子，假设你在学习问题上取得了很大进展，所以误差不再是10%了，假设你把误差降到了2%，但总体错误中的0.6%还是标
	记出错导致的。所以现在，如果你想检查一组标记出错的开发集图片，开发集数据有2%标记错误了，那么其中很大部分0.6%/(2%)，实际上
	变成30%标签而不是6%标签了，有那么多错误例子其实是因为标记出错导致的，所以现在其他原因导致的错误是1.4%，当测得的那么大一部
	分的错误都是开发集标记出错导致的，那似乎修正开发集里的错误标签似乎更有价值。如果你还记得设立开发集的目标的话，开发集的主要
	目的是，你希望用它来从两个分类器A和B中选择一个。所以当你测试两个分类器A和B时，在开发集上有一个2.1%误差，另一个有1.9%误差，
	但是你不能在信任开发集了，因为它无法告诉你，这个分类器是否比这个好，因为0.6%的误差是标记出错导致的。那么现在你就有很好的
	理由去修正开发集里的错误标签。因为在右边这个例子中，标记出错对算法错误的整体评估标准有严重的影响，而左边的例子中，标记出
	错对你算法影响的百分比还是相对较小的。
	
	现在如果你决定要去修正开发集数据，手动检查标签，并尝试修正一些标签，这里还有一些额外的方针和原则需要考虑。
	(1)首先我鼓励你，不管用什么修正手段，都要同时作用到开发集和测试集上。
	我们之前讲过为什么开发集和测试集要来自同样的分布，开发及确定了你的目标，当你集中目标后，你希望算法能够推广到测试集上，这样
	你的团队能够更高效的在来自同一分布的开发集和测试集上迭代。如果你打算修正开发集上的部分数据，那么最好也对测试集做同样的修正
	，以确保他们来自相同的分布。所以我们雇佣了一个人来仔细检查这些标签，但必须同时检查开发集和测试集。
	
	(2)其次，我强烈建议你要考虑，同时检验算法判断正确和判断错误的例子。
	要检查算法出错的例子很容易，只需要看看哪些例子是否需要修正，但还有可能有些例子算法没判断对，那些也需要修正。
	如果你只修正算法出错的例子，你对算法的偏差估计可能会变大，这会让你的算法有一点不公平的优势，我们就需要再次检查出错的例子，
	但也需要再次检查做对的例子，因为算法有可能因为运气好，把某个东西判断对了。在那个特例里，修正那些标签可能会让算法从判断对
	变成判断错。 
	这第二点不是很容易做，所以通常不会这么做。通常不会这么做的原因是，如果你的分类器很准确，那么判断错的次数比判断正确的次数
	要少得多。所以如果你的分类器有98%的准确度，那么就有2%出错，98%都是对的。所以更容易检查2%数据上的标签。然而检查98%数据上的
	标签需要花的时间长得多，所以通常不这么做，但也是要考虑到的。
	
	(3)最后，如果你进入到一个开发集和测试集去修正这里的部分标签,你可能会，也可能不会对训练集做同样的事情。在之前的视频中讲过，
	修正训练集中的标签其实相对没那么重要。你可能决定只修正开发集和测试集中的标签，因为他们通常比训练集小得多，你可能不想把所
	有额外的精力投入到修正大得多的训练集中的标签。
	开发集和测试集来自同样的分布非常重要，而如果训练集来自稍微不同的分布，通常这是意见很合理的事情。
	
	吴恩达的建议：
	在构造实际系统时，通常需要更多的人工误差分析，更多的人类见解来架构这些系统，尽管深度学习的研究人员不愿意承认这点。
	第二，不知道为什么，我看一些工程师和研究人员不愿意亲自去看这些例子，坐下来看100或者几百个例子来统计错误数量，也许做这些事
	很无聊，但我经常亲自这么做。当我带领一个机器学习团队时，我想知道它犯的错误，我会亲自去看这些数据，尝试和一部分错误作斗争。
	我想，就因为花了这几分钟或者几个小时去亲自统计数据，真的可以帮你找到需要优先处理的任务，我发现花时间亲自检查数据非常值得，
	所以我强烈建议你们考虑这么去做。
	
	
	
	
	