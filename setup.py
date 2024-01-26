from setuptools import setup, find_packages

setup(
    name='Your-Project-Name',
    version='0.1',
    packages=find_packages(),
    url='http://github.com/buYoung/Your-Project-Name',
    license='MIT',
    author='buYoung',
    author_email='your-email@example.com',
    description='Short description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        # List your project dependencies here
        # For example:
        # 'numpy>=1.13.3',
        # 'toml>=0.10.2',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)