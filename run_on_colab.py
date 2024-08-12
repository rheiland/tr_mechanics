# library
import os
import shutil
import stat
import sys
import importlib

# function
def go(s_home):
    # set variables
    s_bin = f'{s_home}/tr_mechanics/bin'
    s_src = f'{s_home}/tr_mechanics/bin/myproj_colab'
    s_exe = f'{s_home}/tr_mechanics/bin/myproj'
    s_wd = f'{s_home}/tr_mechanics'

    # going home
    os.chdir(s_home)

    # install binary
    if not os.path.exists(s_exe):
        shutil.copy(src=s_src, dst=s_exe)
        os.chmod(s_exe, stat.S_IXOTH)
        sys.path.insert(0, s_bin)

    # relaod module binary and fire up gui
    os.chdir(s_wd)
    if 'tr_mechanics' in set(sys.modules.keys()):
        importlib.reload(tr_mechanics)
    else:
        import tr_mechanics
    tr_mechanics.gui
