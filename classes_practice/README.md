## Shool Catalogue

The project aims to create classes for primary and high schools. Because these classes share properties and methods, each will inherit from a parent School class. Our parent and three child classes have the following properties, getters, setters, and methods:

- School
Properties: name, level (one of three strings: 'primary', 'middle', or 'high'), and numberOfStudents 
Getters: all properties have getters
Setters: the numberOfStudents property has a setter
Methods: A __repr__ method that displays information about the school.
 - Primary
Includes everything in the School class, plus one additional property
Properties: pickupPolicy (string, like "Pickup Allowed/Not allowed")
- Middle
Does not include any additional properties or methods
 - High
Includes everything in the School class, plus one additional property
Properties: sportsTeams (like ['basketball', 'tennis'])