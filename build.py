#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bincrafters import build_template_default
import copy
import os
import platform

if __name__ == "__main__":
    os.environ['CONAN_REMOTES'] = 'https://api.bintray.com/conan/bincrafters/public-conan'
    builder = build_template_default.get_builder()
    
    filtered_builds = []
    for settings, options, env_vars, build_requires, reference in builder.items:

      # Build shared only
      if not options["Qt:shared"]:
        continue

      new_options = copy.copy(options)
      new_options["qt:opengl"] = "dynamic"
      new_options["qt:qtxmlpatterns"] = True

      if platform.system() == "Linux":
        new_options["qt:qtx11extras"] = True

      filtered_builds.append([settings, new_options, env_vars, build_requires])
    builder.builds = filtered_builds
    
    builder.run()
