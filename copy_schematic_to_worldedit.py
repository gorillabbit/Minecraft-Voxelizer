import shutil

# スキーマティックファイルのパス
schematic_file_path = 'output/schematic_file.schematic'

# WorldEditのスキーマティックディレクトリのパス
worldedit_schematics_directory = 'path/to/your/.minecraft/schematics/'

# スキーマティックファイルをコピー
shutil.copy(schematic_file_path, worldedit_schematics_directory)
