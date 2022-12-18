# html-src
This program checks if a website has been updated since "html-src" was launched.

# What you can do
"html-src" will check every 5 minutes the url you chose until the page will be updated or if you close the program.  
You can save urls (in the app) so you don't need to write them every time.  
You can delete urls (in the app) if you don't need them anymore.

# To do
You have to set the variable "fileLocation" (line 8) with the location of your csv file to be able to save urls. If there is no file the program will make it.

# Input format
You need the write the whole url, http/https included.  
Example:  
YES https://github.com/itsraval/  
NO  github.com/itsraval/  

# Used libraries
* requests
* hashlib
* time
* webbrowser
* cvs
