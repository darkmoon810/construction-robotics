from setuptools import setup, find_packages

setup(
    name='robotics-dashboard',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A dashboard for construction robotics',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/robotics-dashboard',
    packages=find_packages(where='app'),
    package_dir={'': 'app'},
    install_requires=[
        # List your project dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)