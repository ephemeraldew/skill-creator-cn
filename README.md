# Skill Creator (中文版)

Skill Creator 的中文版本，包含完整的中文技能创建指南和工具脚本。

## 项目简介

本项目是 Skill Creator 的中文版本，提供：

- 📚 **中文技能创建指南** (`SKILL.md`) - 完整的中文技能创建指南和最佳实践
- 🛠️ **工具脚本** - 技能初始化、验证和打包工具（所有提示信息均为中文）

如果你熟悉 Skill Creator 的英文版本，可以直接使用本项目的工具和指南来创建中文技能。

## 项目结构

```
skill-creator-cn/
├── SKILL.md              # 中文技能创建指南
├── scripts/              # 工具脚本
│   ├── init_skill.py     # 初始化新技能
│   ├── package_skill.py  # 打包技能为 zip
│   └── quick_validate.py # 验证技能结构
└── README.md
```

## 工具说明

### init_skill.py

初始化新技能，自动生成模板和目录结构。

```bash
python scripts/init_skill.py <技能名称> --path <路径>
```

**技能名称要求：** 连字符格式（小写字母、数字和连字符），例如 `my-new-skill`

### quick_validate.py

验证技能的基本结构和格式要求。

```bash
python scripts/quick_validate.py <技能目录>
```

### package_skill.py

将技能文件夹打包成可分发的 zip 文件（打包前会自动验证）。

```bash
python scripts/package_skill.py <技能文件夹路径> [输出目录]
```

## 详细指南

完整的技能创建流程和最佳实践请参考 `SKILL.md` 文件。

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

本项目采用开源许可证。完整条款见 LICENSE.txt（如果存在）。
