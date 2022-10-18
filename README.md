# Elevator management system
##### Project's target: <br /> 
creating a management system for elevators requests by tenants. <br />
<br />
Elevator types and restrictions- <br />
  o	Fast elevator – work for 10th floor and up, max capacity 5 persons, 1 sec per floor <br />
  o	Standard elevator – work over all floors, max capacity 10 persons and 50KG cargo, 3 sec per floor <br />
  o	Cargo elevator – work for floor number <=5 , max capacity 750KG and 2 persons max, 5 sec per floor <br />
<br />
###### Management-<br />
•	factory: the function creates concrete implementations of a common interface (using the factory method pattern).       				                               The function gets elevation type and return an object type elevator according to the input it received. 
<br />
•	get input: the function requests the tenant's restrictions for ordering an elevator, checks whether the restrictions are correct, and if so, it orders an elevator for him accordingly.
<br />
•	call elevator: the function orders an elevator that meets the tenant's restrictions and can perform the operation in the most ideal way.
If there is no such elevator, she will send a message accordingly.
<br />
The function gets list of elevators and the tenant's restrictions and return an informative string. 
<br />
o	Thread - Multithreading is used to allow the elevator management system to operate in such a way that tenants can order elevators at the same time.
<br />
<br />
###### Elevator- <br />
•	calculate operation time: the function calculates the operation time – time for serving the tenant + time he needs to wait until the elevator will arrive. <br />                   The function gets tenant's current floor and requested floor and return the operation time in secs.
<br />
•	reserve: the function changes the elevator for use and pause it according to the operation time.
<br />
•	is supported: the function checks if there is an elevator that supported the tenant's restrictions.
<br />
•	FastElevetor, StandardElevator, CargoElevator : objects that are inherited from Elevator
<br />
<br />


##### Project's output: <br />
informative string including the chosen elevator type or the elevator status with any problem with reserving an elevator (if a specific elevator needed but in use).

