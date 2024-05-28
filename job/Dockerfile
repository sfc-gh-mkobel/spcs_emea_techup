ARG BASE_IMAGE=continuumio/miniconda3:4.12.0   
FROM $BASE_IMAGE
RUN conda install python=3.8 && \
    conda install snowflake-snowpark-python
    
COPY main.py ./
#serves as the starting point for a Docker container’s runtime
#When you create a Docker image and instantiate it as a container, the ENTRYPOINT command executes by default.
ENTRYPOINT ["python3", "main.py"]
