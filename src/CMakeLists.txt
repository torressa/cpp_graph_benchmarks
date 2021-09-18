set(NAME Dijkstra_bgl)
add_executable(${NAME} dijkstra_bgl.cc)
target_include_directories(
  ${NAME}
  PUBLIC ${PROJECT_SOURCE_DIR}/src/
         $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
         $<INSTALL_INTERFACE:include> ${Boost_INCLUDE_DIRS})
target_link_libraries(${NAME} ${Boost_LIBRARIES})

set(NAME Dijkstra_lemon)
add_executable(${NAME} dijkstra_lemon.cc)
target_include_directories(
  ${NAME}
  PUBLIC ${PROJECT_SOURCE_DIR}/src/
         $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
         $<INSTALL_INTERFACE:include> ${Boost_INCLUDE_DIRS})
target_link_libraries(${NAME} ${Boost_LIBRARIES} lemon)
