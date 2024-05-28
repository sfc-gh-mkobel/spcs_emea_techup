#!/opt/conda/bin/python3

import argparse
import logging
import os
import sys
import git

from snowflake.snowpark import Session
from snowflake.snowpark.exceptions import *


def get_arg_parser():
    """
    Input argument list.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--git_repo_url", required=True, help="get repo url")
    parser.add_argument("--repo_name",required=True,help="name of the repo")
    parser.add_argument("--main_file_name", required=True, help="main file name")
    parser.add_argument("--volume_mounts_path", required=True, help="volume mounts path")

    return parser


def get_logger():
    """
    Get a logger for local logging.
    """
    logger = logging.getLogger("job-tutorial")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def run_job():
    """
    Main body of this job.
    """
    logger = get_logger()
    logger.info("Job started")
    
     # Parse input arguments
    args = get_arg_parser().parse_args()
    git_repo_url = args.git_repo_url
    repo_name= args.repo_name
    main_file_name = args.main_file_name
    volume_mounts_path = args.volume_mounts_path
    
    logger.info(f"Args:  git_repo_url:{git_repo_url}, repo_name:{repo_name}, main_file_name:{main_file_name}, volume_mounts_path:{volume_mounts_path}")
    
    git.Git(volume_mounts_path).clone(git_repo_url)
    from importlib.machinery import SourceFileLoader
    
    main_file_path = f"{volume_mounts_path}/{repo_name}/{main_file_name}" 
    logger.info(f"Going to run file: {main_file_path}")
   
    main = SourceFileLoader("run_job",main_file_path).load_module()
    main.run_job()
    
    logger.info("Job finished")


if __name__ == "__main__":
    run_job()

