import logging

import pandas as pd

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("CoReM Predictor")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def predict_using_regression(regressor, dataset_to_predict):
    """
    performs all predictions a given dataset
    :param regressor:
    :param dataset_to_predict:
    :return: the labeled dataset
    """
    prediction = pd.DataFrame(data=regressor.predict(dataset_to_predict))
    predicted_dataset = pd.concat([dataset_to_predict, prediction], axis=1, sort=False)

    return predicted_dataset
