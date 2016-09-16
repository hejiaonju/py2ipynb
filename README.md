# py2ipynb
This is a script to convert from python (.py) to jupyter notebook. It is tested under Python 3.5.2, Ipython version 4.2.0.

Two cell types are recognized, code and markdown, starting with "#%%" and "#%%#" respectively. Each line in markdown cell should be prepended with a "#". The header of the python script can start with "#" (but not "#%%"). Header is ignored in the conversion. 
