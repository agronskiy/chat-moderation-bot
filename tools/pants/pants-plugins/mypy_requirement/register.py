"""This plugin expands a custom target `mypy_requirement(name = "mypy")`.

It expands to the version of mypy set in TOML, and its `extra_requirements`.


"""
from pants.backend.python.target_types import PythonRequirementModulesField
from pants.backend.python.target_types import PythonRequirementsField
from pants.backend.python.target_types import PythonRequirementTarget
from pants.backend.python.typecheck.mypy.subsystem import MyPy
from pants.engine.rules import collect_rules
from pants.engine.rules import rule
from pants.engine.target import COMMON_TARGET_FIELDS
from pants.engine.target import GeneratedTargets
from pants.engine.target import GenerateTargetsRequest
from pants.engine.target import Target
from pants.engine.unions import UnionRule


class MypyRequirementsTargetGenerator(Target):
    alias = "mypy_requirement"
    help = "Generate mypy requirements based on [mypy].* set of options"
    core_fields = (*COMMON_TARGET_FIELDS,)


class GenerateFromMypyRequirementsRequest(GenerateTargetsRequest):
    generate_from = MypyRequirementsTargetGenerator


@rule
async def generate_from_mypy_requirements(
    request: GenerateFromMypyRequirementsRequest, mypy: MyPy
) -> GeneratedTargets:
    generator = request.generator
    pip_requirements = []
    # First, generate mypy requirement itself from `[mypy].version`
    pip_requirements.append(mypy.version)
    # Next, generate the requirements _of_ mypy from `extra-requirements`
    pip_requirements.extend(mypy.extra_requirements)

    target = PythonRequirementTarget(
        {
            PythonRequirementsField.alias: (*pip_requirements,),
            PythonRequirementModulesField.alias: ("mypy",),
        },
        generator.address.create_generated(f"mypy"),
    )
    result = [target]

    return GeneratedTargets(generator, result)


def rules():
    return (
        *collect_rules(),
        UnionRule(GenerateTargetsRequest, GenerateFromMypyRequirementsRequest),
    )


def target_types():
    return [MypyRequirementsTargetGenerator]
