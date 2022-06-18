import os
import pandas as pd
import argparse
import logging
from sklearn.model_selection import train_test_split
from src.utils.common_utils import read_config, create_dirs, save_local_df,clean_prev_dirs_if_exists


logging.basicConfig(
    filename= os.path.join('logs', 'running_logs.log'),
    level=logging.INFO,
    format='[%(asctime)s: %(levelname)s: %(module)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filemode='a'
)

def split_and_save_data(config_path):
    """this method splits the data and saves into train and eval set.

    Args:
        config_path: path to the config file.
    """
    config = read_config(config_path)

    raw_local_data_dir= config['local_data_source']
    raw_local_data = raw_local_data_dir['data_file']
    
    artifacts= config['artifacts']
    artifacts_dir= artifacts['artifacts_dir']

    split_data= artifacts['split_data']
    processed_data_dir= split_data['processed_data_dir']
    train_data= split_data['train_data_path']
    test_data= split_data['test_data_path']

    clean_prev_dirs_if_exists(artifacts_dir)

    create_dirs(dirs= [artifacts_dir, processed_data_dir])

    base= config['base']
    split_ratio= base['test_size']
    random_seed= base['random_state']

    df= pd.read_csv(raw_local_data, sep=',')

    train, test = train_test_split(df, test_size=split_ratio, random_state=random_seed)

    for data, data_path in (train, train_data), (test, test_data):
        save_local_df(data, data_path)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Split data into train and test sets')
    parser.add_argument('--config', '-c', default='configs/config.yaml', help='Path to config file')
    parsed_args = parser.parse_args()

    try:
        logging.info('\n**********************************')
        logging.info('>>>>>> stage 02 split_data started  <<<<<<')
        split_and_save_data(parsed_args.config)
        logging.info('\n>>>>>> stage 02 split_data finished successfully...<<<<<<\n')

    except Exception as e:
        logging.error(e)
        logging.error('\n>>>>>> stage 02 split_data failed <<<<<<\n')
    