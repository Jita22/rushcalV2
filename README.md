DirHelp.ipynb : Read this to understand the organization of the files and folders in the current directory.

Programmatic flow:
************************************************
1. Remember to make empty folders 'fresults' in the working directory, if not already present.
2. Open instance of legend-base in the terminal by typing "cenv legend-base"
3. Run "python3 readroot-v2-loop.py"
4. Run the interactive notebook "compare_expsim.ipynb"
************************************************

About readroot-v2-loop.py
This calls readroot-v2.py

Inputs:
iplist.txt -> this contains the paths to the MaGe rootfiles
MaGe o/p rootfiles

Output: 2-D Hits matrix (in the ROI) for the detectors saved in fresults. Columns = string number (1 to 12) and Rows = detector unit (1 to 8)

Step 1: Read the MaGe output file using uproot. 
Step 2: Store the fSteps.fEdep and fSteps.fPhysVolName into numpy arrays (easier to iterate than dataframes)
Step 3: Manually change the centroid energy (centE) and half-window (deltaE).
Step 4: Initialize the energy table (etab) and hits arrays. Note that the etab is a 3-D array while hits is a 2-D array.
Step 5: Loop over the events, and invoke the indext (index extractor) to get the element in the 3-D matrix which needs to be updated. No if statements are needed in this process and it is much faster (reduced time from few hours to a few minutes). I'm very happy and proud of this logic block :D
Step 6: 

For loops are much faster than while loops in python. Thus, wherever needed, while loops have been eliminated and for loops have been implemented.
************************************************


About compare_expsim.ipynb

Inputs:
The relevant matrices with simulated counts (o/p of readroot-v2.py stored in fresults)

Outputs:
Simulated counts adjusted as per the source activities,
List of factors (Simulation/Experiment)

Step 1: Calculate the activities of the sources, taking into account exponential decay, as on the day of the run.
Step 2: Calculate the strength factor sf which will give us the factor by which the simulated counts need to be multiplied in order to take into account the run time, source strength.
Step 3: Load the simulated counts for various positions, combine and multiply by sf in order to get the array of counts from simulations.
Step 4: Manually input the array of experimental counts.
Step 5: Generate a list of factor = simulation / experiment.
************************************************

TO BE UPDATED
