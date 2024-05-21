# API

### What Bash scripting should not be used for?
Bash scripting is powerful for automation and system tasks, but it has its limitations and should not be used for:

- **Complex Application Development:** It lacks advanced programming constructs found in other languages.
- **High-Performance Computing:** Bash is not optimized for performance-critical tasks.
- **Cross-Platform Applications:** Bash is primarily for Unix-like systems and not suited for Windows.
- **GUI Development:** Bash is not designed for building graphical user interfaces.
- **Handling Large Data:** Bash can struggle with large datasets due to limited memory management.

### What is an API?
An API (Application Programming Interface) is a set of rules and protocols for building and interacting with software applications. It defines the methods and data structures that developers use to interact with a service or system, enabling different software programs to communicate with each other

### What is a REST API?
A REST API (Representational State Transfer API) is a type of API that conforms to the constraints of REST architectural style. It uses HTTP requests to perform CRUD operations (Create, Read, Update, Delete) on resources, represented as URLs. REST APIs are stateless, meaning each request contains all the information needed to process it.

### What are Microservices?
Microservices is an architectural style where an application is composed of small, loosely coupled, and independently deployable services. Each service runs a unique process and communicates through well-defined APIs, often over HTTP. This approach allows for greater flexibility, scalability, and easier maintenance.

### What is the CSV Format?
CSV (Comma-Separated Values) is a simple file format used to store tabular data, such as a spreadsheet or database. Each line in a CSV file represents a data record, and each record consists of one or more fields separated by commas.
```
name,age,city
John Doe,30,New York
Jane Smith,25,Los Angeles
```

### What is the JSON Format?
JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate. It uses key-value pairs to represent data objects.
```
{
  "name": "John Doe",
  "age": 30,
  "city": "New York"
}
```

### Pythonic Package and Module Name Style
- **Package Names:** Should be short, all-lowercase, and may use underscores if it improves readability.
`Example: my_package`
- **Module Names:** Should follow the same convention as package names.
`Example: my_module.py`

### Pythonic Class Name Style
- **Class Names:** Should use CapWords (CamelCase) convention.
`Example: MyClass, Person`

### Pythonic Variable Name Style
- **Variable Names:** Should be lowercase, with words separated by underscores to improve readability (snake_case).
`Example: my_variable, user_name`

### Pythonic Function Name Style
- **Function Names:** Should be lowercase, with words separated by underscores (snake_case).
`Example: my_function(), calculate_total()`

### Pythonic Constant Name Style
- **Constant Names:** Should be all uppercase with words separated by underscores.
`Example: MAX_VALUE, PI`

### Significance of CapWords or CamelCase in Python
`CapWords (CamelCase)` is used primarily for class names in Python. It helps to distinguish classes from other identifiers such as variables, functions, and constants. This convention improves code readability and clarity by making it immediately clear when a class is being referenced.