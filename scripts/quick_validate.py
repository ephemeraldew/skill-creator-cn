#!/usr/bin/env python3
"""
技能快速验证脚本 - 简化版本
"""

import sys
import os
import re
from pathlib import Path

def validate_skill(skill_path):
    """技能的基本验证"""
    skill_path = Path(skill_path)

    # 检查 SKILL.md 是否存在
    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        return False, "未找到 SKILL.md"

    # 读取并验证前置元数据
    content = skill_md.read_text()
    if not content.startswith('---'):
        return False, "未找到 YAML 前置元数据"

    # 提取前置元数据
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return False, "前置元数据格式无效"

    frontmatter = match.group(1)

    # 检查必需字段
    if 'name:' not in frontmatter:
        return False, "前置元数据中缺少 'name'"
    if 'description:' not in frontmatter:
        return False, "前置元数据中缺少 'description'"

    # 提取名称进行验证
    name_match = re.search(r'name:\s*(.+)', frontmatter)
    if name_match:
        name = name_match.group(1).strip()
        # 检查命名约定（连字符格式：小写字母加连字符）
        if not re.match(r'^[a-z0-9-]+$', name):
            return False, f"名称 '{name}' 应为连字符格式（仅限小写字母、数字和连字符）"
        if name.startswith('-') or name.endswith('-') or '--' in name:
            return False, f"名称 '{name}' 不能以连字符开头/结尾或包含连续连字符"

    # 提取并验证描述
    desc_match = re.search(r'description:\s*(.+)', frontmatter)
    if desc_match:
        description = desc_match.group(1).strip()
        # 检查尖括号
        if '<' in description or '>' in description:
            return False, "描述不能包含尖括号（< 或 >）"

    return True, "技能验证通过！"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法：python quick_validate.py <技能目录>")
        sys.exit(1)

    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)
