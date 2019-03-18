# <img align="top" src="https://github.com/ReactionMechanismGenerator/pyrms/blob/master/logos/rms-logo-small.png"> Py-RMS - Python Reaction Mechanism Simulator

[![Build status](https://img.shields.io/travis/ReactionMechanismGenerator/pyrms/master.svg)](https://travis-ci.org/ReactionMechanismGenerator/pyrms)
[![codecov](https://codecov.io/gh/ReactionMechanismGenerator/pyrms/branch/master/graph/badge.svg)](https://codecov.io/gh/ReactionMechanismGenerator/pyrms)

Python wrapper for the Reaction Mechanism Simulator (RMS) package for simulating and analyzing large chemical reaction mechanisms.  Currently only supports python 2.  

In theory this wraps all functionality within RMS with two caveats:  

1) In jupyter notebooks julia objects don't display the same way in the python kernel as they would in the julia kernel.  For example flux diagram generation had to be hard coded into this wrapper to display properly.  If this happens please make an issue.  

2) There are ways to define julia functions that makes them impossible to call from python using the pyjulia.  In most cases this is easy to fix.  If you find a case where this happens please make an issue.  

## Installation Instructions:  

Note:  
pyrms currently only supports python 2 so running `python` must open a python 2 kernel.  
Installing pyrms links/relinks your julia PyCall module to the python 2 being used.  

Run 
```
git clone https://github.com/ReactionMechanismGenerator/pyrms.git
cd pyrms
make install
```
