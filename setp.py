import setuptools
with open("README.md","r") as f:
	long_desc=f.read()
setuptools.setup(name="navdeepPackage",
                 version="0.0.1",
                 author="Navdeep",
                 author_email="sujith133@gmail.com",
                 description="This package shows if a number is prime,odd or even",
                 long_description=long_desc,
                 long_description_content_type="tent/markdown",
                 url="https://github.com/Navdeep6/navdeepPackage",
                 packages=setuptools.find_packages(),
                 classifiers=["programing language::python::3","operating system::os independent,],
                 python_requiers='>=3.6',)
