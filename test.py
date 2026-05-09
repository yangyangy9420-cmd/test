import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.io import loadmat
from pathlib import Path
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

print("开始测试 Python 库是否可用...\n")

# 1. 测试 numpy
a = np.array([1, 2, 3, 4, 5])
print("numpy 正常，数组内容：", a)

# 2. 测试 pandas
df = pd.DataFrame({
    "编号": [1, 2, 3],
    "数值": [10.5, 20.3, 30.1]
})
print("\npandas 正常，DataFrame 内容：")
print(df)

# 3. 测试 pathlib
p = Path(".")
print("\npathlib 正常，当前目录：", p.resolve())

# 4. 测试 seaborn
sns.set_theme()
print("\nseaborn 正常，已设置主题")

# 5. 测试 matplotlib
plt.figure(figsize=(6, 4))
plt.plot([1, 2, 3], [2, 4, 6], marker='o')
plt.title("Matplotlib Test")
plt.xlabel("X")
plt.ylabel("Y")
plt.tight_layout()
plt.show()
print("matplotlib 正常，图像已显示")

# 6. 测试 scipy.io.loadmat
print("\nscipy 正常，loadmat 已成功导入（未实际读取 mat 文件）")

print("\n所有测试完成，没有报错说明这些库基本可用。")