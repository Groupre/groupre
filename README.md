# Groupre's development has been moved from Github to Gitlab: https://gitlab.com/unc-cs-toolsmiths/groupre
# groupre

Welcome to the groupre GitHub repository!

## Overview

Groupre is a program written in python meant to allow fast, automated matching of students to chairs based on student preferences, professor settings, and chair attributes.

As a result of being created within the [Software Engineering Lab][COMP 523] course at the [University of North Carolina at Chapel Hill][UNC-CH], this repository contains the groupre python source code as well as the web implementation for professor use of it at UNC-CH. The current web-app locations can be found at our website [groupre.cs.unc.edu][website].

## Documentation

Documentation for the groupre project can be found [here][masterDocs], with archives located [here][masterDocsArchive].

In the event that the master documentation is not up to date, you can view the develop documentation [here][developDocs], with archives located [here][developDocsArchive].

## Usage

### Prerequisites

* [Python 3.7][Python3]


### General Information

Prospective users looking to utilize the groupre python module for a different organization are encouraged to pull the groupre module source code located [here][masterSrc].

Here are the currently available command-line flags you can use when calling groupre:

* **-c \<CHAIRS>** or **--chairs \<CHAIRS>**
  * The chairs input file.
* **-s \<STUDENTS>** or **--students \<STUDENTS>**
  * The students input file.
* **-f** or **--fallback**
  * Enable fallback functionality.
* **-m** or **--metrics**
  * Enable metrics functionality.
* **-g** or **--gender**
  * Enable gender functionality.
* **-o \<OUTPUT>** or **--output \<OUTPUT>**
  * The output file.

<br>

### Running groupre  Directly

You can use the groupre module directly via the command line by entering the following:

```bash
groupre.py -f -c <CHAIRS> -s <STUDENTS> -o <OUTPUT>
```

Where _\<CHAIRS>_, _\<STUDENTS>_, and _\<OUTPUT>_ are file locations for those respective files.

Note: If groupre.py has not been given execution permissions, you may need to preface this command with "python" or your machine's equivalent Python 3 alias.

<br>

### Using groupre as a Python Module

#### Python Module Installation

Alternatively, you can install the groupre module and import it directly into another python project.

Installation can be done by calling the following in your terminal emulator of choice while located in the same directory as setup.py (src/groupre):

<!-- **For Users:**

```bash
python setup.py install
```

**For Developers:** -->

```bash
python setup.py develop --user
```

<br>

#### Python Module Usage

Running the module can be done by using the following call to groupre's main function:

```python
groupre.main('groupre.py', ARGS)
```

Where ARGS is defined as a list of arguments such as:

```python
ARGS = ['-c', <CHAIRS>, '-s', <STUDENTS>, '-o', <OUTPUT>]
```

Where _\<CHAIRS>_, _\<STUDENTS>_, and _\<OUTPUT>_ are file locations for those respective files.

<br>

<!-- **For Developers:**  -->

#### Python Module Uninstallation

You can uninstall the module by calling the following in your terminal emulator of choice:

```bash
python setup.py develop --user -u
```

### Developing with Flask

Developers looking to modify html files need to look in the *templates* directory. All other relevant files can be found (and should be stored) in the *static* directory.

## Built With

* [Flask][Flask] - The web framework used for our Carolina CloudApps deployment.
* [gunicorn][gunicorn] - A Python WSGI HTTP Server for UNIX.

## Contributing

View our [CONTRIBUTING.md][contributing_file] file for details.

## Versioning

An official versioning template has not yet been chosen.

## License

View our chosen [LICENSE][license_file] file for details.

<!-- Begin References -->
[UNC-CH]: https://www.unc.edu/
[COMP 523]: https://wwwx.cs.unc.edu/Courses/comp523-f17/deliverables.php
[CloudApps-master]: http://master-groupre.cloudapps.unc.edu/
[CloudApps-develop]: http://develop-groupre.cloudapps.unc.edu/
[Carolina CloudApps]: https://cloudapps.unc.edu/
[CloudApps_console]: https://console.cloudapps.unc.edu
[CloudAppsStorage_help]: https://help.unc.edu/help/carolina-cloudapps-increasing-the-size-of-a-persistent-volume/
[masterSrc]: https://github.com/jeyerena/ClassTeamBuilder/tree/master/src/groupre
[masterDocs]: https://github.com/jeyerena/ClassTeamBuilder/tree/master/docs
[masterDocsArchive]: https://github.com/jeyerena/ClassTeamBuilder/tree/master/docs/archive
[developDocs]: https://github.com/jeyerena/ClassTeamBuilder/tree/develop/docs
[developDocsArchive]: https://github.com/jeyerena/ClassTeamBuilder/tree/develop/docs/archive
[Flask]: http://flask.pocoo.org/
[OpenShift]: https://www.openshift.com/
[contributing_file]: https://github.com/jeyerena/ClassTeamBuilder/tree/master/CONTRIBUTING.md
[license_file]: https://github.com/jeyerena/ClassTeamBuilder/blob/master/LICENSE
[Python3]: https://www.python.org/downloads/
[gunicorn]: http://gunicorn.org/
[website]: http://groupre.cs.unc.edu
<!-- End References -->
