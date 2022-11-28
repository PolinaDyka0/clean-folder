from setuptools import setup

setup(name='clean-folder',
      version='1',
      description='Sorting files and folders',
      url='https: // github.com/PolinaDyka0/clean-folder',
      author='Polina Dyka',
      author_email='polinadyka@gmail.com',
      license='MIT',
      packages=['clean_folder'],
      entry_points={'console_scripts': ['clean-folder = clean_folder.sort:main']})
