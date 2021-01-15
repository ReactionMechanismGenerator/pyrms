# <img align="top" src="https://github.com/ReactionMechanismGenerator/pyrms/blob/master/logos/rms-logo-small.png"> Py-RMS - Python Reaction Mechanism Simulator

[![Build status](https://img.shields.io/travis/ReactionMechanismGenerator/pyrms/master.svg)](https://travis-ci.org/ReactionMechanismGenerator/pyrms)
[![codecov](https://codecov.io/gh/ReactionMechanismGenerator/pyrms/branch/master/graph/badge.svg)](https://codecov.io/gh/ReactionMechanismGenerator/pyrms)

Python wrapper for the Reaction Mechanism Simulator (RMS) package for simulating and analyzing large chemical reaction mechanisms.  Currently only supports python 2.  

In theory this wraps all functionality within RMS with two caveats:  

1) In jupyter notebooks julia objects don't display the same way in the python kernel as they would in the julia kernel.  For example flux diagram generation had to be hard coded into this wrapper to display properly.  If this happens please make an issue.  

2) There are ways to define julia functions that makes them impossible to call from python using the pyjulia.  In most cases this is easy to fix.  If you find a case where this happens please make an issue.  

## Installation Instructions from Anaconda:  

Note: We recommend installing pyrms in its own conda environment when convenient because getting pyjulia to work with conda python efficiently currently requires relinking 
      the python executable to the python-jl executable, this usually isn't problematic, but it can be an issue in more complicated conda environments. 

To Install Binaries with Conda Run:  
```
conda install -c rmg pyrms
python -c "import pyrms; pyrms.install()"
ln -sfn $(which python-jl) $(which python)
```
