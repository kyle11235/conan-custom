import os
import shutil
from conans import ConanFile, tools
from waf_environment import WafBuildEnvironment


class PythonRequires(ConanFile):
    name = "waf-build-helper"
    version = "0.1"

    # export a local source
    exports = "waf_environment.py"
