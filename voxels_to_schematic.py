import pymclevel

# ボクセルモデルのパス
voxel_model_path = 'output/voxelized_model.vox'

# ボクセルモデルをロード
vox_model = pyvox.models.Model.from_file(voxel_model_path)

# pymclevelのスキーマティックオブジェクトを作成
schematic = pymclevel.schematic.Schematic((vox_model.size_x, vox_model.size_y, vox_model.size_z))

# ボクセルデータをスキーマティックデータに変換
for x in range(vox_model.size_x):
    for y in range(vox_model.size_y):
        for z in range(vox_model.size_z):
            block_id = vox_model.get_voxel((x, y, z))
            if block_id != 0:
                schematic.setBlockAt(x, y, z, block_id)

# スキーマティックファイルを保存
schematic.saveToFile('output/schematic_file.schematic')