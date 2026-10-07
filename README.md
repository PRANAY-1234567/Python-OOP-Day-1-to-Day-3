# Python OOP – Day 1 to Day 3

This repository contains my learning notes and practice programs for **Object-Oriented Programming (OOP) in Python**.

The examples cover the basics of classes, objects, class variables, instance variables, methods, and how data can be accessed and modified using objects and class names.

## 📚 Topics Covered

### Day 1 – Classes, Objects & Class Variables

* Creating an empty class using `pass`
* Creating classes and objects
* Reference variables
* Accessing class variables
* Using `ClassName.variable`
* Understanding `__dict__`
* Class variable modification
* Object variable modification
* Understanding how modifications affect multiple objects
* Basic understanding of memory/reference behavior

### Day 2 – Methods & Instance Variables

* Understanding methods in Python
* Instance methods
* The `self` parameter
* Calling methods using an object
* Calling instance methods using the class name
* Understanding object references
* Creating instance variables using `self`
* Passing parameters to instance methods
* Creating and displaying object-specific information

### Day 3 – Accessing Class Variables

* Accessing class variables inside instance methods
* Using `self` to access class variables
* Using `ClassName` to access class variables
* Modifying class variables using an object
* Modifying class variables using the class name
* Difference between class-level and object-level modifications

## 🧠 Key Concepts

### 1. Class

A class is a blueprint used to create objects.

```python
class Student:
    name = "Rohit"
    rno = 32
    branch = "CS"
```

### 2. Object

An object is an instance of a class.

```python
s = Student()
```

Here, `s` is a reference variable that refers to the `Student` object.

### 3. Class Variable

A variable defined directly inside a class is called a class variable.

```python
class Student:
    name = "Rohit"
    rno = 32
```

It can be accessed using:

```python
Student.name
Student.rno
```

### 4. Instance Method

A method that works with an object's data is called an instance method.

```python
class Evening:
    def demo(self):
        print("Welcome to all")

e = Evening()
e.demo()
```

The `self` parameter represents the current object.

### 5. Instance Variable

Instance variables are created using `self`.

```python
class Student:
    def information(self):
        self.name = "XYZ"
        self.age = 21
```

Each object can have its own instance variables and values.

### 6. `__dict__`

`__dict__` can be used to inspect attributes stored in a class or object.

```python
print(Student.__dict__)
```

## 🔄 Class Variable vs Object Variable

One important concept practiced in these examples is the difference between modifying a class variable and creating/modifying an object attribute.

### Modifying through the class

```python
Amazon.product_name = "Mobile"
```

This changes the class variable.

### Modifying through an object

```python
a.product_name = "Laptop"
```

This creates/updates an attribute for that particular object rather than changing the original class variable.

This demonstrates the difference between **class-level data** and **object-level data**.

## 📂 Example Structure

The practice code includes examples such as:

```text
Python OOP
│
├── Classes
├── Objects
├── Reference Variables
├── Class Variables
├── Instance Variables
├── Instance Methods
├── self Parameter
├── __dict__
├── Class Variable Modification
└── Object Variable Modification
```

## 🎯 Learning Objective

The main objective of these programs is to build a strong foundation in **Python Object-Oriented Programming** before moving on to advanced OOP concepts such as:

* Constructors (`__init__`)
* Class methods
* Static methods
* Encapsulation
* Inheritance
* Polymorphism
* Abstraction

## 🛠️ Technologies Used

* **Python 3**
* Any Python IDE or editor such as VS Code, PyCharm, or Jupyter Notebook

## ▶️ How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open the Python file in your preferred IDE.
4. Uncomment the example you want to execute.
5. Run the program.

Example:

```bash
python filename.py
```

## 📌 Note

The code in this repository is primarily written as **learning notes and practice examples**. Some examples are intentionally separated or commented out to demonstrate individual OOP concepts step by step.

## 👨‍💻 Learning Progress

**Day 1:** Classes, Objects & Class Variables
**Day 2:** Methods, `self` & Instance Variables
**Day 3:** Accessing and Modifying Class Variables

This repository will be updated as I continue learning advanced Python OOP concepts.


