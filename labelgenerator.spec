# -*- mode: python -*-

block_cipher = None


a = Analysis(['labelgenerator.py'],
             pathex=['labelgenerator.py'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas += [
    ('vegetarian.png','./icons/vegetarian.png', "DATA"),
    ('vegan.png','./icons/vegan.png', "DATA"),
    ('gluten_free.png','./icons/gluten_free.png', "DATA"),
    ('nut_free.png','./icons/nut_free.png', "DATA"),
    ('dairy_free.png','./icons/dairy_free.png', "DATA"),
	
]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Label Generator',
          debug=False,
          strip=False,
          upx=True,
          console=True,
          icon='')