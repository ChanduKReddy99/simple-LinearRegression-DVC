import pandas as pd
import os
import argparse
import logging
from sklearn.linear_model import LinearRegression
from src.utils.common_utils import read_config, create_dirs, save_reports
import joblib




logging.basicConfig(
    filename= os.path.join('logs', 'running_logs.log'),
    level=logging.INFO,
    format='[%(asctime)s: %(levelname)s: %(module)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filemode='a'
)

def train_model(config_path: str, params_path:str) -> None:
    """This model trains the Linear Regression model on training data.

    Args:
        config_path: path to the config file
        params_path: path to the params file
    """
    config= read_config(config_path)
    params= read_config(params_path)

    artifacts= config['artifacts']

    split_data= artifacts['split_data']
    train_data_path= split_data['train_data_path']

    base= config['base']
    random_seed= base['random_state']
    target= base['target_col']

    reports = artifacts['reports']
    reports_dir= reports['reports_dir']
    params_file= reports['parameters']

    Linear_Regression_params= params['estimators']['LinearRegression']['lr_params']
    intercept= Linear_Regression_params['intercept']
    coefficients= Linear_Regression_params['coefficients']

    train= pd.read_csv(train_data_path, sep= ',')

    x_train = train.drop(target, axis=1)
    y_train=  train[target]

    lr= LinearRegression()
    lr.fit(x_train, y_train)

    model_dir= artifacts['model_dir']
    model_path= artifacts['model_path']

    create_dirs([model_dir, reports_dir])

    params= {
        'intercept': intercept,
        'coefficients': coefficients
    }

    save_reports(params_file, params)

    joblib.dump(lr, model_path)

    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Train the Linear Regression model')
    parser.add_argument('--config', '-c', default='configs/config.yaml', help='Path to config file')
    parser.add_argument('--params', '-p', default='params.yaml', help='Path to params file')
    parsed_args = parser.parse_args()

    try:
        logging.info('\n**********************************')
        logging.info('>>>>>> stage 03 training model started  <<<<<<')
        train_model(parsed_args.config, parsed_args.params)
        logging.info('>>>>>> stage 03 training model finished successfully..!! <<<<<<\n')

    except Exception as e:
        logging.error(e)
        logging.info('\n>>>>>> stage 03 training model failed <<<<<<\n')