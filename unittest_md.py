import sys, unittest
from md import calcenergy

from ase import units
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from asap3 import Trajectory

use_asap = True

if use_asap:
    from asap3 import EMT

    size = 10
else:
    from ase.calculators.emt import EMT

    size = 3

class MdTests(unittest.TestCase):
    def test_calcenergy(self):
        atoms = FaceCenteredCubic(
        directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        symbol='Cu',
        size=(size, size, size),
        pbc=True)
        atoms.calc = EMT()

        etot_test = atoms.get_total_energy()/len(atoms)

        epot, ekin, temp, etot = calcenergy(atoms)
        if etot_test == etot:    
            self.assertTrue(True)
        else: 
            self.assertTrue(False)

if __name__ == "__main__":
    tests = [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())
