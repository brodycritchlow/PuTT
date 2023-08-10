# open README to set as docstring
readme_file = open("README.md")
# set __doc__ to the text inside `readme_file`
__doc__ = readme_file.read()
# close file
readme_file.close()

