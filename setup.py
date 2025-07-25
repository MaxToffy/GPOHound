from setuptools import setup

setup(
    name="gpohound",
    version="1.0.0",
    description="GPO dumper and analyser",
    author="Maxime AWOUKOU",
    maintainer="Maxime AWOUKOU",
    python_requires=">=3.10",
    packages=[
        "config",
        "config.analysis",
        "config.gpo_files_structure.csv",
        "config.gpo_files_structure.inf",
        "config.gpo_files_structure.ini",
        "config.gpo_files_structure.pol",
        "config.gpo_files_structure.xml",
        "config.gpo_files_structure.aas",
        "gpohound",
        "gpohound.utils",
        "gpohound.parsers",
        "gpohound.processors",
        "gpohound.analysers",
    ],
    package_dir={"config": "config/"},
    package_data={
        "config": ["*.yaml"],
        "config.analysis": ["*.yaml"],
        "config.gpo_files_structure.csv": ["*.yaml"],
        "config.gpo_files_structure.inf": ["*.yaml"],
        "config.gpo_files_structure.ini": ["*.yaml"],
        "config.gpo_files_structure.pol": ["*.yaml"],
        "config.gpo_files_structure.xml": ["*.yaml"],
        "config.gpo_files_structure.aas": ["*.yaml"],
    },
    install_requires=[
        "pyyaml>=6.0.2",
        "neo4j>=5.28.1",
        "rich>=14.0.0",
        "pycryptodome>=3.22.0",
        "platformdirs>=4.3.7",
    ],
    entry_points={"console_scripts": ["gpohound=gpohound:main"]},
)
