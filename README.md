# MLIPs-with-iPI
Here are a few examples of running basic simulations with i-PI v3.0. You are welcome to read the [paper on the v3.0 release here](https://doi.org/10.1063/5.0215869) for more details on the features. Long story short, we have made i-PI faster so that its Python overhead is not a bottleneck. Check out the following directories on the various types of simulations!

| Directory            | Description                                                                                                 | Useful For                                                                                  |
|----------------------|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| `00-NVE`               | Constant energy ensemble.                                                                                   | Estimating classical dynamical properties.                                                  |
| `01-NVT-for-dynamics`  | Constant temperature ensemble with a weak global thermostat.                                                | Recommended for calculating dynamical properties due to better ergodicity compared to NVE.  |
| `02-NVT-Langevin`      | Constant temperature simulation with a Langevin thermostat.                                                 | Simulating solids or model systems.                                                         |
| `03-NVT-SVR`           | Constant temperature simulation with a stochastic velocity rescaling thermostat.                            | Simulating liquids.                                                                         |
| `04-NVT-GLE`           | Constant temperature simulation with a generalized Langevin equation thermostat.                            | Simulating molecular gases with disparate modes or biphasic interfaces where other thermostats are inefficient. |
| `05-NPT-isotropic-BZP` | Constant temperature and pressure simulation with isotropic cell fluctuations using the Bussi-Zykova-Parrinello scheme. | Simulating fluids as they are isotropic in their response to pressure.                                  |
| `06-flexible-MTTK`     | Constant temperature and pressure simulation with flexible cell fluctuations using the Martyna-Tuckerman-Tobias-Klein scheme. | Simulating solids as they can be anisotropic in their response to pressure.                                |
| `07-REMD-NVT`          | Replica exchange simulation at constant temperature.                                                        | Obtaining statistics for many temperatures, improving sampling efficiency.                  |
| `08-REMD-NPT`          | Replica exchange simulation at constant temperature and pressure.                                           | Efficiently simulating an isobar.                                                           |
| `09-REPIMD-NVT-for-dynamics`          | Constant temperature quantum ensemble with weak thermostatting on the centroid and efficient thermostatting on non-centroid mode.                                           | Recommended for calculating quantum dynamical properties approximately within the thermostatted ring polymer molecular dynamics.                                                           |


## How to run

Running simulations with i-PI is a two-step process. You will first need to run i-PI and then the force provider. 
```bash
i-pi input.xml &> log.i-pi &
sleep 30
python run-ase.py
```
For most simulations, you can reduce the sleep time to 10 seconds. However, a REMD simulation can require a longer time to set up. In these examples, ASE is the force provider, and I am using the [MACE-MP-0](https://github.com/ACEsuit/mace-mp) potential. However, you can use any potential by replacing the calculator in the run-ase.py file. 

```python
atoms.calc = mace_mp() # Replace this with your preferred calculator 
```

Check out [i-PI's README]() on installation instructions. If you want to install the last version
```bash
pip install git+https://github.com/i-pi/i-pi.git
```

If you have git cloned the i-PI source directory, please ensure you source the `env.sh` file in the i-PI directory
```bash
source ${IPI_ROOT_DIRECTORY}/env.sh
```
to have access to executables.

and you have `ase` and `mace` available in your Python environment. If you don't have that, an easy way is to
```bash
pip install mace-torch
```

### Contact

If you encounter any problems, you are welcome to contact me at [v.kapil@ucl.ac.uk](v.kapil@ucl.ac.uk) or raise an issue on GitHub. I strongly encourage you to go through the [troubleshooting section of i-PI's online documentation](https://ipi-code.org/i-pi/troubleshooting.html) beforehand, as it should address the majority of your problems. Feel free to suggest examples or use cases that are not covered here. 



