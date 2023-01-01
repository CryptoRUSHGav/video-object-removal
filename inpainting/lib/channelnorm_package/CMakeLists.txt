
cmake_minimum_required(VERSION 3.8 FATAL_ERROR)
project(channelnorm_package LANGUAGES CXX CUDA)
set(CMAKE_PREFIX_PATH "<path_to_libtorch>")
find_package(Torch REQUIRED)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS}")

add_library(ChannelNorm_kernel
  src/ChannelNorm_cuda.c
  src/ChannelNorm_cuda.h
  src/ChannelNorm_kernel.cu
  src/ChannelNorm_kernel.h
  )

target_link_libraries(ChannelNorm_kernel "${TORCH_LIBRARIES}")

set_property(TARGET ChannelNorm_kernel PROPERTY CXX_STANDARD 14)

# Request that particles be built with -std=c++11
# As this is a public compile feature anything that links to particles
# will also build with -std=c++11
# target_compile_features(ChannelNorm_kernel PUBLIC cxx_std_11)

# We need to explicitly state that we need all CUDA files in the particle
# library to be built with -dc as the member functions could be called by
# other libraries and executables
set_target_properties( ChannelNorm_kernel
                       PROPERTIES CUDA_SEPARABLE_COMPILATION ON
                       OUTPUT_NAME "ChannelNorm_kernel.o"
                      )



