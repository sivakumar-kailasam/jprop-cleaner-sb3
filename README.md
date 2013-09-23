jprop-cleaner
=============

A Sublime text 3 plugin to remove multiple occurrences of a key in java property files.

Sometimes we end up having duplicate entries of the same key due to merge issues in source control (I'm looking at you svn!) or other reasons. This is something I whipped up to remove such duplicate entries and preserve the last key value pair because that's the one resource bundle class ends up selecting from the file. 


If you want to know the duplicate entries in the file open up the SublimeText3 console using ctrl+` to see the list of keys.

Shortcut keys:
* On windows & linux ctrl+shift+j, ctrl+shift+c
* On mac cmd+j, cmd+c

Definitely open to suggestions and ideas to improve this :)


Installation:
-------------
In case you haven't setup sublime package control before here's the official page - https://sublime.wbond.net/installation

This plugin is now available officially through the sublime package control. Search for 'Java property cleaner' and install it.


Why a separate repo for the same plugin?
----------------------------------------
Sublime text 3 uses Python 3 so the plugin had to be ported to work on Sublime text 3 but I still want to support the ST2 users, that's why! :)