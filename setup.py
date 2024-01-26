from setuptools import setup, find_packages, Command
from sys import platform

import os

class CustomBuild(Command):
    description = "custom build command"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        if (platform == 'win32'):
            os.system('pyinstaller.exe -w -F main.py')
        else:
            os.system('pyinstaller -w -F main.py')

setup(
    name='d2r_yupgul_macro',
    version='0.0.2',
    packages=find_packages(),
    url='https://github.com/buYoung/d2r_yupgul_macro',
    license='MIT',
    author='buYoung',
    author_email='leebu18@gmail.com',
    description='Diablo 2 Resurrected Yupgul Macro',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'joblib==1.3.2',
        'MouseInfo==0.1.3',
        'numpy==1.26.3',
        'opencv-python==4.9.0.80',
        'pillow==10.2.0',
        'PyAutoGUI==0.9.54',
        'PyGetWindow==0.0.9',
        'PyMsgBox==1.0.9',
        'pyperclip==1.8.2',
        'PyRect==0.2.0',
        'PyScreeze==0.1.30',
        'pytweening==1.0.7',
        'pywin32==306',
        'scikit-learn==1.4.0',
        'scipy==1.11.4',
        'threadpoolctl==3.2.0',
        'toml==0.10.2',
        'pywebview~=4.4.1'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    cmdclass={
        'build': CustomBuild,
    }
)