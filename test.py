from AllModels import AllModels


AllModels().reportData().randomForest(20).report().plot('confusion matrix',True).plot('roc').save('hi.txt')
# AllModels().reportData().knn(2).report().report().plot('confusion matrix').plot('roc')
# AllModels().reportData().linearSVM().report().report().plot('confusion matrix').plot('roc')
# AllModels().reportData().nonLinearSVM().report().report().plot('confusion matrix').plot('roc')