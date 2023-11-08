# < definition scip-python python snapshot-util 0.1 `src.foo`/__init__:
#documentation (module) src.foo

def exported_function():
#   ^^^^^^^^^^^^^^^^^ definition  snapshot-util 0.1 `src.foo`/exported_function().
#   documentation ```python
#               > def exported_function(): # -> Literal['f...
#               > ```
    return "function"

class MyClass:
#     ^^^^^^^ definition  snapshot-util 0.1 `src.foo`/MyClass#
#     documentation ```python
#                 > class MyClass:
#                 > ```
#     documentation This is a class and it is cool
    """This is a class and it is cool"""

    def __init__(self):
#       ^^^^^^^^ definition  snapshot-util 0.1 `src.foo`/MyClass#__init__().
#       documentation ```python
#                   > def __init__(
#                   >   self
#                   > ) -> None:
#                   > ```
#                ^^^^ definition  snapshot-util 0.1 `src.foo`/MyClass#__init__().(self)
        pass

    def exported_function(self):
#       ^^^^^^^^^^^^^^^^^ definition  snapshot-util 0.1 `src.foo`/MyClass#exported_function().
#       documentation ```python
#                   > def exported_function(
#                   >   self
#                   > ): # -> Literal['exported']:
#                   > ```
#                         ^^^^ definition  snapshot-util 0.1 `src.foo`/MyClass#exported_function().(self)
        return "exported"

this_class = MyClass()
#^^^^^^^^^ definition  snapshot-util 0.1 `src.foo`/this_class.
#documentation ```python
#            > src.foo.MyClass
#            > ```
#            ^^^^^^^ reference  snapshot-util 0.1 `src.foo`/MyClass#

