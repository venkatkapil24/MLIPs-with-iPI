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

