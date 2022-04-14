from datetime import datetime
import yaml


def log_time():
    """Returns date time with ms. Can be used for logging messages"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]


def read_yaml_config(filename):
    config = {}
    try:
        with open(filename, "r") as cfg:
            config = yaml.safe_load(cfg)
    except Exception as e:
        raise

    print(f"Configuration read for {filename} complete.")
    return config
