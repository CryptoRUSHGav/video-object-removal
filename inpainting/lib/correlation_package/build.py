import os
import torch
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

this_folder = os.path.dirname(os.path.abspath(__file__)) + '/'

Headers = []
Sources = []
Defines = []
Objects = []

if torch.cuda.is_available() == True:
    Headers += ['src/correlation_cuda.h']
    Sources += ['src/correlation_cuda.c']
    Defines += [('WITH_CUDA', None)]
    Objects += ['src/correlation_cuda_kernel.o']

# ffi = torch.utils.cpp_extension.CppExtension(
#     name='_ext.correlation',
#     headers=Headers,
#     sources=Sources,
#     verbose=False,
#     with_cuda=True,
#     package=False,
#     relative_to=this_folder,
#     define_macros=Defines,
#     extra_objects=[os.path.join(this_folder, Object) for Object in Objects]
# )

if __name__ == '__main__':
    # ffi.build()
    setup(name='_ext.correlation', ext_modules=[
        CUDAExtension(
            name='_ext.correlation',
            headers=Headers,
            sources=Sources,
            extra_objects=Objects
        )],
        cmdclass={'build_ext': BuildExtension})