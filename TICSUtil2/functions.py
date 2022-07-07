from datetime import datetime
import yaml, os


def log_time():
    """Returns date time with ms. Can be used for logging messages"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]


def read_yaml_config(filepath):
    filename = filepath.split(".")[0]
    fileext = filepath.split(".")[1]
    filepath_dev = filename + "_dev" + "." + fileext
    if os.path.isfile(filepath_dev):
        filepath = filepath_dev
        print(f"Dev config file exists. Using Dev config.")
    config = {}
    try:
        with open(filepath, "r") as cfg:
            config = yaml.safe_load(cfg)
    except Exception as e:
        raise
    print(f"Configuration read for {filepath} complete.")
    return config
