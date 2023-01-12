# N-interconnected-mass-spring-system
A PyGame simulation of the motion over time for an interconnected mass-spring-system with n masses. The masses are oscillating on a horizontal and frictionless surface.

The user can input some initial conditions on the position of each mass. For each new initial condition, a new mass is added into the system. 
It's assumed that all masses are identical, and that they all start from rest. Through some mathematical derivation, the equations of motions are derived for each and every block. The derivations can be found in the uploaded pdf. 

<img src = Skärmbild 2022-05-15 205135](https://user-images.githubusercontent.com/121384892/212168393-e093951a-aa1e-47f9-a099-1126ce9dd005.png >

The solution of the motion of each block over time is then plotted using matplotlib. After this window has been closed, a PyGame simulation of the development of the system over time will be presented. 
The floor.jpg file is used as a background for the PyGame simulation, but the user is of course to change that to their preferred style. 

NOTE: This code still has some issues that has to be addressed.
