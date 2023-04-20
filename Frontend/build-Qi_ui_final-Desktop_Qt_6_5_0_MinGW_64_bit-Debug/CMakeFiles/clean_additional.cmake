# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\Qi_ui_final_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\Qi_ui_final_autogen.dir\\ParseCache.txt"
  "Qi_ui_final_autogen"
  )
endif()
