                                      Readme

MD file: markdown formatted text file, can be easily converted to HTML

setup.py
------------
Purpose of setup.py: 
copy python source files and resources to customer's workstation so it can run directly

example of setup.py
    from distutils.core import setup
    setup(name='foo',
          version='1.0',
          py_modules=['foo'],
          )  

create the installation file. this will create foo-1.0.tar.gz under dist folder
python setup.py sdist

user can get this gz file and unzip, then
python setup.py install

MANIFEST.in
------------------------------
tell setup.py which files will be included:
    include *.txt
    recursive-include examples *.txt *.py
    prune examples/sample?/build

setup.cfg
----------------------
tell setup.py configuration parameters
    [command]
    option=value
    ...

setuptools
---------
enhanced Python official distutils
    from setuptools import setup, find_packages
    setup(
        name = "HelloWorld",
        version = "0.1",
        packages = find_packages(),
        scripts = ['say_hello.py'],
        # Project uses reStructuredText, so ensure that the docutils get
        # installed or upgraded on the target machine
        install_requires = ['docutils>=0.3'],
        package_data = {
            # If any package contains *.txt or *.rst files, include them:
            '': ['*.txt', '*.rst'],
            # include any *.msg files found in the 'hello' package, too:
            'hello': ['*.msg'],
        },
        # metadata for upload to PyPI
        author = "Me",
        author_email = "me@example.com",
        description = "This is an Example Package",
        license = "PSF",
        keywords = "hello world example examples",
        url = "http://example.com/HelloWorld/",   # project home page, if any
        # could also include long_description, download_url, classifiers, etc.
    )

