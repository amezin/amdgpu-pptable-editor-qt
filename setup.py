import setuptools


setuptools.setup(
    name='amdgpu-pptable-editor-qt',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'amdgpu-pptable @ git+https://github.com/amezin/amdgpu-pptable.git',
        'PyQt5'
    ],
    setup_requires=['setuptools_scm', 'setuptools_scm_git_archive'],
    entry_points={
        'gui_scripts': ['amdgpu-pptable-editor-qt=amdgpu_pptable_qt.gui:main']
    },
    python_requires='>=3.6',
    use_scm_version={'write_to': 'src/amdgpu_pptable_qt/version.py'}
)
