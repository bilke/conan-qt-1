#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bincrafters import build_template_default
import copy

if __name__ == "__main__":

    builder = build_template_default.get_builder()
    
    # Enable xmlpatterns and opengl
    filtered_builds = []
    for settings, options, env_vars, build_requires, reference in builder.items:
      new_options = copy.copy(options)
      new_options["qt:xmlpatterns"] = True
      new_options["qt:opengl"] = "dynamic"
      filtered_builds.append([settings, new_options, env_vars, build_requires])
    builder.builds = filtered_builds
    
    builder.run()
