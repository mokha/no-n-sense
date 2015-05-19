import timeit
from pattern.vector import MAJORITY, MULTINOMIAL, COSINE, CLASSIFICATION, POLYNOMIAL
from pattern.vector import NB, KNN, SLP, SVM, kfoldcv

def test(data, type):
    print '----------------------------------------------------'
    print 'TEST FUNCTION STARTED FOR ' + type + '!'
    total_data_size = len(data)
    training_size = int(round(total_data_size/2))
    test_size = training_size
    print 'Total Size: ' + str(total_data_size)
    print 'Training Size: ' + str(training_size)
    print 'Test Size: ' + str(test_size)

    print 'Training Started for ' + type + '!'
    classification_methods = {
      #uncomment based on what classification algorithm you would like to test
      'NB' :  NB(train=data[:training_size], baseline=MAJORITY, method=MULTINOMIAL),
      'KNN2' : KNN(train=data[:training_size], baseline=MAJORITY, k=2, distance=COSINE),
      'KNN3' : KNN(train=data[:training_size], baseline=MAJORITY, k=3, distance=COSINE),
      'KNN4' : KNN(train=data[:training_size], baseline=MAJORITY, k=4, distance=COSINE),
      'KNN5' : KNN(train=data[:training_size], baseline=MAJORITY, k=5, distance=COSINE),
      'KNN6' : KNN(train=data[:training_size], baseline=MAJORITY, k=6, distance=COSINE),
      'KNN7' : KNN(train=data[:training_size], baseline=MAJORITY, k=7, distance=COSINE),
      'KNN8' : KNN(train=data[:training_size], baseline=MAJORITY, k=8, distance=COSINE),
      'KNN9' : KNN(train=data[:training_size], baseline=MAJORITY, k=9, distance=COSINE),
      'KNN10' : KNN(train=data[:training_size], baseline=MAJORITY, k=10, distance=COSINE),
      'SLP1' : SLP(train=data[:training_size], baseline=MAJORITY, iterations=1),
      'SLP2' : SLP(train=data[:training_size], baseline=MAJORITY, iterations=2),
      'SLP3' : SLP(train=data[:training_size], baseline=MAJORITY, iterations=3),
      'SVM' : SVM(train=data[:training_size], type=CLASSIFICATION, kernel=POLYNOMIAL),
    }

    print 'Normal Testing Started!'
    # uncomment to start the normal test
    for classification in classification_methods.keys():
      #measure the time it takes to classify!
      start = timeit.default_timer()
      #normal test
      accuracy, precision, recall, f1 = classification_methods[classification].test(data[training_size:training_size+test_size])
      stop = timeit.default_timer()
      print '*' + classification + '*'
      print 'Accuracy: ' + str(accuracy)
      print 'Precision: ' + str(precision)
      print 'Recall: ' + str(recall)
      print 'F1-score: ' + str(f1)
      print 'Time: ' + str(stop - start)
      print


    # #uncomment to test using cross-validation
    # start = timeit.default_timer()
    # accuracy, precision, recall, f1, stdev = kfoldcv(NB, data, folds=10, method=MULTINOMIAL)
    # stop = timeit.default_timer()
    # print '*NB*'
    # print 'Accuracy: ' + str(accuracy)
    # print 'Precision: ' + str(precision)
    # print 'Recall: ' + str(recall)
    # print 'F1-score: ' + str(f1)
    # print 'STDev: ' + str(stdev)
    # print 'Time: ' + str(stop - start)
    # print
    #
    # start = timeit.default_timer()
    # accuracy, precision, recall, f1, stdev = kfoldcv(SLP, data, folds=10, iterations=1)
    # stop = timeit.default_timer()
    # print '*SLP1*'
    # print 'Accuracy: ' + str(accuracy)
    # print 'Precision: ' + str(precision)
    # print 'Recall: ' + str(recall)
    # print 'F1-score: ' + str(f1)
    # print 'STDev: ' + str(stdev)
    # print 'Time: ' + str(stop - start)
    # print
    #
    # start = timeit.default_timer()
    # accuracy, precision, recall, f1, stdev = kfoldcv(SLP, data, folds=10, iterations=2)
    # stop = timeit.default_timer()
    # print '*SLP2*'
    # print 'Accuracy: ' + str(accuracy)
    # print 'Precision: ' + str(precision)
    # print 'Recall: ' + str(recall)
    # print 'F1-score: ' + str(f1)
    # print 'STDev: ' + str(stdev)
    # print 'Time: ' + str(stop - start)
    # print
    #
    # start = timeit.default_timer()
    # accuracy, precision, recall, f1, stdev = kfoldcv(SLP, data, folds=10, iterations=3)
    # stop = timeit.default_timer()
    # print '*SLP3*'
    # print 'Accuracy: ' + str(accuracy)
    # print 'Precision: ' + str(precision)
    # print 'Recall: ' + str(recall)
    # print 'F1-score: ' + str(f1)
    # print 'STDev: ' + str(stdev)
    # print 'Time: ' + str(stop - start)
    # print

    print '----------------------------------------------------'