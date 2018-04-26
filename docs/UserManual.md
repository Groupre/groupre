# groupre User Manual

## System Requirements

Python 3.6 or better.
Microsoft Excel, LibreOffice Calculator, or some other program able to develop and generate csv files and export them as text-csv files.

## Installation

The program does not require installation for a typical user, it is simply run through a web-app.

## Registration

Users using the groupre web-app for UNC-CH are expected to use single-sign-on through the Onyen service in order to access the web-app.

## Data Field Requirements

Student rows in a text csv file are expected to follow the format of {PID, Name, VIP, Score, Preference(s)}, with VIP being a True/False value, and Preference(s) being an arbitrary list of preferences that apply to the target environment.
Chair rows in a text csv file are expected to follow the format of {CID, TeamID, Attribute(s)}, with Attribute(s) being an arbitrary list of attributes that apply to the target environment.

## Program Use

Go to https://master-groupre.cloudapps.unc.edu, upload your csv files, click run, and download the output.
When the GUI is complete, you will be able to design room templates and blueprints dynamically, and then assign seat properties within that design.

## Troubleshooting

If any errors are received, verify that the input files are in the correct format.

## Current Needs, Should Project End Today

As of 04/26/2018, the current plan for features or prominant issues still standing will be summarized here. The most up-to-date location to find this sort of information will be at the issues page for the groupre repository, located at https://github.com/Groupre/groupre/issues.

* Finished front-end:
  * Finalized Room Builder (Blueprints)
  * Finalized Template Editor (Templates)
  * Ability to save Blueprints and Templates to local machine.
  * Ability to save Blueprints and Templates to server.
    * User actions and ownership determined by Onyen.
  * Ability to process a given Template alongside input Student data.
* Finished back-end:
  * Student-To-Student matching:
    * Design for generalized language to describe matching criteria and rulesets for any given situation by the user.