Unicorn HAT Examples
====================

These files are copied from: https://github.com/pimoroni/unicorn-hat

For instructions on how to install the libraries required and the most
current files, please visit Pimoroni's repository at the above link.

Note: some of these files may be modified from the original 

By virture of the Unicorn HAT being a HAT(!), and hence using the Raspberry Pi's GPIO pins, all of these examples must be run with `sudo`, for example

    sudo ./clock.py

or

    sudo python clock.py    


clock.py
--------

Uses `graphics.py` and shows how you can, but probably shouldn't, display an analogue clock on Unicorn HAT!


demo.py
-------

Multi-effect demo;  twisty swirly goodness, roto-zooming checker board, weeee waaaah, rainbow search spotlights and zoom tunnel


matrix.py
----------

Knock, knock, Neo.


rainbow.py
----------

Demonstrates the use of `colorsys` to animate through colour hues.


rainbow_blinky.py
-----------------

Blinks a rainbow spot light on and off. Change `fwhm` to make the spot more/less focused (smaller numbers = more focused/larger numbers = less focused).


random_blinky.py
----------------

Blinks random yellow-orange-red LEDs.


random_sparkles.py
------------------

Random multi-coloured sparkles.



show_png.py
-----------

Shows how you can open and display a PNG image file, great for sprite animations.

**Requirements:**

    sudo pip install pillow


simple.py
---------

Sets each pixel in turn and updates the display.
