import os
import sys
from IPython.display import Image
import IPython.display

from julia import Main
from julia import ReactionMechanismSimulator

from julia.ReactionMechanismSimulator import makefluxdiagrams

def pygetfluxdiagram(bsol,t,centralspecieslist=[],superimpose=False,
    maximumnodecount=50, maximumedgecount=50, concentrationtol=1e-6, speciesratetolerance=1e-6,
    maximumnodepenwidth=10.0,maximumedgepenwidth=10.0,radius=1,centralreactioncount=-1,outputdirectory="fluxdiagrams",
    colorscheme="viridis"):

    fd = makefluxdiagrams(bsol,[t], centralspecieslist=centralspecieslist,superimpose=superimpose,
        maximumnodecount=maximumnodecount, maximumedgecount=maximumedgecount, concentrationtol=concentrationtol,
        speciesratetolerance=speciesratetolerance,maximumnodepenwidth=maximumnodepenwidth,
        maximumedgepenwidth=maximumedgepenwidth,radius=radius,centralreactioncount=centralreactioncount,
        outputdirectory=outputdirectory,colorscheme=colorscheme)

    IPython.display.display(IPython.display.Image(os.path.join(fd.outputdirectory,"flux_diagram_1.png")))

ReactionMechanismSimulator.getfluxdiagram = pygetfluxdiagram

for item in dir(ReactionMechanismSimulator):
    try:
        locals()[item] = getattr(ReactionMechanismSimulator,item)
    except AttributeError:
        pass
