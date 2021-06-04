
# conan custom build system demo

- prepare env

        install conan, best to finish my example http://github.com.npmjs.org/kyle11235/conan-example

- waf

        - guide
                
                https://blog.conan.io/2019/07/24/C++-build-systems-new-integrations-in-Conan-package-manager.html
                
        - source code

                https://github.com/conan-io/examples/tree/master/features/integrate_build_system

        - build helper
        
                the build helper is responsible for translating Conan settings to something that the build tool understands

                - define build helper, conan settings -> waf settings in generate waf_conan_toolchain.py
                
                        waf_environment.py
                                -> init -> conan settings
                                -> configure -> _save_toolchain_file -> waf_conan_toolchain.py (waf settings) -> waf configure ...
                                -> build -> waf build ...

                - export build helper
                
                        conan create waf-build-helper user/channel (pointing to folder ./waf-build-helper)

                - python_requires build helper
                
                        waf-mylib/wscript -> waf_conan_toolchain.py
                        waf-mylib/conanfile.py -> build
                                waf = self.python_requires["waf-build-helper"].module.WafBuildEnvironment(self)
                                waf.configure()
                                waf.build()

                - use build helper

                        conan create waf-mylib user/channel -s compiler.cppstd=14

- premake

        - guide

                https://docs.conan.io/en/latest/howtos/custom_generators.html

                