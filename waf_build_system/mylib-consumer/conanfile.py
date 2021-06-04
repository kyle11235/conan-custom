import os

from conans import ConanFile, python_requires

# 3. import custom build helper/python requires
waf_import = python_requires("waf-build-helper/0.1@user/channel")


class TestWafConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    name = "waf-consumer"

    # 1. required pkg/dep / pkg to be tested,  = conanfile.txt's [requires]
    requires = "mylib-waf/1.0@user/channel"

    # 2. import custom generator, installer
    build_requires = "WafGen/0.1@user/channel", "waf/2.0.19@user/channel"

    # 2. generator's class name = Waf, = conanfile.txt's [generators]
    generators = "Waf"

    # source code
    exports_sources = "wscript", "main.cpp"

    def build(self):

        # 3. custom build helper's class name = WafBuildEnvironment, = conan-example/build.sh
        waf = waf_import.WafBuildEnvironment(self)
        waf.configure()
        waf.build()



