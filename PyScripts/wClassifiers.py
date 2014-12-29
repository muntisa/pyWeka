# print the list of classifiers for normalized/standardized data or not
# (to be copied with COPY PASTE for a file)
 
#######################################################################################################################
## MAIN
#######################################################################################################################

# ===================================================================================
# PARAMETERS
# ===================================================================================

# Skips normalization
ClassifierList=["bayes.AODE","bayes.AODEsr","bayes.BayesianLogisticRegression",\
                "bayes.BayesNet","bayes.ComplementNaiveBayes","bayes.DMNBtext",\
                "bayes.HNB","bayes.NaiveBayes","bayes.NaiveBayesMultinomial",\
                "bayes.NaiveBayesMultinomialUpdateable","bayes.NaiveBayesMultinomialText",\
                "bayes.NaiveBayesSimple","bayes.NaiveBayesUpdateable","bayes.WAODE",\
                "functions.LibLINEAR","functions.LibSVM -C","functions.LinearRegression","functions.Logistic",\
                "functions.MLPClassifier -C","functions.MLPRegressor","functions.MultilayerPerceptron -C -I",\
                "functions.PaceRegression","functions.PLSClassifier","functions.RBFNetwork",\
                "functions.RBFClassifier","functions.RBFRegressor","functions.SimpleLinearRegression",\
                "functions.SimpleLogistic","functions.SGD","functions.SGDText","functions.SMO -N 2",\
                "functions.SMOreg","functions.SPegasos -N","functions.SVMreg","functions.VotedPerceptron",\
                "functions.Winnow","trees.ADTree","trees.BFTree","trees.DecisionStump","trees.ExtraTree",\
                "trees.FT","trees.Id3","trees.J48","trees.J48graft","trees.LADTree","trees.LMT","trees.M5P",\
                "trees.NBTree","trees.RandomForest","trees.RandomTree","trees.REPTree","trees.SimpleCart",\
                "lazy.IB1","lazy.IBk","lazy.KStar","lazy.LBR","lazy.LWL","rules.ConjunctiveRule",\
                "rules.DecisionTable","rules.DTNB","rules.FURIA","rules.JRip","rules.M5Rules","rules.NNge",\
                "rules.OneR","rules.PART","rules.Prism","rules.Ridor","rules.ZeroR","meta.AdaBoostM1",\
                "meta.AdditiveRegression","meta.AttributeSelectedClassifier","meta.Bagging",\
                "meta.ClassificationViaClustering","meta.ClassificationViaRegression",\
                "meta.CostSensitiveClassifier","meta.CVParameterSelection","meta.Dagging","meta.Decorate",\
                "meta.END","meta.EnsembleSelection","meta.FilteredClassifier","meta.Grading","meta.GridSearch",\
                "meta.LogitBoost","meta.MetaCost","meta.MultiBoostAB","meta.MultiClassClassifier",\
                "meta.MultiClassClassifierUpdateable","meta.MultiScheme","meta.OneClassClassifier",\
                "meta.OrdinalClassClassifier","meta.RacedIncrementalLogitBoost","meta.RandomCommittee",\
                "meta.RandomSubSpace","meta.RealAdaBoost","meta.RegressionByDiscretization",\
                "meta.RotationForest","meta.Stacking","meta.StackingC","meta.ThresholdSelector","meta.Vote",\
                "meta.nestedDichotomies.ClassBalancedND","meta.meta.nestedDichotomies.DataNearBalancedND",\
                "meta.nestedDichotomies.ND"]

# Native = with normalizations if exists
##ClassifierList=["bayes.AODE","bayes.AODEsr","bayes.BayesianLogisticRegression",\
##                "bayes.BayesNet","bayes.ComplementNaiveBayes","bayes.DMNBtext",\
##                "bayes.HNB","bayes.NaiveBayes","bayes.NaiveBayesMultinomial",\
##                "bayes.NaiveBayesMultinomialUpdateable","bayes.NaiveBayesMultinomialText",\
##                "bayes.NaiveBayesSimple","bayes.NaiveBayesUpdateable","bayes.WAODE",\
##                "functions.GaussianProcesses","functions.IsotonicRegression","functions.LeastMedSq",\
##                "functions.LibLINEAR","functions.LibSVM","functions.LinearRegression","functions.Logistic",\
##                "functions.MLPClassifier","functions.MLPRegressor","functions.MultilayerPerceptron",\
##                "functions.PaceRegression","functions.PLSClassifier","functions.RBFNetwork",\
##                "functions.RBFClassifier","functions.RBFRegressor","functions.SimpleLinearRegression",\
##                "functions.SimpleLogistic","functions.SGD","functions.SGDText","functions.SMO",\
##                "functions.SMOreg","functions.SPegasos","functions.SVMreg","functions.VotedPerceptron",\
##                "functions.Winnow","trees.ADTree","trees.BFTree","trees.DecisionStump","trees.ExtraTree",\
##                "trees.FT","trees.Id3","trees.J48","trees.J48graft","trees.LADTree","trees.LMT","trees.M5P",\
##                "trees.NBTree","trees.RandomForest","trees.RandomTree","trees.REPTree","trees.SimpleCart",\
##                "lazy.IB1","lazy.IBk","lazy.KStar","lazy.LBR","lazy.LWL","rules.ConjunctiveRule",\
##                "rules.DecisionTable","rules.DTNB","rules.FURIA","rules.JRip","rules.M5Rules","rules.NNge",\
##                "rules.OneR","rules.PART","rules.Prism","rules.Ridor","rules.ZeroR","meta.AdaBoostM1",\
##                "meta.AdditiveRegression","meta.AttributeSelectedClassifier","meta.Bagging",\
##                "meta.ClassificationViaClustering","meta.ClassificationViaRegression",\
##                "meta.CostSensitiveClassifier","meta.CVParameterSelection","meta.Dagging","meta.Decorate",\
##                "meta.END","meta.EnsembleSelection","meta.FilteredClassifier","meta.Grading","meta.GridSearch",\
##                "meta.LogitBoost","meta.MetaCost","meta.MultiBoostAB","meta.MultiClassClassifier",\
##                "meta.MultiClassClassifierUpdateable","meta.MultiScheme","meta.OneClassClassifier",\
##                "meta.OrdinalClassClassifier","meta.RacedIncrementalLogitBoost","meta.RandomCommittee",\
##                "meta.RandomSubSpace","meta.RealAdaBoost","meta.RegressionByDiscretization",\
##                "meta.RotationForest","meta.Stacking","meta.StackingC","meta.ThresholdSelector","meta.Vote",\
##                "meta.nestedDichotomies.ClassBalancedND","meta.meta.nestedDichotomies.DataNearBalancedND",\
##                "meta.nestedDichotomies.ND"]

for item in ClassifierList:
    print item
