.. _alphalogic_api3:

API Documentation
*****************

.. py:module:: alphalogic_api3.objects


Objects
=======

.. _root_link:

Root
~~~~
To specify a root object of the user-written adapter, you must create a class that inherits from class Root:
::

    from alphalogic_api3.objects import Root
    ......
    class MyRoot(Root):
        ......

.. autoclass:: Root
   :members:

.. _object_link:

Object
~~~~~~
To specify an adapter object (not Root object), create a class that inherits from the class Object:
::

    from alphalogic_api3.objects import Object
    ......
    class Controller(Object):
        ......

.. autoclass:: Object
   :members:



.. _parameter_link:

Parameter
~~~~~~~~~
| You have to define parameter, depending on its value type:
| ParameterBool, ParameterLong, ParameterDouble, ParameterDatetime, ParameterString, ParameterList, ParameterDict

Example of parameter definition:
::

    from alphalogic_api3.objects import ParameterBool, ParameterLong, ParameterDouble, ParameterDatetime,
                                        ParameterString, ParameterList, ParameterDict
    ...

    message = ParameterString(default='Hello world!')

Read and write parameter value:
::

    self.message.val = 'Me too'
    self.param_str.val = self.message.val


Parameter arguments are optional.

.. table:: Parameter arguments

    +-------------+---------------------------+------------------------+----------------------------+
    | Argument    | Description               | Default Value          | Possible Values            |
    +=============+===========================+========================+============================+
    | default     | Default parameter value   | | 0 (ParameterLong)    | | All the values of the    |
    |             |                           | | False (ParameterBool)| | corresponding type are   |
    |             |                           | | 0.0 (ParameterDouble)| | allowed (for example,    |
    |             |                           | | 0 (ParameterDatetime)| | a parameter of           |
    |             |                           | | "" (ParameterString) | | ParameterDouble can      |
    |             |                           | | [] (ParameterList)   | | hold real numbers)       |
    |             |                           | | {} (ParameterDict)   |                            |
    +-------------+---------------------------+------------------------+----------------------------+
    | visible     | | A parameter type that   | Visible.runtime        | | Visible.runtime - used   |
    |             | | specifies its features  |                        | | to transfer data from    |
    |             | | and visibility in the   |                        | | integrated device or     |
    |             | | Alphalogic Studio       |                        | | subsystem into           |
    |             |                           |                        | | Alphalogic               |
    |             |                           |                        |                            |
    |             |                           |                        | | Visible.setup - used to  |
    |             |                           |                        | | configure adapter        |
    |             |                           |                        | | object's properties      |
    |             |                           |                        |                            |
    |             |                           |                        | | Visible.hidden - used to |
    |             |                           |                        | | store some data that     |
    |             |                           |                        | | must be hidden for       |
    |             |                           |                        | | target user, e.g.        |
    |             |                           |                        | | adapter license key      |
    |             |                           |                        |                            |
    |             |                           |                        | | Visible.common - a       |
    |             |                           |                        | | hybrid of                |
    |             |                           |                        | | Visible.runtime and      |
    |             |                           |                        | | Visible.setup            |
    |             |                           |                        | | parameter types          |
    |             |                           |                        | | providing combined       |
    |             |                           |                        | | functions                |
    +-------------+---------------------------+------------------------+----------------------------+
    | access      | | A parameter access type | Access.read_write      | | Access.read_write        |
    |             | | which specifies the     |                        | | Access.read_only         |
    |             | | permitted and prohibited|                        |                            |
    |             | | uses of the parameter   |                        |                            |
    +-------------+---------------------------+------------------------+----------------------------+
    | choices     | | Allows to set up a      |                        | | The enumeration can be   |
    |             | | predefined enumeration  |                        | | specified in one of two  |
    |             | | of values for the       |                        | | different ways:          |
    |             | | parameter               |                        | | 1) list of values of the |
    |             |                           |                        | | corresponding type in a  |
    |             |                           |                        | | tuple as (value1,        |
    |             |                           |                        | | value2, ..., valueN)     |
    |             |                           |                        | | 2) list of enumeration   |
    |             |                           |                        | | members in a tuple of    |
    |             |                           |                        | | tuples as ((value1,      |
    |             |                           |                        | | 'enum_name1'), (value2,  |
    |             |                           |                        | | 'enum_name2'), ...,      |
    |             |                           |                        | | (value2, 'enum_nameN'))  |
    +-------------+---------------------------+------------------------+----------------------------+


To build a value list for the parameter, it is required that both arguments 'choices' and 'default' are specified.
::

    param_tmp = ParameterLong(visible=Visible.setup, access=Access.read_write, default=1,
                              choices=((1, 'First'), (2, 'Second')))

Second approach to build value list for parameter:
::

    param_tmp = ParameterLong(visible=Visible.setup, access=Access.read_write, default=1, choices=(1, 2))

Be careful to assign a value (not an enumeration member's name) to 'default' argument if the 'choices' argument provides enumeration with descriptions:
::

    param_tmp2 = ParameterBool(default=True, choices=((True, 'On'), (False, 'Off')))

Here is the definition of the class Parameter:

.. autoclass:: Parameter
   :members:

.. _event_link:

Event
~~~~~
| You have to define event, depending on its severity level:
| TrivialEvent, MinorEvent, MajorEvent, CriticalEvent, BlockerEvent

To define an event with arguments, you must append a tuple of (argument name, argument type) pairs. The names of the arguments must be enclosed with single or double quotes.

Example of event definition:
::

   alarm = MajorEvent(('where', str), ('when', datetime.datetime), ('why', long))

| The possible value types of the event arguments are:

* str – used for string data,
* datetime.datetime – used for date and time,
* long – for integer values,
* float – to store real numbers,
* bool – used for boolean values.

The function that triggers an event occurence (emit) can be passed with the event arguments as a tuple of name/value pairs, each argument name followed by an equal sign:
::

    alarm.emit(where="Red Square, Moscow", when=datetime.datetime(2018, 12, 31), why=123456)

Python allows you to pass functions as a parameters to another functions. In the present case, function can be passed instead of the value for the event argument:
::

    alarm.emit(where="Red Square, Moscow", when=datetime.datetime.utcnow(), why=123456)

Example of the event function without arguments:
::

    alarm.emit()


Here is the definition of the class Event:

.. autoclass:: Event
   :members:


Decorators
~~~~~~~~~~
A decorator is any callable Python object that is used to modify a function, method or class definition.
A decorator is passed the original object being defined and returns a modified object, which is then bound to the name in the definition.
Decorators are used for creating class methods or static methods, adding function attributes, tracing, setting pre- and postconditions, etc.
The @ special character is used to indicate a decorator.

.. py:module:: alphalogic_api3.decorators

.. _command_link:

Command
-------
Possible values for result type are: str, datetime.datetime, int, float, bool, list, dict.
Here is the definition of the class Command:

.. autoclass:: command
   :members:


Run functions
-------------
There is easy way to do some job periodicaly. You can define a lot of run functions in the root or object.

.. autoclass:: run
   :members:


.. py:module:: alphalogic_api3.exceptions

Handlers
~~~~~~~~

The handlers are executed when the corresponding condition occurs.
There are three types of handlers which can be installed to control the workflow of the adapter before or after calling some functions:

1) Request on child objects of the adapter object:
::

    def handle_get_available_children(self):
        return [
            (Controller, 'Controller'),
            (MyObject, 'MyObject')
        ]

You can define and implement this function in the object class to return an array of the child adapter objects.
You must use the exact name of the handler as in the example above.

2) Request on deletion of the adapter object(s):
::

    def handle_before_remove_device(self):
        do something

You can use this handler to do something before the adapter object will be deleted.
You must use the exact name of the handler as in the example above.

3) Changing the value of the parameter:
::

    def handle_after_set_double(node, parameter):
        node.log.info('double changed')
        node.after_set_value_test_event.emit(value=parameter.val)

    param_double = ParameterDouble(default=2.3, callback=handle_after_set_double)

The handler will be invoked when the specified parameter is changed.
In the example above, this means that the function handle_after_set_double will be called if param_double is changed.
In the case of parameter changes, you can use whichever name of the handler function you like.

4) Handler for configure Object after creation by user
::

    number = ParameterLong(visible=Visible.setup)
    def handle_defaults_loaded(self, **kwargs):
        self.displayName.val = str(self.number.val)

5) Handler is executed before work of object
::

    number = ParameterLong(visible=Visible.setup)
    def handle_prepare_for_work(self):
        self.displayName.val = str(self.number.val)


Оbject lifetime
~~~~~~~~~~~~~~~

Created by user
---------------

* ``__init__``. You can't do anything with parameters, events, commands here.
* Create parameters, events, commands
* Accept values from ``__init__`` kwargs. See `Advanced using` p.1.
* ``handle_defaults_loaded`` handle
* ``handle_prepare_for_work`` handle

Loaded from configuration
-------------------------
* ``__init__``. You can't do anything with parameters, events, commands here.
* Create parameters, events, commands
* ``handle_prepare_for_work`` handle

Removed by user
---------------
* ``handle_before_remove_device``

Advanced using
~~~~~~~~~~~~~~
1) Create a child object with predefault values:
::

    class Controller(Object, DiagHelper):
        some_parameter_title = ParameterLong(default=0)

    def handle_get_available_children(self):
        children = []  # return empty list if exception
        try:
            p = partial(Controller, some_parameter_title=0)
            p.cls = Controller
            children.append((p, 'Controller 0'))

            # You can set parameter values in
            p = partial(Controller, some_parameter_title=1, displayName=h['name'])
            p.cls = Controller
            children.append((p, 'Controller 1'))

        except Exception as err:
            log.error(err.message)
        return children

Handlers order example
----------------------
1) Situation 1: User creates object
::

    class Controller(Object):

        def __init__(self, type_device, id_device, **kwargs):
            super(Controller, self).__init__(type_device, id_device, **kwargs)
            # 1: Partial arguments in the kwargs

        def handle_defaults_loaded(self, **kwargs):
            # 2: Partial arguments in the kwargs

        def handle_prepare_for_work(self):
            # 3: Parameters, commands, events created and have default values

        def handle_before_remove_device(self):
            # remove object by user

2) Situation 2: Object has been loaded from configuration
::

    class Controller(Object):

        def __init__(self, type_device, id_device, **kwargs):
            super(Controller, self).__init__(type_device, id_device, **kwargs)
            # 1: nothing in the kwargs

        def handle_defaults_loaded(self, **kwargs):
            # Not called

        def handle_prepare_for_work(self):
            # 2: Parameters, commands, events created.
            #    Values from configuration loaded.

Arbitrary object type
---------------------
Alphalogic objects have ``type`` attribute. By default, it's set to Python object's class name. For example, an object of Python class ``MyObject`` has ``MyObject`` alphalogic object type.
However, you may want to set an alphalogic type, which cannot be represented by Python class name, like ``access.wipepoint``. Such names are usually required for ACS adapters.
In this case, two steps should be done to set an arbitrary type attribute.

First, in the list returned from parent's ``handle_available_children()`` method, corresponding item should be represented by a tuple with 3 elements where the last element is the required type name.

Second, before creating root object, this type should be registered with ``Manager.add_device("type name", ClassName)`` method.

Example:
::
    class AccessWipepoint(Object):
        # This device has alphalogic type "access.wipepoint"
        pass

    class RootDevice(Root):
        def handle_get_available_children(self):
            # Set device type in a tuple (the last item)
            return [(AccessWipepoint, "access wipepoint device", "access.wipepoint")]

    if __name__ == "__main__":
        # Add device AccessWipepoint to alphalogic-api with device type "access.wipepoint"
        Manager.add_device("access.wipepoint", AccessWipepoint)

        # main loop
        root = RootDevice()
        # ...


If you need to set arbitrary type for the root object, this type must be set in the C++ part of your adapter.

Dynamic object components
-------------------------
Besides adding a component (parameter, command, event) as a class attribute, components can be added dynamically since alphalogic_api v0.1.9.
Repeated addition overwrites the previous one.
::

    @run(period_one=3)
    def run_function(self):
        # Dynamic switching of attributes and parameters of dynamic_event
        event_class = random.choice([TrivialEvent, MinorEvent, MajorEvent, CriticalEvent,
                                     BlockerEvent])
        param_type = random.choice([int, bool, str])
        param_name = random.choice(["foo", "bar", "baz"])
        if param_type is int:
            param_value = random.randint(0, 10)
        elif param_type is bool:
            param_value = random.choice([True, False])
        elif param_type is str:
            param_value = random.choice(["value1", "value2", "value3", "value4", "value5"])
        else:
            assert False, "Impossible branch"

        event = event_class((param_name, param_type))
        
        # Add dynamic event (not added as class attribute)
        # Can be called after Object's constructor
        Object.manager.add_event_to_object(self, "dynamic_event", event)
        event.emit(**{param_name: param_value})

        # Dynamic command example
        # Handler, parameters, choices, default values can be changed
        # Result type MUST NOT be changed
        @command(result_type=bool, param1={"default": "default", "val1": "value1", "val2": "value2"})
        def dynamic_command1(self, param1="default", param2=0):
            log.info("param1={}, param2={}".format(param1, param2))
            return True

        @command(result_type=str, p1={"default": 0, "v1": 1, "v2": 2})
        def dynamic_command2(self, p1=0, p2=True):
            log.info("p1={}, p2={}".format(p1, p2))
            return "OK"

        # Can be called after Object's constructor
        Object.manager.add_command_to_object(self, "dynamic_command",
                                             random.choice([dynamic_command1, dynamic_command2]))


        # Dynamic parameter: attributes and choices can be changed
        # Type MUST NOT be changed
        p = random.choice([ParameterLong(visible=Visible.setup, access=Access.read_write,
                                         choices=((1, "one"), (2, "two"))),
                           ParameterLong(visible=Visible.runtime, access=Access.read_only,
                                         choices=((1, "ONE"), (2, "TWO")))])
        
        # Can be called after Object's constructor
        Object.manager.add_parameter_to_object(self, "dynamic_parameter", p)
        
Exceptions
~~~~~~~~~~

.. autoclass:: IncorrectRPCRequest

.. autoclass:: RequestError

.. autoclass:: ComponentNotFound

.. autoclass:: Exit

