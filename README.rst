AMDGPU PowerPlay table editor
=============================

A simple GUI tool to inspect and modify AMD GPU powerplay tables. Tries to
parse tables the same way as Linux driver does.

.. image:: screenshot.png

Installation
------------

Dependencies:

- Python 3.6 or later
- PyQt 5

On recent Debians/Ubuntus::

$ sudo apt-get install python3-pyqt5 python3-pip git
$ pip3 install --user git+https://github.com/amezin/amdgpu-pptable-editor-qt.git

Usage
-----

GUI app::

$ amdgpu-pptable-editor-qt

View current pptable::

$ amdgpu-pptable-editor-qt /sys/class/drm/card*/device/pp_table

``pp_table`` is only writable by root, so you'll have to save the file to a
temporary location and then ``cp`` it back to
``/sys/class/drm/card*/device/pp_table``. Or use ``sudoedit``::

$ env EDITOR=amdgpu-pptable-editor-qt sudoedit /sys/class/drm/card*/device/pp_table

.. Caution::
   You can completely screw up your card by modifying its pp_table.
