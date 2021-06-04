from conans.model import Generator
from conans.model import Generator
from conans import ConanFile


class Waf(Generator):
    def _remove_lib_extension(self, libs):
        return [lib[0:-4] if lib.endswith(".lib") else lib for lib in libs]

    @property
    def filename(self):
        return "waf_conan_libs_info.py"

    @property
    def content(self):
        sections = []
        sections.append("def configure(ctx):")
        conan_libs = []

        # get deps - https://docs.conan.io/en/latest/reference/conanfile/attributes.html#deps-cpp-info
        # deps is a list of package names: ["poco", "zlib", "openssl"]
        # e.g. deps = self.deps_cpp_info.deps
        # e.g. self.deps_cpp_info["zlib"].rootpath

        # can use a template - https://docs.conan.io/en/latest/howtos/custom_generators.html

        for dep_name, info in self.deps_build_info.dependencies:
            if dep_name not in self.conanfile.build_requires:
                dep_name = dep_name.replace("-", "_")
                sections.append("   ctx.env.INCLUDES_{} = {}".format(
                    dep_name, info.include_paths))
                sections.append("   ctx.env.LIBPATH_{} = {}".format(
                    dep_name, info.lib_paths))
                sections.append("   ctx.env.LIB_{} = {}".format(
                    dep_name, self._remove_lib_extension(info.libs)))
                conan_libs.append(dep_name)
        sections.append("   ctx.env.CONAN_LIBS = {}".format(conan_libs))
        sections.append("")
        return "\n".join(sections)


class WafGeneratorPackage(ConanFile):
    name = "WafGen"
    version = "0.1"
    license = "MIT"


