"""Setup for katas."""


from setuptools import setup

setup(
    name="code-katas",
    description="code-katas solutions.",
    version=0.1,
    author="Zach Taylor",
    author_email="zacharymtaylor3@gmail.com",
    license='MIT',
    py_modules=['sum_two_lowest_in_array'],
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-cov']}
)
