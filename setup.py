from setuptools import setup, find_packages

setup(
    name='fava_git_branch_ext',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'fava',
    ],
    entry_points={
        'fava.plugins': [
            'git_branch_extension = fava_git_branch_ext:GitBranchExtension',
        ],
    },
    include_package_data=True,  # Ensure non-Python files are included
    package_data={
        'fava_git_branch_ext': ['templates/*'],  # Include templates folder
    },
)
