import pyvox

# 3Dモデルファイルのパス
model_path = 'path/to/your/3dmodel.obj'

# ボクセル化の設定
resolution = 128
model = pyvox.models.Model.from_obj(model_path, resolution)

# ボクセル化されたモデルを保存
model.write('output/voxelized_model.vox')