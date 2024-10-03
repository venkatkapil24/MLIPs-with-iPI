from ase.io import read
from mace.calculators import mace_mp 
from ase.calculators.socketio import SocketClient

# Define atoms object
print ("Reading atoms object.")
atoms = read("init.xyz", 0)
atoms.calc = mace_mp()

host = "driver"
print ("Setting up socket.")
client = SocketClient(unixsocket=host)
print ("Running socket.")
client.run(atoms, use_stress=True)
print ("setting up calculator")
