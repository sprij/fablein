
from setuptools import setup, find_packages

setup(
    name='fablein',
    version='0.0.1',
    author='sprij',
    author_email='s.rijo@yahoo.com',
    description='Fabric tasks.',
    keywords="lein build automation",
    url='https://github.com/sprij/fablein',
    packages=find_packages(),
    include_package_data=True,
    long_description=__doc__,
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Topic :: Utilities",
        'Programming Language :: Python',
    ]
)
