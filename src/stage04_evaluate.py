import os
import argparse
import pandas as pd
import logging
import joblib
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from src.utils.common_utils import read_config, save_reports



logging.basicConfig(
    filename= os.path.join('logs', 'running_logs.log'),
    level=logging.INFO,
    format='[%(asctime)s: %(levelname)s: %(module)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filemode ='a'
)

def eval_metrics(actual, pred):
    """This method calculates the evaluation metrics.
    """
    rmse= mean_squared_error(actual, pred)**0.5
    r2= r2_score(actual, pred)
    mae= mean_absolute_error(actual, pred)
    return rmse, r2, mae

def evaluate(config_path:str) -> None:
    """This method evaluates the model on the test data.

    Args:
        config_path: path to the config file
    """
    config= read_config(config_path)

    artifacts= config['artifacts']
    split_data= artifacts['split_data']

    test_data_path= split_data['test_data_path']
    model_path= artifacts['model_path']
    target= config['base']['target_col']
    scores_file= artifacts['reports']['scores']

    test= pd.read_csv(test_data_path, sep= ',')

    x_test= test.drop(target, axis=1)
    y_test= test[target]

    lr= joblib.load(model_path)
    logging.info(f'Model loaded from {model_path}')

    predicted_values= lr.predict(x_test)

    rmse, r2, mae= eval_metrics(y_test, predicted_values)

    scores= {
        'rmse': rmse,
        'r2': r2,
        'mae': mae
    }

    save_reports(scores_file, scores)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Evaluate the model')
    parser.add_argument('--config', default='configs/config.yaml',help='Path to the config file')
    parsed_args = parser.parse_args()

    try:
        logging.info('\n**************************')
        logging.info('>>>>>>>> stage 04 Evaluating the model started   <<<<<<<')
        evaluate(parsed_args.config)
        logging.info('>>>>>>>> stage 04 Evaluating the model completed <<<<<<<')

    except Exception as e:
        logging.error(e)
        logging.error('>>>>>>>> stage 04 Evaluating the model failed <<<<<<<')