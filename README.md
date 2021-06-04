
# conan custom build system demo

- prepare env

        install conan, best to finish my example http://github.com/kyle11235/conan-example

- waf 

        - guide
                
                https://blog.conan.io/2019/07/24/C++-build-systems-new-integrations-in-Conan-package-manager.html
                
        - source code

                https://github.com/conan-io/examples/tree/master/features/integrate_build_system (I have fix in main.cpp)

        - build helper
        
                the build helper is responsible for translating Conan settings to something that the build tool understands

                1. custom build helper, conan settings -> waf settings in generate waf_conan_toolchain.py
                
                        waf_environment.py
                                -> init -> conan settings
                                -> configure -> _save_toolchain_file -> waf_conan_toolchain.py (waf settings) -> waf configure ...
                                -> build -> waf build ...

                2. export build helper
                
                        conan create waf-build-helper user/channel (pointing to folder ./waf-build-helper)

                3. use/python_requires build helper
                
                        waf-mylib/wscript -> waf_conan_toolchain.py
                        waf-mylib/conanfile.py -> build
                                waf = self.python_requires["waf-build-helper"].module.WafBuildEnvironment(self)
                                waf.configure()
                                waf.build()

        - generator

                1. custom generator
                2. export generator
                3. use/build requires

                        - mylib-consumer/conanfile.py
                                -> build_requires = "WafGen/0.1@user/channel", "waf/2.0.19@user/channel"
                                -> generators = "Waf"
                        
                        - waf generator -> waf_conan_libs_info.py
                                -> ...
                                -> ctx.env.LIBPATH_LIB_mylib_waf = ['dir_to_mylib_libs']
                                -> ctx.env.LIB_mylib_waf = 'mylib'

                        - mylib-consumer/wscript -> conf.load('waf_conan_libs_info... -> waf_conan_libs_info.py

        - test

                ./build.sh

- premake

        - guide

                https://docs.conan.io/en/latest/howtos/custom_generators.html

- profile env

        https://docs.conan.io/en/latest/reference/conanfile/methods.html#env-info
        profile -> [env] CC -> tool installer -> package_info() -> self.env_info.CC

        access evn from conanfile.py
        e.g.
        requires = "mylib/1.6.0@conan/stable"
        self.deps_env_info["mylib"].othervar   