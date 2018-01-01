Lesson 3 - arithmetic operations
================================

Numbers
-------

You can use plain numbers for printing:

.. code_example:: pycon
    :name: print_numbers

    print("I have", 3, "children")

The output should be like below:

.. code_output:: print_numbers


Arithmetic
----------

Numbers can be combined by using mathematical operations, represented by special symbols.

.. code_example:: pycon
    :name: print_arithmetic

    print("I have", 3, "children")
    print("Their total age is", 2 + 4 + 10)
    print("The total number of their fingers is", 3 * 5 * 2)
    print("The oldest boy is", 10 - 2, "years older than the youngest one")
    print("One child is", 10/4, "times older than another")

The output should be like below:

.. code_output:: print_arithmetic

Logical
-------

It is also possible to test for conditions using `logical` operations. The result of each such operation is
either `True` or `False`. Example is below.

.. code_example:: pycon
    :name: print_logical

    print("Is 3 < 5?")
    print(3 < 5)
    print("Is 3+4 > 5*1?")
    print(3+4 < 5*1)
    print("Is 3*4 == 2*6?")
    print(3*4 == 2*6)

The output should be like this:

.. code_output:: print_logical


Full list
---------

+-------------+-----------------------+
| Operation   | Name                  |
+=============+=======================+
| \+          | Add                   |
+-------------+-----------------------+
| \-          | Subtract              |
+-------------+-----------------------+
| \*          | Multiply              |
+-------------+-----------------------+
| /           | Divide                |
+-------------+-----------------------+
| <           | Less than             |
+-------------+-----------------------+
| >           | Greater than          |
+-------------+-----------------------+
| =           | Equals                |
+-------------+-----------------------+
| <=          | Less than or equal    |
+-------------+-----------------------+
| >=          | Greater than or equal |
+-------------+-----------------------+
