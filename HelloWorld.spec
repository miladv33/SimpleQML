# HelloWorld.spec
# -*- mode: python -*-
block_cipher = None

# Only include the absolute minimum required Qt modules
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
    excludes=['numpy', 'PIL', 'pandas', 'matplotlib', 'scipy'],
    runtime_hooks=[],
)

# Keep only the essential Qt plugins
binaries = []
for binary in a.binaries:
    if not any(exclude in binary[0] for exclude in [
        'Qt6Network', 'Qt6Svg', 'Qt6DBus', 'Qt6VirtualKeyboard',
        'Qt6Widgets', 'Qt6Sql', 'Qt6Test', 'Qt6WebEngine'
    ]):
        binaries.append(binary)
a.binaries = binaries

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='HelloWorld',
    debug=False,
    strip=True,
    upx=True,
    console=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=True,
    upx=True,
    name='HelloWorld',
)