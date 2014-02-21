import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'pyramid_beaker',
    'zope.sqlalchemy',
    'waitress',
    'webhelpers',
    # currently needs to be installed via pip -> 'numpy', 
    'shapely',
    'geojson',
    'gdal',
    'scipy',
    'decorator'
    ]

setup(name='np',
      version='1.0',
      description='Electricity infrastructure prototyping system',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Roy Hyunjin Han',
      author_email='',
      url='http://networkplanner.modilabs.org',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='np',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = np:main
      [console_scripts]
      initialize_np_db = np.scripts.initializedb:main
      """,
      )
