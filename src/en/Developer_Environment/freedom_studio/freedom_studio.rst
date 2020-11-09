Freedom Studio
==============

This document describes the use of Freedom Studio.

Importing a project
-------------------

- First of all, start ``Freedom Studio``, open ``File > import`` on the toolbar and select ``Existing Projects into Workspace`` option under ``General`` menu to import projects.


.. figure:: imgs/image01.png
   :alt:

.. figure:: imgs/image02.png
   :alt:

Debug
-----

- First let the board run, use the shortcut key ``F11`` to start Debug, Freedom Studio will compile the project first (make sure the .launch file name is bl_iot_sdk_debug_freedom_studio.launch when you use the shortcut key, you can use the toolbar Run > Debug As > Make View)

- Use the shortcut key ``F8`` to resume, you can see the program stops at ``void bfl_main()`` main function, now you can click the three buttons in the following figure. Their meanings are

   - First Step Into (F5) Single-step execution, entering and continuing single-step execution when sub-functions are encountered.

   - The second Step Over (F6) does not go into subfunctions when encountered within a function during single-step execution, but instead stops the entire execution of the subfunctions as a single step.

   - The third Step Return (F7) is used to finish the remainder of the sub-function and return the previous level function when a single step is executed into the sub-function.

.. figure:: imgs/image05.png
   :alt:

.. figure:: imgs/image06.png
   :alt:

-   You can add and delete breakpoints by double-clicking on the leftmost orange bar of the ``code`` window.

.. figure:: imgs/image08.png
   :alt:

- You can also view the corresponding assembly by looking at the ``Disassembly`` window on the right (if that window is not available, you can add it by using ``Window > show view > Disassembly`` in the top toolbar).

.. figure:: imgs/image07.png
   :alt:
