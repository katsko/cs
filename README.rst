Computer Science Practice
=========================

Linked list
-----------

File
````

`linked_list.py <https://github.com/katsko/cs/blob/main/linked_list.py>`_

Test
````

.. code-block:: console

   $ python -m doctest -v linked_list.py

or without *-v* for short output

.. code-block:: console

   $ python -m doctest linked_list.py

Usage
`````

.. code-block:: python

   from linked_list import LinkedList
   ll = LinkedList()
   ll.insert(0, 'a')
   ll.insert(1, 'b')
   ll.get_array()  # ['a', 'b']
   ll.delete(0)
   ll.get_array()  # ['b']
