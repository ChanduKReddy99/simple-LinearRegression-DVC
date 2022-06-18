from email import header
import os
import argparse
import pandas as pd
from tqdm import tqdm
import logging
from src.utils.common_utils import read_config, clean_prev_dirs_if_exists, create_dirs, save_local_df

logging.basicConfig(
    filename= os.path.join('logs', 'running_logs.log'),
    level=logging.INFO,
    format='[%(asctime)s: %(levelname)s: %(module)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filemode='a'
)

def get_data(config_path: str) -> None:
    """this method Loads the data from the source dir and saves it to local dir as csv file by reading config.yaml.

    Args:
        config_path: path to the config.yaml file
    """
    config = read_config(config_path)

    source_data_path= config['remote_data_source']['path']

    local_data_source= config['local_data_source']
    local_data_dir= local_data_source['data_dir']
    raw_local_data= local_data_source['data_file']

    clean_prev_dirs_if_exists(local_data_dir)

    create_dirs(dirs=[local_data_dir])

    df= pd.read_csv(source_data_path, sep= ',')

    save_local_df(df, raw_local_data, header= True)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load and save data from remote to local directory")
    parser.add_argument("--config", '-c', default= 'configs/config.yaml',help="Path to the config.yaml file")
    parsed_args = parser.parse_args()

    try:
        logging.info('\n********************************')
        logging.info('>>>>>> stage 01 load and save data started..!!')
        get_data(parsed_args.config)
        logging.info('>>>>>> stage 01 load and save data completed..!!<<<<<<\n')
    
    except Exception as e:
        logging.error(e)
        logging.error('\n>>>>>> stage 01 load and save data failed...<<<<<<<\n')


