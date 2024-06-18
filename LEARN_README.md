# 学习记录

本地部署 Swanlab，而不是用登录的方式。

## 难点

1. DataSet 处理

   我直接从 modelscope 上下载数据集，但是这里使用的是作者处理过的数据集，并且需要在百度网盘上下载，不是很适合 ssh 操作。

   从 modelscope 下载数据集后，需要改写继承 DataSet 的 DatasetLoader 类，处理图片内容和 label。

2. 修改为本地部署

   根据文档中的[离线实验跟踪](https://github.com/SwanHubX/SwanLab/blob/main/README_cn.md#%E7%A6%BB%E7%BA%BF%E5%AE%9E%E9%AA%8C%E8%B7%9F%E8%B8%AA), 修改了 swanlab.init 函数参数内容，使其不需要登录。
