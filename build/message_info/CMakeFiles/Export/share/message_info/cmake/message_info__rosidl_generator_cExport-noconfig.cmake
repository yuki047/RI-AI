#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "message_info::message_info__rosidl_generator_c" for configuration ""
set_property(TARGET message_info::message_info__rosidl_generator_c APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(message_info::message_info__rosidl_generator_c PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libmessage_info__rosidl_generator_c.dylib"
  IMPORTED_SONAME_NOCONFIG "@rpath/libmessage_info__rosidl_generator_c.dylib"
  )

list(APPEND _IMPORT_CHECK_TARGETS message_info::message_info__rosidl_generator_c )
list(APPEND _IMPORT_CHECK_FILES_FOR_message_info::message_info__rosidl_generator_c "${_IMPORT_PREFIX}/lib/libmessage_info__rosidl_generator_c.dylib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
