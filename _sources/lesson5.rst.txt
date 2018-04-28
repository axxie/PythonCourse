********************
Lesson 5 - variables
********************

Programs work with all kinds of data: numbers, strings, images, etc. In a program language, typically you
can give a name to some piece of data. Name data is called `variable`. This is what we are going to study
in this lesson.

In python, variables and corresponding data are not equal entities. Variable in python is a *reference* to
data, not the data itself. For now, you can ignore this, but this is important for big programs.

Variables in python a created by using `assignment` operator::

    var = 3

From now on, you can use ``var`` instead of 3 with the same result. You can also `reassign` variable, that is,
change its value after initial assignment. Try a complete example as shown below:

.. code_example:: pycon
    :name: vars_print

    var = 3
    print("4 times var is: ", 4*var)
    var = 4
    print("Now 4 times var is: ", 4*var)

The result is as follows:

.. code_output:: vars_print

The `expression` involving our "var" variable is the same in both prints (4*var), but the result is different.
This approach allows to reuse the same programs to process different data with only minor changes.

TO BE CONTINUED