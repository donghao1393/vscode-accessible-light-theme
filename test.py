#!/usr/bin/env python3
"""
简单的主题测试脚本
验证所有颜色是否符合无障碍标准
"""

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

def main():
    """测试主题颜色对比度"""
    print("🎨 Accessible Light Theme - 对比度测试")
    print("=" * 50)
    
    background = '#fdfdfd'
    
    # 主要颜色测试
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
        ratio = contrast_ratio(color, background)
        passed = ratio >= 4.5
        status = '✅' if passed else '❌'
        
        print(f"{status} {description:<15}: {ratio:.2f}:1")
        
        if not passed:
            all_passed = False
    
    print("=" * 50)
    
    if all_passed:
        print("🎉 所有颜色都符合 WCAG AA 标准！")
        print("✅ 主题可以安全使用")
    else:
        print("⚠️  部分颜色不符合标准")
        print("❌ 需要调整颜色")
    
    return 0 if all_passed else 1

if __name__ == '__main__':
    exit(main())
