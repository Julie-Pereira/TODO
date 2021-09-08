"""
Module main
===============

Contains the main classes for creating the todo application


"""

class Todo():
    """ class that contains the Todo object """

    def __init__(self, title=None, states=None):
        """ Constructor of the Todo class """
        
        self.title = title
        self.states = states