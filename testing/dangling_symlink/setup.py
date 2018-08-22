from setuptools import Extension
from setuptools import setup


setup(
    name='fake',
    ext_modules=[Extension('fake', ['fake.go'])],
    build_golang={'root': 'github.com/asottile/fake'},
    # Would do this, but we're testing *our* implementation and this would
    # install from pypi.  We can rely on setuptools-golang being already
    # installed under test.
    # setup_requires=['setuptools-golang'],
)
