from distutils.core import setup


def readme():
    """Import the README.md Markdown file and try to convert it to RST format."""
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except(IOError, ImportError):
        with open('README.md') as readme_file:
            return readme_file.read()


setup(
    name='production',
    version='0.1',
    description='Analysis of the Evolution of Music',
    long_description=readme(),
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    url='https://github.com/<vivvvli>/evolution-of-music',
    author='Vivian Li', 
    author_email='vivian.li982@gmail.com',  
    license='MIT',
    packages=['production'],
)
