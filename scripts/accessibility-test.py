#!/usr/bin/env python3
"""
VS Code主题无障碍性测试脚本
检查颜色对比度是否符合WCAG标准
"""

import json
import math
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """将十六进制颜色转换为RGB"""
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 3:
        hex_color = ''.join([c*2 for c in hex_color])
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_luminance(r: int, g: int, b: int) -> float:
    """计算RGB颜色的相对亮度"""
    def srgb_to_linear(c: int) -> float:
        c = c / 255.0
        if c <= 0.03928:
            return c / 12.92
        else:
            return pow((c + 0.055) / 1.055, 2.4)
    
    r_lin = srgb_to_linear(r)
    g_lin = srgb_to_linear(g)
    b_lin = srgb_to_linear(b)
    
    return 0.2126 * r_lin + 0.7152 * g_lin + 0.0722 * b_lin


def contrast_ratio(color1: str, color2: str) -> float:
    """计算两个颜色之间的对比度"""
    try:
        rgb1 = hex_to_rgb(color1)
        rgb2 = hex_to_rgb(color2)
        
        lum1 = rgb_to_luminance(*rgb1)
        lum2 = rgb_to_luminance(*rgb2)
        
        lighter = max(lum1, lum2)
        darker = min(lum1, lum2)
        
        return (lighter + 0.05) / (darker + 0.05)
    except (ValueError, TypeError):
        return 0.0


def extract_colors_from_theme(theme_path: str) -> Dict[str, str]:
    """从主题文件中提取颜色"""
    with open(theme_path, 'r', encoding='utf-8') as f:
        theme_data = json.load(f)
    
    colors = {}
    
    # 提取UI颜色
    if 'colors' in theme_data:
        for key, value in theme_data['colors'].items():
            if isinstance(value, str) and value.startswith('#'):
                colors[f"ui.{key}"] = value
    
    # 提取token颜色
    if 'tokenColors' in theme_data:
        for token in theme_data['tokenColors']:
            if 'settings' in token and 'foreground' in token['settings']:
                scope = token.get('scope', ['unknown'])
                if isinstance(scope, list):
                    scope_name = ', '.join(scope[:2])  # 只取前两个scope
                else:
                    scope_name = scope
                
                foreground = token['settings']['foreground']
                if isinstance(foreground, str) and foreground.startswith('#'):
                    colors[f"token.{scope_name}"] = foreground
    
    return colors


def check_accessibility(theme_path: str) -> Dict:
    """检查主题的无障碍性"""
    colors = extract_colors_from_theme(theme_path)
    
    # 主要背景色
    background = colors.get('ui.editor.background', '#ffffff')
    
    # 需要检查的重要颜色组合
    important_checks = [
        ('ui.editor.foreground', '主文本'),
        ('token.string', '字符串'),
        ('token.constant.numeric', '数字'),
        ('token.comment', '注释'),
        ('token.keyword', '关键字'),
        ('token.entity.name.function', '函数名'),
        ('ui.errorForeground', '错误信息'),
        ('ui.warningForeground', '警告信息'),
    ]
    
    results = {
        'theme_path': theme_path,
        'background_color': background,
        'checks': [],
        'summary': {
            'total': 0,
            'passed_aa': 0,
            'passed_aaa': 0,
            'failed': 0
        }
    }
    
    for color_key, description in important_checks:
        if color_key in colors:
            foreground = colors[color_key]
            ratio = contrast_ratio(foreground, background)
            
            # WCAG标准检查
            aa_normal = ratio >= 4.5
            aa_large = ratio >= 3.0
            aaa_normal = ratio >= 7.0
            aaa_large = ratio >= 4.5
            
            check_result = {
                'description': description,
                'foreground': foreground,
                'background': background,
                'ratio': round(ratio, 2),
                'wcag_aa_normal': aa_normal,
                'wcag_aa_large': aa_large,
                'wcag_aaa_normal': aaa_normal,
                'wcag_aaa_large': aaa_large,
                'status': 'PASS' if aa_normal else 'FAIL'
            }
            
            results['checks'].append(check_result)
            results['summary']['total'] += 1
            
            if aa_normal:
                results['summary']['passed_aa'] += 1
            if aaa_normal:
                results['summary']['passed_aaa'] += 1
            if not aa_normal:
                results['summary']['failed'] += 1
    
    return results


def print_results(results: Dict):
    """打印测试结果"""
    print(f"\n{'='*60}")
    print(f"无障碍性测试报告")
    print(f"{'='*60}")
    print(f"主题文件: {results['theme_path']}")
    print(f"背景色: {results['background_color']}")
    print(f"\n{'检查项目':<20} {'前景色':<10} {'对比度':<10} {'AA标准':<8} {'AAA标准':<8}")
    print(f"{'-'*60}")
    
    for check in results['checks']:
        status_aa = '✓' if check['wcag_aa_normal'] else '✗'
        status_aaa = '✓' if check['wcag_aaa_normal'] else '✗'
        
        print(f"{check['description']:<20} {check['foreground']:<10} "
              f"{check['ratio']:<10.2f} {status_aa:<8} {status_aaa:<8}")
    
    print(f"\n{'='*60}")
    print(f"总结:")
    print(f"  总检查项: {results['summary']['total']}")
    print(f"  通过AA标准: {results['summary']['passed_aa']}")
    print(f"  通过AAA标准: {results['summary']['passed_aaa']}")
    print(f"  未通过: {results['summary']['failed']}")
    
    if results['summary']['failed'] == 0:
        print(f"\n🎉 所有颜色都符合WCAG AA标准！")
    else:
        print(f"\n⚠️  有 {results['summary']['failed']} 个颜色不符合WCAG AA标准")


def main():
    """主函数"""
    theme_path = Path(__file__).parent.parent / 'themes' / 'accessible-light-theme.json'
    
    if not theme_path.exists():
        print(f"错误: 找不到主题文件 {theme_path}")
        return 1
    
    try:
        results = check_accessibility(str(theme_path))
        print_results(results)
        
        # 如果有失败的检查，返回非零退出码
        return 1 if results['summary']['failed'] > 0 else 0
        
    except Exception as e:
        print(f"错误: {e}")
        return 1


if __name__ == '__main__':
    exit(main())
