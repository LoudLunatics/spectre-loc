from setuptools import setup, find_packages

setup(
    name='spectre-loc',
    version='1.0.1', # Kita naikkan versinya karena ini perbaikan
    packages=find_packages(), # 🚨 INI SANGAT WAJIB ADA
    install_requires=[
        'shodan==1.31.0',
        'python-dotenv==1.0.1',
        'rich==13.7.1'
    ],
    entry_points={
        'console_scripts': [
            'spectre-loc=spectre.cli:main',
        ],
    },
)
