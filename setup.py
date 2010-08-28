from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='decobrewery.xdvtheme',
      version=version,
      description="The Deco Brewery XDV Theme",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Rob Gietema',
      author_email='rob@fourdigits.nl',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['decobrewery'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.xdv',
          'plonetheme.wireframe',
      ],
      entry_points="""
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
