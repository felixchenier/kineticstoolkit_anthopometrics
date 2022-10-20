"""Setup tool for building a pip-accessible package."""

import setuptools

name = "kineticstoolkit_anthropometrics"
description = "Provide tools associated to anthropometric measurements and estimates"
url = "https://github.com/felixchenier/kineticstoolkit_anthropometrics"
author = "Félix Chénier"
author_email = "chenier.felix@uqam.ca"
#--------------------------------------------------------------------------------
# It may be advised to avoid modifying the rest of this file.
#--------------------------------------------------------------------------------


with open("README.md", "r") as fh:
    long_description = fh.readline()

setuptools.setup(
    name=name,
    description=(description),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    author=author,
    author_email=author_email,
    license='Apache',
        license_files=['LICENSE.txt'],
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=setuptools.find_packages(),
    install_requires=['kineticstoolkit'],
    package_data={
        "kineticstoolkit_anthropometrics": ["anthropometrics_dumas_2007.csv"],
    },    python_requires='>=3.8',
)
