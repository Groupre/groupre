# groupre Functional Spec

## Concept

The goal of the groupre project is to create an intuitive tool to quickly and automatically place students into both individual seats and small class groups based on the classroom environment, student-oriented preferences, and instructor specifications.

## User Types and Use Cases

### User Stories

As a professor of a large 1XX-level course with over 400+ students, seating assignments can be an extremely tedious and time consuming process. Add to this the fact that my curriculum is designed to benefit from maximum class participation and team-based projects, a tool for this process would be extremely beneficial. Enter groupre, an application designed to take all the relevant student data that I provide alongside a room template that I design, which will then assign Students to Teams based on the criteria I specified alongside an element of randomness. I will then receive seating assignments for all 400+ students within mere seconds as opposed to several hours.

### Personas

#### Left-Handed Student

This is simply a left-handed student who requires a left-handed desk for any writing, reading, or setting up of a laptop for class-related activities.

#### Front-Of-Class Student

This student wishes to sit at or neat the front of the class. Reasons include, but are not limited to, difficulty seeing/hearing the instructor or material presented, a desire to be more focused and/or engaged with the course, or physical considerations such as legroom.

##### Back-Of-Class Student

This student wishes to be seated at or neat the rear of the class. Reasons include, but are not limited to, a wish to be non-intrusive, a requirement to be able to depart the classroom swiftly after class ends, and social concerns.

#### Special Requirements Student

This student wishes or requires special considerations when being placed in the classroom. These considerations include any requirement covered by the Americans with Disabilities Act (ADA).

#### The Lazy Instructor

This is the professor or TA/LA who wants to group his or her students one time at the outset of the semester, get all groups and seating as “perfect” as possible, and wants to leave them in those groups for the remainder of the term.

#### The Communication-Intensive Instructor

This instructor wants to change groups or seating according to class-specific requirements or specifications. The reasons for these regular changes are myriad, but include changing group composition based on exam results, separating problem students or groups, and encouraging diversity and communication between groups and students.

### Use Cases

#### Student

Optimally, students will check Sakai for seating assignments. Students may also be able to check Sakai for group assignments as well, depending on instructor specified parameters.

#### Instructor (One-Time Grouping)

In this case, the instructor obtains and develops the seating and grouping roster from both the initial survey and Sakai information, in the form of a csv. That csv will then be taken as input by our product, which will output a different csv with all of the student-seat pairings sorted by Team ID. The original can, of course, be re-run if necessary, and the final product will be modifiable before finalizing the seating plan and publishing it to Sakai.

#### Instructor (Multiple Group Creation)

This case is initially the same as the One-Time Grouping, but since the program’s parameters will be easily modifiable, the instructor will be able – mid-semester – to account for and adjust the seating assignments based on changes in the class roster, student participation and/or grades, and varying other group dynamics.

## Requirements

The groupre project plans to implement the following feature-set:

* Matching Algorithm
  * Priority Match
  * Random Match
* Matching Mechanics
  * Fallback
    * Handle cases where seats with a desired attribute are not available in a manner which can still satisfy most students.
  * VIP
    * Give preference when matching students to chairs for students who have special needs, as verified or selected by faculty members when necessary.
  * Range Preferences
    * Handle preferences which span a set of applicable attributes.
  * Student-To-Student Matching
    * Handle matching students to teams based on what that team’s current student composition is.
* Web Interface
  * Target audience: UNC-CH Faculty
  * Single Sign-On (ONYEN)
  * Room Blueprint Creation & Saving
    * Specify the coordinates and basic attributes of chairs for a given room.
  * Room Template Creation & Saving
    * Specify class-specific team layouts and/or apply extra attributes to a chosen room blueprint.
  * Allow Fine-Tuning of Results
    * User should be able to tweak the results of the matching algorithm by hand through an intuitive GUI before receiving the final results. They should also be able to re-run the sorting algorithm if they are unsatisfied with prior results.
  * Readable, Interactive User Interface
    * User should be able to visually identify students that have unmet preferences, or be able to tell at a glance what attributes belong to which chairs.

## Interfaces

### Data

#### Student Data

All student input data should be in text csv file format, with a layout consisting of (and in the following order) for any given row in the csv file:

* PID
* Name
* VIP
* Score
* Preference(s)

Student preferences pertaining to chairs are expected to have a corresponding attribute available in the target chairs input file used.
Student preferences can consist of the following types:

* Chair Preferences
  * Ex: “front” or “front-0”, which corresponds to the front row of seats.
* Range Preferences
  * Ex: “front-0:6”, which spans the first 7 rows of seats from the front backwards.
* Student Preferences
  * Ex: “gender”, which will be used to create groups of students based on those who have the same attribute.

#### Chair Data

All chair input data should be in text csv file format, with a layout consisting of (and in the following order) for any given row in the csv file:

* CID
* TeamID
* Attribute(s)

Chair attributes are expected be a member of the following set:

* front
* back
* aisle
* left-handed
* etc.

### Rules and Priorities

Sorting will be accomplished in accordance with the following rules, which have accompanying priorities. Priorities are values assigned to student preferences that assist in giving Students who want rarer seat options a slight priority over other students not looking for such seats. Chairs are assigned based on which one provides the maximum “satisfaction” rating for a given Student.

* Students who are given the VIP attribute by an instructor will be given the highest priority among all other students.
* Students who have any preferences at all are next in line, with those that have preferences of higher value being sorted such that they will be serviced first.
* Students who have no preferences at all will be randomly assigned to Chairs as the last section of data that is processed by the groupre module.