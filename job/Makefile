# The make file

# load the various configurations from config file
cnf ?=./job_service_config.env
include $(cnf)
export $(shell sed 's/=.*//' $(cnf))

# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

run_docker_locally:
	docker run -d -p8888:8888 $(SS_SERVICE_NAME)

build_docker: ## Build the customized osrm backend container
	$(info ################# Build docker $(SS_SERVICE_NAME))
	export DOCKER_BUILDKIT=1
	docker build --platform linux/amd64 -t $(SS_SERVICE_NAME) -f Dockerfile .

tag_docker:
	$(info ################# Tag Image $(SS_SERVICE_NAME) $(IMAGE_REGISTRY)/$(SS_SERVICE_NAME))
	docker tag $(SS_SERVICE_NAME) $(IMAGE_REGISTRY)/$(SS_SERVICE_NAME)

push_docker: ## tag and push the containers to the repo $(IMAGE_REGISTRY)
	$(info ################# Push Image to $(IMAGE_REGISTRY)/$(SS_SERVICE_NAME))
	docker push $(IMAGE_REGISTRY)/$(SS_SERVICE_NAME)

upload_yaml: ## upload yaml to stage $(SS_STAGE)
	$(info ################# upload yaml to stage $(SS_STAGE))
	snowsql --config ~/.snowsql/spcs-account-config -q " \
		put file://./*.yaml @$(SS_DB).$(SS_SCHEMA).$(SS_STAGE) auto_compress=false overwrite=true; \
		list @$(SS_DB).$(SS_SCHEMA).$(SS_STAGE); \
		"
######################## COMPOSITE TARGETS ######################

build_and_run_docker_locally: build_docker run_docker_locally

build_and_push_docker: build_docker tag_docker push_docker

tag_and_push_docker: tag_docker push_docker

all: build_and_push_docker upload_yaml