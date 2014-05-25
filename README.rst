IPython Plugin for NINJA-IDE
===============================

Version:
********
0.15 First released version.

Why?
****
Because I work with IPython in a daily basic and I think that it would be a great to get a plugin for NINJA-IDE.

How?
****
I use qwebkit module to get a minimal browser to embed it into a plugin, provided the support given by the NINJA-IDE API.
I started to write some code to get a functional working prototype. Later, I found devicenzo coded by Roberto Alsina and I take some code to improve the previous one. 
Now, I have a version (this one, 0.15) ready to release to the public, so here it is...

Requirements
************
NINJA-IDE >= 2.0
IPython >= 1.0
PyQT >= 4.9 (the plugin is not working with PyQt 4.8 because qwebkit module do not support the correct web socket protocol.

Usage
*****
In a terminal type:
$ ipython notebook --no-browser

in any directory you want, remember you will be able to navigate down from that directory.

Then starts NINJA-ide 

MIT License:
************

Copyright (c) 2012 Damián Avila

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
