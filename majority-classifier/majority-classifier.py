import numpy as np

def majority_classifier(y_train, X_test):
    y_train, X_test = np.array(y_train), np.array(X_test)

    classes, counts = np.unique(y_train, return_counts=True)

    majority_classees = classes[np.argmax(counts)]

    predictions = np.full(X_test.shape[0], majority_classees)
    return predictions