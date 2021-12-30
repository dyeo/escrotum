Scrotre (SCReenshOT REdux)
========

Linux screen capture and screen recording program inspired by scrot, forked from `escrotum <https://github.com/Roger/escrotum>`_.


Why fork escrotum?
----

Because the main developer has said that they don't have the time/resources to develop the project further, and I need a version with a few key fixes to add it to my workflow. I figured this would be a good open source project to maintain, so here we are.


Features
--------

* Fullscreen screenshots
* Screen recording
* Partial (selection) screenshots and recordings
* Window screenshot (click to select)
* Screenshot by xid
* Copy the image to the clipboard

::

    usage: scrotre [-h] [-v] [-s] [-x XID] [-d DELAY]
                   [--selection-delay SELECTION_DELAY] [-c] [-C] [-e COMMAND]
                   [-r]
                   [FILENAME]

    positional arguments:
      FILENAME              image filename, default is
                            %Y-%m-%d-%H%M%S_$wx$h_scrotre.png

    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         output version information and exit
      -s, --select          interactively choose a window or rectangle with the
                            mouse, cancels with Esc or Right Click
      -x XID, --xid XID     take a screenshot of the xid window
      -d DELAY, --delay DELAY
                            wait DELAY seconds before taking a shot
      --selection-delay SELECTION_DELAY
                            delay in milliseconds between selection/screenshot
      -c, --countdown       show a countdown before taking the shot (requires
                            delay)
      -C, --clipboard       store the image on the clipboard
      -e COMMAND, --exec COMMAND
                            run the command after the image is taken
      -r, --record          screen recording. Alt+Ctrl+s to stop the recording

      SPECIAL STRINGS
      Both the --exec and filename parameters can take format specifiers
      that are expanded by scrotre when encountered.

      There are two types of format specifier. Characters preceded by a '%'
      are interpreted by strftime(2). See man strftime for examples.
      These options may be used to refer to the current date and time.

      The second kind are internal to scrotre and are prefixed by '$'
      The following specifiers are recognised:
      	$f image path/filename (ignored when used in the filename)
      	$u a one-time uuid
      	$w image width
      	$h image height
      Example:
      	scrotre '%Y-%m-%d-%H%M%S_$wx$h_scrotre.png'
      	Creates a file called something like 2013-06-17-082335_263x738_scrotre.png

      EXIT STATUS CODES
      1 can't get the window by xid
      2 invalid pixbuf
      3 can't save the image
      4 user canceled selection
      5 can't grab the mouse
      6 error with ffmpeg

Install
-------

* on archlinux, install with your favorite aur manager, ie. yay -S scrotre-git
