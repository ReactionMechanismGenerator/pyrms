# Makefile for pyrms

install:
	python install.py

	conda install --yes yaml
	conda install --yes ipython
	conda install --yes pydot
	conda install --yes setuptools

	#install julia if necessary
	# JL=`which julia`
	# if [[ "$JL" == "" ]]
	# if [[ "$OSTYPE" == "linux-gnu" ]]; then
	#    curl -L https://julialang-s3.julialang.org/bin/linux/x64/1.1/julia-1.1.0-linux-x86_64.tar.gz -o "$HOME/Downloads/julia.tar.gz";
	#    tar xzf "$HOME/Downloads/julia.tar.gz" -C "$HOME/Downloads";
	#    cp -r "$(find "$HOME/Downloads" -maxdepth 2 -name "julia*" -type d | head -n 1)" "$HOME/julia";
	# elif [[ "$OSTYPE" == "darwin"* ]]; then
	#   curl -L https://julialang-s3.julialang.org/bin/mac/x64/1.1/julia-1.1.0-mac64.dmg -o "$HOME/Downloads/julia.dmg";
	#   hdiutil attach ~/Downloads/julia.dmg;
	#   cp -r /Volumes/Julia*/Julia*/Contents/Resources/julia $HOME/julia;
	#   hdiutil detach -force /Volumes/Julia*;
	# else
	#   echo "could not identify OS type attempting linux style install"
	#   curl -L https://julialang-s3.julialang.org/bin/linux/x64/1.1/julia-1.1.0-linux-x86_64.tar.gz -o "$HOME/Downloads/julia.tar.gz";
	#   tar xzf "$HOME/Downloads/julia.tar.gz" -C "$HOME/Downloads";
	#   cp -r "$(find "$HOME/Downloads" -maxdepth 2 -name "julia*" -type d | head -n 1)" "$HOME/julia";
	# fi
	# fi


	#install PyCall properly and install ReactionMechanismSimulator
	julia pyrms/install.jl

	#install julia-python modules
	python2 -m pip install julia
	pip install diffeqpy
	python -c "import diffeqpy; diffeqpy.install()"

	#test
	nosetests pyrms/rmsTest.py

install-travis:


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
