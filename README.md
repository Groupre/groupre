# groupre

Welcome to the groupre GitHub repository!

## Overview

Groupre is a program written in python meant to allow fast, automated matching of students to chairs based on student preferences, professor settings, and chair attributes.

As a result of being created within the [Software Engineering Lab][COMP 523] course at the [University of North Carolina at Chapel Hill][UNC-CH], this repository contains the groupre python source code as well as the web implementation for professor use of it at UNC-CH. The current web-app locations can be found at our [master][CloudApps-master] and [develop][CloudApps-develop] sites hosted on [Carolina CloudApps][Carolina CloudApps].

## Documentation

Documentation for the groupre project can be found [here][masterDocs], with archives located [here][masterDocsArchive].

In the event that the master documentation is not up to date, you can view the develop documentation [here][developDocs], with archives located [here][developDocsArchive].

## Usage

A prerequisite for using the groupre module is **Python 3**.

Prospective users looking to utilize the groupre python module for a different organization are encouraged to pull the groupre module source code located [here][masterSrc].

Following are the currently available command-line flags you can use when calling groupre:

* **-c** or **--chairs**
  * The chairs input file.
* **-s** or **--students**
  * The students input file.
* **-f** or **--fallback**
  * Enable fallback functionality.
* **-m** or **--metrics**
  * Enable metrics functionality.
* **-o** or **--output**
  * The output file.

<br><br><br>

### Command-Line

You can use the groupre module directly via the command line by entering the following:

```bash
groupre.py -f -c <CHAIRS> -s <STUDENTS> -o <OUTPUT>
```

Where _\<CHAIRS>_, _\<STUDENTS>_, and _\<OUTPUT>_ are file locations for those respective files.

Note: If groupre.py has not been given execution permissions, you may need to preface this command with "python" or your machine's equivalent Python 3 alias.

<br><br><br>

### Python Module Installation

Alternatively, you can install the groupre module and import it directly into another python project.

Installation can be done by calling the following in your terminal emulator of choice while located in the same directory as setup.py (src/groupre):

**For Users:**

```bash
python setup.py install
```

**For Developers:**

```bash
python setup.py develop --user
```

<br>

Calling it can be done by using the following call to groupre's main function:

```python
groupre.main('groupre.py', ARGS)
```

Where ARGS is defined as a list of arguments such as:

```python
ARGS = ['--c', <CHAIRS>, '--s', <STUDENTS>, '--o', <OUTPUT>]
```

Where _\<CHAIRS>_, _\<STUDENTS>_, and _\<OUTPUT>_ are file locations for those respective files.

<br>

**For Developers:** You can uninstall the module by calling the following in your terminal emulator of choice:

```bash
python setup.py develop --user -u
```

<br><br><br>

### Flask

To incorporate the groupre module into a web-app that uses the [Flask][Flask] framework, such as a Python 3 web-app, you can simply include the directory that contains groupre's *setup.py* in the *requirements.txt* and it should be installed when the web-app builds (reference: [OpenShift][OpenShift]/[Carolina CloudApps][Carolina CloudApps]).

Here is an example from our web-app's *requirements.txt*:

```pip requirements
gunicorn
Flask
src/groupre/
```

## License

~~Read our chosen license [here]().~~

<!-- Begin References -->
[UNC-CH]: https://www.unc.edu/
[COMP 523]: https://wwwx.cs.unc.edu/Courses/comp523-f17/deliverables.php
[CloudApps-master]: http://master-groupre.cloudapps.unc.edu/
[CloudApps-develop]: http://develop-groupre.cloudapps.unc.edu/
[Carolina CloudApps]: https://cloudapps.unc.edu/
[masterSrc]: https://github.com/jeyerena/ClassTeamBuilder/tree/master/src/groupre
[masterDocs]: https://github.com/jeyerena/ClassTeamBuilder/tree/master/docs
[masterDocsArchive]: https://github.com/jeyerena/ClassTeamBuilder/tree/master/docs/archive
[developDocs]: https://github.com/jeyerena/ClassTeamBuilder/tree/develop/docs
[developDocsArchive]: https://github.com/jeyerena/ClassTeamBuilder/tree/develop/docs/archive
[Flask]: http://flask.pocoo.org/
[OpenShift]: https://www.openshift.com/
<!-- End References -->