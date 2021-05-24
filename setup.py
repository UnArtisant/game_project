from cx_Freeze import setup, Executable
base = None
executables = [Executable("main.py", base=base)]
packages = ["idna","pygame.py"]
options = {
    'build_exe': {
        'packages':packages,
    },
}
setup(
    name = "DripFighters",
    options = options,
    version = "1.0",
    description = 'Voici mon programme',
    executables = executables
)