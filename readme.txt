Execution:
- Unzip the folder
- Make sure path to the Python executable is in the system Path environment variable
  or else provide full path to the python executable while running the below commands.
- Navigate to the unzipped folder.

Code is Structured as:
Both the Searches are divided into seperate Classes. There are helpers for reading input file contents and returning lists and also for printing output after the search is done.
There is Node Class that is used for the Individual objects that are used during the execution as basic units.

UnInformed Search:
python.exe find_route.py input.txt Bremen Kassel
Expected Output:
nodes expanded:  9
distance:  297  km
Bremen  to  Hannover ,  132 km
Hannover  to  Kassel ,  165 km

python.exe find_route.py input.txt London Kassel
Expected Output:
nodes expanded:  4
distance: infinity
route:
none

Informed Search:

python.exe find_route.py inf input.txt Bremen Kassel heuristic_values.txt
Expected Output:
nodes expanded:  3
distance:  297  km
Bremen  to  Hannover ,  132 km
Hannover  to  Kassel ,  165 km

python.exe find_route.py inf input.txt London Kassel heuristic_values.txt
Expected Output:
nodes expanded:  4
distance: infinity
route:
none
