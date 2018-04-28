Lesson 2 - logo
===============

Setup
-----

Install logo module

Usage
-----

Type the following program:

.. code_example:: logo
    :name: logo_fd

    from logo import *

    fd(50)

    main()

The easiest way to run these examples is to reuse the same file and only change
the inner part.

Assuming you have the logo module installed and typed the program correctly, you should see the window with the following
contents after pressing ``Shift+F10``:

.. code_output:: logo_fd

Copying and pasting
-------------------

Now, use ``Ctrl+C`` - ``Ctrl+V`` sequence to have `fd(50)` three times, like below:

.. code_example:: logo
    :name: logo_fd3

    from logo import *

    fd(50)
    fd(50)
    fd(50)

    main()

If you press ``Shift+F10``, you should the same picture, but the line is three times longer than before:

.. code_output:: logo_fd3

The reason is that our `fd(50)` command in fact instructs a virtual robot called 'turtle' to walk forward by
50 pixels, drawing the line on the ground (screen) at the same time.

Commenting
----------

As you might expect, if we comment one line out, the total length will be two times longer than original:

.. code_example:: logo
    :name: logo_fd3_comment

    from logo import *

    fd(50)
    #fd(50)
    fd(50)

    main()

The output:

.. code_output:: logo_fd3_comment

The above program is equivalent to the following, where we just tell the turtle to walk by 100 pixels:

.. code_example:: logo
    :name: logo_fd1_100

    from logo import *

    fd(100)

    main()
