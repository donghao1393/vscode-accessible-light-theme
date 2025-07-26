#!/usr/bin/env python3
"""
快速对比度检查脚本
用于验证特定颜色组合的对比度
"""

import sys


def hex_to_rgb(hex_color):
    """将十六进制颜色转换为RGB"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_luminance(r, g, b):
    """计算RGB颜色的相对亮度"""
    def srgb_to_linear(c):
        c = c / 255.0
        if c <= 0.03928:
            return c / 12.92
        else:
            return pow((c + 0.055) / 1.055, 2.4)
    
    r_lin = srgb_to_linear(r)
    g_lin = srgb_to_linear(g)
    b_lin = srgb_to_linear(b)
    
    return 0.2126 * r_lin + 0.7152 * g_lin + 0.0722 * b_lin


def contrast_ratio(color1, color2):
    """计算两个颜色之间的对比度"""
    rgb1 = hex_to_rgb(color1)
    rgb2 = hex_to_rgb(color2)
    
    lum1 = rgb_to_luminance(*rgb1)
    lum2 = rgb_to_luminance(*rgb2)
    
    lighter = max(lum1, lum2)
    darker = min(lum1, lum2)
    
    return (lighter + 0.05) / (darker + 0.05)


def check_color_pair(color1, color2, description=""):
    """检查一对颜色的对比度"""
    ratio = contrast_ratio(color1, color2)
    
    aa_normal = '✓' if ratio >= 4.5 else '✗'
    aa_large = '✓' if ratio >= 3.0 else '✗'
    aaa_normal = '✓' if ratio >= 7.0 else '✗'
    
    print(f"{description:<25} | {color1} vs {color2}")
    print(f"  对比度: {ratio:.2f}:1")
    print(f"  WCAG AA 普通文本: {aa_normal} | AA 大文本: {aa_large} | AAA 普通文本: {aaa_normal}")
    print()
    
    return ratio >= 4.5


def main():
    """主函数"""
    if len(sys.argv) == 3:
        # 命令行模式：检查两个颜色
        color1, color2 = sys.argv[1], sys.argv[2]
        check_color_pair(color1, color2, "自定义颜色对")
    else:
        # 默认模式：检查主题的主要颜色
        print("=== 无障碍主题颜色对比度检查 ===\n")
        
        background = '#fdfdfd'
        
        # 当前主题的主要颜色
        colors = [
            ('#1a1a1a', '主文本'),
            ('#dc2626', '关键字(红色)'),
            ('#047857', '字符串(绿色)'),
            ('#c2410c', '数字/类型(橙色)'),
            ('#2563eb', '函数(蓝色)'),
            ('#6b7280', '注释(灰色)'),
            ('#1f2937', '操作符(深灰)')
        ]
        
        all_passed = True
        for color, description in colors:
            passed = check_color_pair(color, background, description)
            if not passed:
                all_passed = False
        
        if all_passed:
            print("🎉 所有颜色都符合WCAG AA标准！")
        else:
            print("⚠️  部分颜色不符合WCAG AA标准，需要调整")


if __name__ == '__main__':
    main()
