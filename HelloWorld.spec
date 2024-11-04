# HelloWorld.spec
# -*- mode: python -*-
block_cipher = None

# Define which Qt modules we actually need
hiddenimports = [
    'PySide6.QtCore',
    'PySide6.QtGui',
    'PySide6.QtQml',
    'PySide6.QtQuick'
]

# Define excludes to remove unnecessary modules
excludes = [
    'PySide6.QtSql',
    'PySide6.QtNetwork',
    'PySide6.QtTest',
    'PySide6.QtConcurrent',
    'PySide6.QtOpenGL',
    'PySide6.QtOpenGLWidgets',
    'PySide6.QtPositioning',
    'PySide6.QtPrintSupport',
    'PySide6.QtWebChannel',
    'PySide6.QtWebEngineCore',
    'PySide6.QtWebEngineQuick',
    'PySide6.QtWebEngineWidgets',
    'PySide6.QtWebSockets',
    'PySide6.QtXml',
    'PySide6.QtBluetooth',
    'PySide6.QtMultimedia'
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
    excludes=excludes,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# Remove unnecessary Qt plugins
qt_plugins = ['platforms', 'styles']  # Keep only essential plugins
for plugin in a.binaries[:]:
    if 'Qt6' in plugin[0] and not any(p in plugin[0] for p in qt_plugins):
        a.binaries.remove(plugin)

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
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=True,
    upx=True,
    upx_exclude=[],
    name='HelloWorld',
)