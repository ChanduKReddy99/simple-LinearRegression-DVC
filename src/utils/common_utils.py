import os
import shutil
import yaml
import logging
import json




def read_config(file_path:str) -> dict:
    """reads the config file and returns the config dictionary

    Args:
        config_: path to the config.yaml file
    
    Returns:
        config_dict: dictionary containing the content of the config.yaml file
    """
    with open(file_path) as yaml_file:
        logging.info(f"Reading config file from {file_path} successfully..!!!")
        content = yaml.safe_load(yaml_file)
        return content

def clean_prev_dirs_if_exists(dir_path:str) -> None:
    """cleans the previous directories if they exist
    """
    if os.path.isdir(dir_path):
        shutil.rmtree(dir_path)
        logging.info(f"Clean previous directories if they exist in {dir_path}")
        
def create_dirs(dirs:list) -> None:
    """creates the directories if they do not exist
    """
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        logging.info(f"Created directory {dir_path}")

def save_local_df(df, dir_path, header=False) -> None:
    """saves the dataframe to the local directory
    """
    if header:
        new_columns= [col.replace(' ', '_') for col in df.columns]
        df.to_csv(dir_path, index=False, header=new_columns)
        logging.info(f'dataframe saved at {dir_path} with new headers')

    else:
        df.to_csv(dir_path, index=False)
        logging.info(f'dataframe saved at {dir_path}')


def save_reports(file_path:str, report:dict):
    """ this method saves the reports of the model in the reports directory
    """
    with open(file_path, 'w') as f:
        json.dump(report, f, indent=4)


