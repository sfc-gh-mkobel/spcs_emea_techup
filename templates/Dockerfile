ARG BASE_IMAGE=continuumio/miniconda3:4.12.0   
FROM $BASE_IMAGE
RUN conda install python=3.8 && \
    conda install gitpython && \
    conda install snowflake-snowpark-python
    
COPY run_job.py ./
ENTRYPOINT ["python3", "run_job.py"]
