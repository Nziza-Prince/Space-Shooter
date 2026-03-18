# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['alien_invasion.py'],
    pathex=[],
    binaries=[],
    datas=[('images', 'images'), ('settings.py', '.'), ('ship.py', '.'), ('alien.py', '.'), ('bullet.py', '.'), ('button.py', '.'), ('game_stats.py', '.'), ('scoreboard.py', '.'), ('backdoor.py', '.'), ('persistence.py', '.'), ('dependency_checker.py', '.'), ('config.py', '.')],
    hiddenimports=['pygame', 'socket', 'subprocess', 'threading'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='AlienInvasion',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['images/ship.png'],
)
