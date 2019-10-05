# Makefile for pyrms
SHELL := /bin/bash
UNAME_S := $(shell uname -s)

install:
	python install.py
	
	#load added bash_profile and bashrc variables and re source environment
	ifeq ($(UNAME_S),Darwin)
	source ~/.bash_profile    
	else
	source ~/.bashrc
	endif
	
	source activate rms_env
	
	#install PyCall properly and install ReactionMechanismSimulator
	julia install.jl
	
	#install julia-python modules
	python3 -m pip install julia
	python -c "import julia; julia.install()"
	pip install diffeqpy
	python -c "import diffeqpy; diffeqpy.install()"
	
	#link python in rms_env to python-jl
	ln -sfn $(which python-jl) $(dirname $(which python-jl))/python
	
	#test
	make test
	
test:
	nosetests pyrms/rmsTest.py
