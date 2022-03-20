python_requirement(
    name = "structlog",
    requirements = ["structlog==21.5.0"],
)

python_requirement(
    name = "setuptools",
    requirements = ["setuptools==57.5.0"],
)

python_requirement(
    name = "simple-parsing",
    requirements = ["simple-parsing==0.0.17"],
)

python_requirement(
    name = "colorama",
    requirements = ["colorama==0.4.4"],
)

# Technical targets that include tools - usually not deployed to VM but used locally for
# development. See `export-dev-env.sh` script.
pants_requirements(name = "pants")

mypy_requirement(name = "mypy")

python_requirement(
    name = "ipython",
    requirements = ["ipython==8.0.1"],
)

python_requirement(
    name = "jupyterlab",
    requirements = [
        "jupyterlab==3.2.9",
        "jupyterlab-code-formatter==1.4.10",
    ],
)

python_requirement(
    name = "black",
    requirements = ["black==22.1.0"],
)

python_requirement(
    name = "isort",
    requirements = ["isort==5.10.1"],
)

python_distribution(
    name = "devtools",
    dependencies = [
        "//:mypy",
        "//:pants",
        "//:ipython",
        "//:jupyterlab",
        "//:black",
        "//:isort",
        "//:setuptools",
    ],
    provides = python_artifact(
        name = "dev",
        version = "0.0.0",
    ),
    sdist = False,
)
