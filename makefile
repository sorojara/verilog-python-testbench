DOCKER_IMAGE = sorojara/verilog-cocotb
VERSION=v1.0.0

all:
	docker pull $(DOCKER_IMAGE):$(VERSION)
	docker run -v `pwd`:/src -it $(DOCKER_IMAGE):$(VERSION) bash