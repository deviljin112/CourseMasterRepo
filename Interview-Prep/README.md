# Interview Prep (STAR)

## Reminder of STAR

__Situation__: What was the situation you were in?
__Task__: What was the task you needed to complete?
__Action__: What actions did you take?
__Result__: How did your actions influence the outcome (What difference did you actions make? How did that lead to the successful completion of the task?)

## Elevators pitch (TAM)

## Questions

## Agile & SCRUM

- What is Agile(STAR)
  - Agile software development refers to  software development methodologies centered round the idea of iterative development, where requirements and solutions evolve through collaboration between self-organizing cross-functional teams.
  - [Source](https://www.cprime.com/resources/what-is-agile-what-is-scrum/)
- What is Scrum(STAR)
  - Scrum is a subset of Agile. It is a lightweight process framework for agile development, and the most widely-used one. A Scrum process is distinguished from other agile processes by specific concepts and practices, divided into the three categories of Roles, Artifacts, and Time Boxes.
  - [Source](https://www.cprime.com/resources/what-is-agile-what-is-scrum/)
- What is the difference between Agile and Scrum
  - Agile describes a set of guiding principles that uses iterative approach for software development, while Scrum is a specific structure / workflow which is used to implement Agile development.
- Three amigos refers to the primary perspectives to examine an increment of work before, during, and after development.
  - Business
  - Development
  - Testing
- Persona:
  - defines an archetypical user of a system, an example of the kind of person who would interact with

![scrum](scrum.png)

- What are SCRUM:
  - Roles
    - **Scrum Master:** responsible for SCRUM process implementation
    - **Product Owner** responsible for defining Stories and prioritizing the Team Backlog to streamline the execution of program priorities while maintaining the conceptual and technical integrity of the Features or components for the team.
    - [Souce](https://www.scaledagileframework.com/product-owner/)
    - **Team** self-organizing and cross-functional group of people who do the hands-on work of developing and testing the product.
  - Artifacts
  - [Source](https://www.scrumalliance.org/about-scrum/artifacts#:~:text=Scrum%20defines%20three%20artifacts%3A%20Product,a%20potentially%20releasable%20product%20increment.):
    - Product Backlog: everything that needs to be done for the project
    - Sprint Backlog: tasks to be completed in the sprint
    - Potentially Releasable Product Increment at the end of the sprint
  - Events
    - Sprint Planning
    - Daily Scrum
    - Sprint Review
    - Sprint Retrospective

- Methodologies (Differences between them and use cases)
- [source](https://productivehut.com/v-model-agile-waterfall-spiral/):
  - V model
    - The main idea in the V-Model is that development tasks and testing tasks are corresponding activities of equal importance, which is symbolized by the two sides of the “V”- At the base point of the V, the code is written. In the right-hand, upward-sloping branch of the V, testing and debugging is done.
    - ![systems](https://productivehut.com/wp-content/uploads/2018/06/11_4_validation_computer_systems.jpg)
  - Agile
    - promotes development iterations throughout the life-cycle of the project.
    - charactrised by very quick cycles
  - Waterfall
    - The main concept of this model is that only when one development level is completed will the next one be initiated.

- starfish retrospective
  - aims to help teams reflect on varying degrees of actions and activities  rather than simply the traditional what went well or what did not go well.
  - ![starfish](https://mk0teamretrojjm4go5x.kinstacdn.com/wp-content/uploads/2018/09/starfish-example.jpg)
- root cause analysis
  - A classic approach to root-cause analysis to ask "why" five times.
  - Focuses on fixing the *processes* instead of blaming people for mistakes
- Information Radiators with example:
  - generic term for any of a number of handwritten, drawn, printed or electronic displays which a team places in a highly visible location
  - Big Visible Chart
  - An example is our trello board.

### STAR

We use agile approaches everyday during our DevOps course. Though constant incrementation of tasks, morning stand ups, and feedback. Through our use of the trello board we can constantly refer to the task at hand, completed and upcoming.

## SQL

### What is a foreign key

A foreign key is a primary key in another table. This connection links the two tables together. The table containing a foreign key is considered a child table. This allows the child table to access parent table’s data via the foreign-primary key.

### DML DDL

DML also known as Data Manipulation Language. DDL also known as Data Definition Language. These two categories focus on different query commands.
Some of the DDL commands are:

- "CREATE", is used to create a database, table, objects etc.
- "DROP", is used to delete a database or a table.
- "ALTER" is used to modify the structure of a database or a table.
- "TRUNCATE", is used to remove all records from a table.

Some of the DML commands are:

- "INSERT", is used to insert / put data into a table.
- "UPDATE" is used to update an existing record in a table.
- "DELETE", is used to remove a record from a table.

### STAR 2

During my DevOps course, we’ve had the task of creating a SQL database based on the Microsoft Azure system.
Our task was to create a fully functioning database as well as write complex queries to access, sort, and display large data structures from a sample database North Wind.
As my background is in MySQL, I have struggled to use the correct syntax for the tasks and often resulted in an error.
Despite these issues, through after class practice, I’ve successfully been able to create a localhost server as well as execute all tasks set by our lecturer.

## Python

### OOP and Four Pillars

OOP also known as Object Orientated Programming, focuses on developing and organising software development around data, also known as objects, rather than functions and logic. OOP follows four pillars also known as the principles of OOP. These are Encapsulation, Abstraction, Inheritance and Polymorphism.

### TDD

TTD also known as Test Driven Development is an expansion on OOP development. It focuses on creating test objects for our software. It allows for developers to focus on the solution and passing the test cases. This also allows for easily repeatable test cases on every stage of the development to ensure that no other module or object has been hindered during the development process.

### STAR 3

During my DevOps course, we’ve been set a task of creating an OOP based project. We’ve had a set deadline and were expected to present our project to the class.
The project consisted of multiple classes, which had object specific methods as well as their functionality was encapsulated to the task of that class. Classes consisted of parents and children while the data was populated through user input. We also had to set up a separate module which would focus on testing our functionality and ensure that each method performs as expected.
Although previously working with OOP I’ve never created a TDD module. This module was used for holding each of the test cases and it made the development a much smoother experience as at each iteration of the software I was able to test whether my program operates as expected.
I have been able to successfully deploy this application as well as test it which resulted in all passed test cases. Through each iteration I was able to add more test cases in order to find any flaws or errors that may arise due to special case inputs that I’ve incorporated into my classes and methods.

## DevOps

### What is DevOps

DevOps stands for Development Operations. The goal of DevOps is to bridge the gap between the Development team and the Operations team to ensure easily scalable projects, improved communications and teamwork as well as improve the project development life cycle.

### Why DevOps

DevOps allows an institution to narrow the gap between Developers and Operations team. This way there is lower wasted time, material and effectively cost. Often development team will put technical issues onto the operations team, meanwhile operations team may be lacking the frequency of updates that the development team requires to deliver. DevOps focuses on removing those issues by putting the two teams together, through shared responsibility, developing infrastructure as code and automating the pipeline.

### Why did you choose DevOps

I’ve been programming for over 6 years and have finished business management degree. DevOps allows me to combine both my hobby and passion with my education. Through the combination of technical, operational a business knowledge allows me to fully understand the needs of a client from both the business side as well as the technical skills required to deliver the project according to the specification. DevOps allows me to be in the centre of the project life cycle.
