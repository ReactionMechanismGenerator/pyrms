# Makefile for pyrms
SHELL := /bin/bash
UNAME_S := $(shell uname -s)

install:
	shell install-julia.sh
	
	python install.py
	
	#install julia-python modules and link PyCall
	python3 -m pip install julia
	python -c "import julia; julia.install()"
	
	#install julia packages
	julia install.jl
	
	pip install diffeqpy
	python -c "import diffeqpy; diffeqpy.install()"
	
	#link python in rms_env to python-jl
	ln -sfn $(shell which python-jl) $(shell which python)
	
	#test
	make test
	
test:
	nosetests pyrms/rmsTest.py
