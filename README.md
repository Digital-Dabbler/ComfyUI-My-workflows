# ComfyUI My_workflows 节点

这是一个用于ComfyUI的自定义节点，可以帮助你管理和存储工作流的描述信息。通过这个节点，你可以为每个工作流添加详细的描述文档，便于后续查看和管理。

## 功能特点

- 为工作流添加描述信息
- 支持多行文本输入
- 自动保存为独立的元数据文件
- 使用UTF-8编码支持中文

## 安装方法

1. 进入ComfyUI的custom_nodes目录
2. 克隆本仓库：
```bash
git clone https://github.com/Digital-Dabbler/ComfyUI-My-workflows
```
3. 重启ComfyUI

## 使用方法

1. 在ComfyUI界面中找到"My_workflows"节点
2. 输入工作流文件名
3. 在描述框中输入工作流的详细说明
4. 运行节点，描述信息将被保存

## 配置说明

- 工作流文件存储在`example_workflows`目录下
- 描述信息以`.meta.json`格式保存
- 支持UTF-8编码，可以使用中文描述

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request来帮助改进这个项目！