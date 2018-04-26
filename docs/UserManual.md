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

* Finished web-app GUI
* Interaction between web-app GUI and back-end module
* Debugging
* Finalization of CloudApps integration