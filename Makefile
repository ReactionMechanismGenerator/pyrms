# Makefile for pyrms

install:
	python install.py

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
