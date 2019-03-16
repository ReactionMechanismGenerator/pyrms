# Makefile for pyrms

install:
	python install.py

	conda install --yes yaml
	conda install --yes ipython
	conda install --yes pydot
	conda install --yes setuptools

	#install PyCall properly and install ReactionMechanismSimulator
	julia pyrms/install.jl

	#install julia-python modules
	python2 -m pip install julia
	pip install diffeqpy
	python -c "import diffeqpy; diffeqpy.install()"

	#test
	cd pyrms
	nosetests rmsTest.py
	cd ..
