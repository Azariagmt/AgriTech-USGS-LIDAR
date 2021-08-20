from setuptools import setup, find_packages
import distutils.command.bdist_conda

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='usgslidar',
    version='0.0.14',
    distclass=distutils.command.bdist_conda.CondaDistribution,
    description='A basic package to fetch usgs agriculture data',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read() + '\n\n' +
    open('CHANGELOG.txt').read(),
    url='',
    author='Azaria Gebremichael',
    author_email='azariagebremichael10@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='usgs',
    packages=find_packages(),
    install_requires=['fiona','gdal','pdal','geopandas', 'pyproj']
)
