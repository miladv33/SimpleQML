# HelloWorld.spec
# -*- mode: python -*-
block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[('main.qml', '.')],
    hiddenimports=['PySide6.QtCore', 'PySide6.QtGui', 'PySide6.QtQml', 'PySide6.QtQuick'],
    excludes=['numpy', 'PIL', 'pandas', 'matplotlib', 'scipy'],
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='HelloWorld',
    debug=False,
    strip=False,
    upx=True,
    runtime_tmpdir=None,
    console=False,
    target_arch='universal2'
)

app = BUNDLE(
    exe,
    name='HelloWorld.app',
    bundle_identifier=None,
)