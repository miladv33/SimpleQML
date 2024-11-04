# HelloWorld.spec
# -*- mode: python -*-
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
    excludes=['numpy', 'PIL', 'pandas', 'matplotlib', 'scipy'],
)

# Keep only essential Qt plugins
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
    bootloader_ignore_signals=False,
    strip=True,
    upx=True,
    console=False,
    target_arch='universal2',  # This builds for both Intel and Apple Silicon
)

app = BUNDLE(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='HelloWorld.app',
    icon=None,  # You can add an icon file here
    bundle_identifier='com.example.helloworld',
    info_plist={
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleVersion': '1.0.0',
        'NSHighResolutionCapable': 'True',
        'LSMinimumSystemVersion': '10.13.0',
    }
)