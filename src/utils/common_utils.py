import os
import shutil
import yaml
import logging




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
    df.to_csv(dir_path, index=False, header=header)
    logging.info(f"Saved dataframe to {dir_path}")

