# HelloWorld.spec
# -*- mode: python -*-
import sys
from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

hiddenimports = [
    'PySide6.QtCore',
    'PySide6.QtGui',
    'PySide6.QtQml',
    'PySide6.QtQuick',
]

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[('main.qml', '.')],
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['numpy', 'PIL', 'pandas', 'matplotlib', 'scipy'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(a.pure,
          a.zipped_data,
          cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='HelloWorld',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=True,
    console=False,
    target_arch='universal2',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='HelloWorld'
)

if sys.platform == 'darwin':
    app = BUNDLE(
        coll,
        name='HelloWorld.app',
        icon=None,
        bundle_identifier='com.example.helloworld',
        version='1.0.0',
        info_plist={
            'NSHighResolutionCapable': 'True',
            'NSRequiresAquaSystemAppearance': 'No',
            'LSMinimumSystemVersion': '10.13.0',
            'CFBundleDisplayName': 'HelloWorld',
            'CFBundleIdentifier': 'com.example.helloworld',
            'CFBundleVersion': '1.0.0',
            'CFBundleShortVersionString': '1.0.0',
            'NSPrincipalClass': 'NSApplication',
            'LSApplicationCategoryType': 'public.app-category.utilities',
        }
    )