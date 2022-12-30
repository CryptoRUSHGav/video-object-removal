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
    Headers += ['src/ChannelNorm_cuda.h']
    Sources += ['src/ChannelNorm_cuda.c']
    Defines += [('WITH_CUDA', None)]
    Objects += ['src/ChannelNorm_kernel.o']

if __name__ == '__main__':
    setup(name='_ext.channelnorm', ext_modules=[
        CUDAExtension(
            name='_ext.channelnorm',
            headers=Headers,
            sources=Sources,
            extra_objects=Objects
        )],
        cmdclass={'build_ext': BuildExtension})

# ffi = torch.utils.cpp_extension.CppExtension(
#     name='_ext.channelnorm',
#     headers=Headers,
#     sources=Sources,
#     verbose=False,
#     with_cuda=True,
#     package=False,
#     relative_to=this_folder,
#     define_macros=Defines,
#     extra_objects=[os.path.join(this_folder, Object) for Object in Objects]
# )

# if __name__ == '__main__':
#     ffi.build()