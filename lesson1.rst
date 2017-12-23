Lesson 1 - first steps
======================

Follow the steps for setup, as described in :ref:`create-project`

First program
-------------

Type the following line into main editor window:

.. code_example:: pycon
    :name: hello

    print("Hello, World!")

Now, press ``Shift+F10`` to run the project. You should see the `Run` tab open with the following text:

.. code_output:: hello

.. note:: PyCharm adds it own output to our "Hello, World!". For now you can ignore it. Soon we will launch our
    program outside of the development environment.

More prints
-----------

Let's add more printing. Extend your program with two more prints:

.. code_example:: pycon
    :name: prints

    print("Hello, World!")
    print("Another line?")
    print("More lines.")


Run the above example and you should see this:

.. code_output:: prints

Try to experiment a little. What would happen, if you forget to type ``)`` or ``"``?

Lesson 1 - commenting
---------------------

Put the octothorpe character ('#') as the first character on the second line and run the programm:

.. code_example:: pycon

    print("Hello, World!")
    #print("Another line?")
    print("More lines.")

What happened?

Now, see what happens if you put the same character inside the string being printed:

.. code_example:: pycon

    print("Hello, World!")
    print("Another line?")
    print("More # lines.")

You probably noticed that entire string is printed, including #. The reason is that processing of characters inside
strings is different to other parts of the language. For instance, special characters, such as octothorpe, are
interpreted differently.

As we just saw, you can use # character to "block" lines from execution without actually removing them. This is useful
for disabling some part of the program temporarily. Often this is needed during some experimenting and testing some
new things.

Another good reason to use #, is to provide explanations about the code inside the code itself. This is called
commenting.

Lesson 1 - copying and pasting
------------------------------

If you want to repeat some code, you can use copy-pasting. First you copy the portion of the code into so-called
`clipboard`, put the cursor into destination, and paste copied code from the clipboard to the destination. Here is
how you do it:

1. Select the code by pressing ``Shift`` and using arrow keys to expand the selection
2. Press ``Ctrl+C`` to copy
3. Move the cursor to the new place by either using arrow keys or clicking with the mouse
4. Press ``Ctrl+V`` to paste

Try this new way to produce the following program:

.. code_example:: pycon
    :name: copy-paste

    print("I am going to repeat this.")
    print("I am going to repeat this.")
    print("I am going to repeat this.")
    print("I am going to repeat this.")
    print("I am going to repeat this.")

As expected, when run, it prints the same sentence five times:

.. code_output:: copy-paste

