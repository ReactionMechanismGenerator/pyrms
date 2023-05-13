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

# These functions force the returned object to be a jlwrap object, 
# to avoid the solution object gets converted into list of lists
_threadedsensitivities_inds = Main.pyfunctionret(ReactionMechanismSimulator.threadedsensitivities, Main.Any, Main.PyAny, Main.PyAny)
_threadedsensitivities = Main.pyfunctionret(ReactionMechanismSimulator.threadedsensitivities, Main.Any, Main.PyAny)
# Allow us the get the solution object in the julia wrapped object without
# it being converted into list of lists
get = Main.pyfunctionret(Main.get, Main.Any, Main.PyAny, Main.PyAny, Main.PyAny)
def pythreadedsensitivities(react, inds=None,
                            odesolver=Main.nothing, senssolver=Main.nothing,
                            odekwargs={"abstol": 1e-20, "reltol": 1e-6},
                            senskwargs={"abstol": 1e-6, "reltol": 1e-3}):
    if inds is not None:
        # the sol_dict returned here is a jlwrap object and is not easy to access the contents
        sol_dict = _threadedsensitivities_inds(react, inds,
                                               odesolver=odesolver, senssolver=senssolver,
                                               odekwargs=odekwargs, senskwargs=senskwargs)
        # pysol_dict is the python dictionary, but the solution object got turned into list of lists
        pysol_dict = Main.PyObject(sol_dict)
        # this remakes the dictionary with the values as julia wrapped object ODEsolution, 
        # but at the same time allows the user to access it normally like a dictionary
        return {key: get(sol_dict, key, Main.Any) for key in pysol_dict.keys()}
    else:
        sol = _threadedsensitivities(react, 
                                     odesolver=odesolver, senssolver=senssolver,
                                     odekwargs=odekwargs, senskwargs=senskwargs)
        return sol

ReactionMechanismSimulator.threadedsensitivities = pythreadedsensitivities

for item in dir(ReactionMechanismSimulator):
    try:
        locals()[item] = getattr(ReactionMechanismSimulator,item)
    except AttributeError:
        pass
