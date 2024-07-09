### OOP Basics. Task 2
***
#### Description

Create a class `SchoolMember` which represents any person in school.
Classes `Teacher` and `Student` are inherited from `SchoolMember`. 

Classes should have the same interface with the public `show ()` method.
`Teacher` accepts *name* (str), *age* (int), *salary* (int).
`Student` accepts *name* (str), *age* (int), *grades*.
Move the same logic of initialization to the class `SchoolMember`.

Method `show()` returns string (see string patters in *Example*).

#### Example

    >>> persons = [Teacher("Mr.Snape", 40, 3000), Student("Harry", 16, 75)]

    >>> for person in persons:
           print(person.show())

    "Name: Mr.Snape, Age: 40, Salary: 3000"
    "Name: Harry, Age: 16, Grades: 75"
