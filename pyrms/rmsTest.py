import unittest
import math

from pyrms import rms
from diffeqpy import de

class Testrms(unittest.TestCase):
    def test_simulate(self):
        phaseDict = rms.readinput("pyrms/testing/superminimal.rms")
        spcs = phaseDict["gas"]["Species"]
        rxns = phaseDict["gas"]["Reactions"]
        ig = rms.IdealGas(spcs,rxns,name="gas")
        initialconds = {"T":1000.0,"P":10.0e5,"H2":2.0,"O2":1.0}
        domain,y0 = rms.ConstantTPDomain(phase=ig,initialconds=initialconds)
        react = rms.Reactor(domain,y0,(0.0,10.001))
        sol = de.solve(react.ode,de.CVODE_BDF(),abstol=1e-20,reltol=1e-8)
        sim = rms.Simulation(sol,domain)
        self.assertAlmostEqual(rms.molefractions(sim,"H2",3.0),0.34445669,places=3)
