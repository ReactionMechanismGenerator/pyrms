import sys
from IPython.display import Image
import IPython.display
from . import load_julia_packages
rms, _, = load_julia_packages("ReactionMechanismSimulator", "PythonCall")
from juliacall import Main

sys.modules[__name__] = rms

