from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pyrms',
      version='1.0.0',
      description='Simulating and Analyzing Chemical Kinetic Systems',
      long_description=readme(),
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Simulation'
      ],
      url='http://github.com/ReactionMechanismGenerator/pyrms',
      keywords='chemical kinetics simulation mechanism reaction',
      author='Matthew Johnson',
      author_email='rmg_dev@mit.edu',
      license='MIT',
      packages=['pyrms','pyrms.tests'],
      install_requires=['julia>=1.0'],
      include_package_data=True,
zip_safe=False)
