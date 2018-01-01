Lesson 4 - more logo
####################

It is time for more operations with logo. In addition to just moving forward and drawing, virtual robot (turtle)
can do more sophisticated things.

Direction
*********

By issuing `left` and `right` commands we can instruct turtle to change direction. Both commands accept a single
parameter - an angle. `left` turns turtle left by `angle` degrees, `right` does the same to the right. You can see
an example below:

.. code_example:: logo
    :name: logo_left

    from logo import *

    fw(50)
    left(90)
    fw(50)
    right(90)
    fw(50)

    main()

This should produce the following polygonal line:

.. code_output:: logo_left

That is getting interesting, huh?

Let's try drawing some more figures:

A square
--------

.. code_example:: logo

    from logo import *

    fw(100)
    left(90)
    fw(100)
    left(90)
    fw(100)
    left(90)
    fw(100)
    left(90)

    main()


A triangle
----------

.. code_example:: logo

    from logo import *

    fw(100)
    left(120)
    fw(100)
    left(120)
    fw(100)
    left(120)

    main()


An interesting figure
---------------------

.. code_example:: logo

    from logo import *

    left(60)
    fw(100)
    right(120)
    fw(100)
    left(120)
    fw(100)
    right(120)
    fw(100)
    left(120)
    fw(100)

    main()

A star
------

This time you can just copy and paste the program from here::

    from logo import *

    fw(100)
    right(144)
    fw(100)
    right(144)
    fw(100)
    right(144)
    fw(100)
    right(144)
    fw(100)
    right(144)

    main()


Pen control
***********

The turtle can handle two more commands, `up` and `down`:

 * *up* tells the turtle to stop drawing when it moves
 * *down* instructs the turtle to resume the drawing during move

This allows to draw disjoint figures, such as the following:

.. code_example:: logo
    :name: logo_up_down

    from logo import *

    fw(100)
    left(90)
    fw(80)
    left(90)
    fw(100)
    left(90)
    fw(80)
    left(90)

    up()
    fw(20)
    left(90)
    fw(20)
    right(90)
    down()

    fw(60)
    left(90)
    fw(40)
    left(90)
    fw(60)
    left(90)
    fw(40)
    left(90)

    main()

You should see two rectangles:

.. code_output:: logo_up_down

