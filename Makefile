# Makefile for pyrms

install:
	python install.py
  
	#load added bash_profile and bashrc variables and re source environment
	if [ "$(uname)" == "Darwin" ]; then
    source ~/.bash_profile    
	elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
	  source ~/.bashrc
	fi

	source activate rms_env
	
	#install PyCall properly and install ReactionMechanismSimulator
	julia install.jl

	#install julia-python modules
	python3 -m pip install julia
	python -c "import julia; julia.install()"
	pip install diffeqpy
	python -c "import diffeqpy; diffeqpy.install()"
  
	#test
	make test

test:
	nosetests pyrms/rmsTest.py
