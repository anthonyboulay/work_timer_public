# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\air_w\\gitProjects\\work_timer\\src\\main\\python\\main.py'],
             pathex=['C:\\Users\\air_w\\gitProjects\\work_timer\\target\\PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['c:\\users\\air_w\\gitprojects\\work_timer\\venv\\lib\\site-packages\\fbs\\freeze\\hooks'],
             runtime_hooks=['C:\\Users\\air_w\\gitProjects\\work_timer\\target\\PyInstaller\\fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Work Timer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , version='C:\\Users\\air_w\\gitProjects\\work_timer\\target\\PyInstaller\\version_info.py', icon='C:\\Users\\air_w\\gitProjects\\work_timer\\src\\main\\icons\\Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='Work Timer')
