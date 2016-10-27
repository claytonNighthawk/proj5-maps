# proj5-maps
Project for mapping near by Points of Interest with Google Maps API

### What do I need?  Where will it work? ###

* Designed for Unix, mostly interoperable on Linux (Ubuntu) or MacOS.
  Target environment is Raspberry Pi. 
  ** May also work on Windows (at least the W10 Ubuntu bash) or a Linux virtual machine
   out of the box depending on your pyvenv package command name. Program might require manual configuration with `. env/bin/activate`, `make configure` and `pip install -r requirements.txt` or changing the PYVENV command name in templates.d/Makefile.standard between pyvenv and virtualenv. I could not get "pyvenv" to install on my pi or anywhere else but virtualenv worked everywhere.    
   
* You will also need Python version 3.4 or higher. 
* Designed to work in "user mode" (unprivileged), therefore using a port 
  number above 1000 (rather than port 80 that a privileged web server would use)

## In your workspace

`bash ./configure` or `make run` should create appropriate configuration files on
most Unix files.   If you are using Windows, some additional editing
of configuration files may be necessary (similar to what was mentioned above).  You might have to edit the
Makefile to find the right version of pyvenv.

If you can run flask applications in your development environment, the
application would might be run by
`   python3 flask_maps.py` or `make run`
and then reached with url
`   http://localhost:5000`

## Points of Interest
Project will populate map with points of interest taken from a data file. Map will also drop a pin when clicked and tell the user what address that pin was dropped at. 
