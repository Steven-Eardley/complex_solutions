"""Generate code for object attributes (getter/setters) from a dict of {attr : "docstring"}"""

strtemp =\
"""
    @property
    def {0}(self):
        \"\"\"{1}\"\"\"
        return self._{0}

    @{0}.setter
    def {0}(self, val):
        self._{0} = val"""

# Example dictionary of attributes
attrib_dict = { 'length' : 'The length of the object', 'width' : 'The width of the object' } 

for key, value in attrib_dict.iteritems():
    print strtemp.format(key, value)

