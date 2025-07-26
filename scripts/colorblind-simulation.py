#!/usr/bin/env python3
"""
色盲模拟测试脚本
模拟不同类型色盲用户看到的颜色效果
"""

import colorsys
from typing import Tuple


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """将十六进制颜色转换为RGB"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(r: int, g: int, b: int) -> str:
    """将RGB转换为十六进制颜色"""
    return f"#{r:02x}{g:02x}{b:02x}"


def simulate_protanopia(r: int, g: int, b: int) -> Tuple[int, int, int]:
    """模拟红色盲（Protanopia）"""
    # 简化的红色盲模拟算法
    # 红色盲用户主要看不到红色，红色会被感知为绿色或黄色
    new_r = int(0.567 * r + 0.433 * g + 0.000 * b)
    new_g = int(0.558 * r + 0.442 * g + 0.000 * b)
    new_b = int(0.000 * r + 0.242 * g + 0.758 * b)
    
    return (min(255, max(0, new_r)), 
            min(255, max(0, new_g)), 
            min(255, max(0, new_b)))


def simulate_deuteranopia(r: int, g: int, b: int) -> Tuple[int, int, int]:
    """模拟绿色盲（Deuteranopia）"""
    # 绿色盲用户主要看不到绿色
    new_r = int(0.625 * r + 0.375 * g + 0.000 * b)
    new_g = int(0.700 * r + 0.300 * g + 0.000 * b)
    new_b = int(0.000 * r + 0.300 * g + 0.700 * b)
    
    return (min(255, max(0, new_r)), 
            min(255, max(0, new_g)), 
            min(255, max(0, new_b)))


def simulate_tritanopia(r: int, g: int, b: int) -> Tuple[int, int, int]:
    """模拟蓝色盲（Tritanopia）"""
    # 蓝色盲用户主要看不到蓝色
    new_r = int(0.950 * r + 0.050 * g + 0.000 * b)
    new_g = int(0.000 * r + 0.433 * g + 0.567 * b)
    new_b = int(0.000 * r + 0.475 * g + 0.525 * b)
    
    return (min(255, max(0, new_r)), 
            min(255, max(0, new_g)), 
            min(255, max(0, new_b)))


def simulate_monochromacy(r: int, g: int, b: int) -> Tuple[int, int, int]:
    """模拟全色盲（Monochromacy）"""
    # 转换为灰度
    gray = int(0.299 * r + 0.587 * g + 0.114 * b)
    return (gray, gray, gray)


def test_color_discrimination(colors: dict):
    """测试颜色在不同色盲条件下的区分度"""
    print("=== 色盲模拟测试 ===\n")
    
    simulations = [
        ("正常视觉", lambda r, g, b: (r, g, b)),
        ("红色盲 (Protanopia)", simulate_protanopia),
        ("绿色盲 (Deuteranopia)", simulate_deuteranopia),
        ("蓝色盲 (Tritanopia)", simulate_tritanopia),
        ("全色盲 (Monochromacy)", simulate_monochromacy)
    ]
    
    for sim_name, sim_func in simulations:
        print(f"\n{sim_name}:")
        print("-" * 50)
        
        for color_name, hex_color in colors.items():
            r, g, b = hex_to_rgb(hex_color)
            sim_r, sim_g, sim_b = sim_func(r, g, b)
            sim_hex = rgb_to_hex(sim_r, sim_g, sim_b)
            
            print(f"{color_name:<15}: {hex_color} → {sim_hex}")


def analyze_theme_accessibility():
    """分析主题的色盲友好性"""
    # 主题的主要颜色
    theme_colors = {
        "背景色": "#fdfdfd",
        "主文本": "#1a1a1a", 
        "关键字": "#dc2626",
        "字符串": "#047857",
        "数字/类型": "#c2410c",
        "函数": "#2563eb",
        "注释": "#6b7280",
        "操作符": "#1f2937"
    }
    
    test_color_discrimination(theme_colors)
    
    print("\n" + "="*60)
    print("色盲友好性分析:")
    print("="*60)
    
    # 分析关键颜色对的区分度
    critical_pairs = [
        ("关键字", "字符串", "红色关键字 vs 绿色字符串"),
        ("关键字", "数字/类型", "红色关键字 vs 橙色数字"),
        ("字符串", "数字/类型", "绿色字符串 vs 橙色数字"),
        ("函数", "关键字", "蓝色函数 vs 红色关键字")
    ]
    
    for color1_name, color2_name, description in critical_pairs:
        color1 = theme_colors[color1_name]
        color2 = theme_colors[color2_name]
        
        print(f"\n{description}:")
        
        # 检查在不同色盲条件下的区分度
        for sim_name, sim_func in [
            ("红色盲", simulate_deuteranopia),
            ("绿色盲", simulate_deuteranopia)
        ]:
            r1, g1, b1 = hex_to_rgb(color1)
            r2, g2, b2 = hex_to_rgb(color2)
            
            sim_r1, sim_g1, sim_b1 = sim_func(r1, g1, b1)
            sim_r2, sim_g2, sim_b2 = sim_func(r2, g2, b2)
            
            # 计算颜色差异
            diff = abs(sim_r1 - sim_r2) + abs(sim_g1 - sim_g2) + abs(sim_b1 - sim_b2)
            
            status = "✓ 可区分" if diff > 100 else "⚠️ 难以区分"
            print(f"  {sim_name}: {status} (差异值: {diff})")


def main():
    """主函数"""
    analyze_theme_accessibility()
    
    print("\n" + "="*60)
    print("建议:")
    print("="*60)
    print("1. 我们已经为不同语法元素添加了字体样式区分（粗体、斜体、下划线）")
    print("2. 这些字体样式为色盲用户提供了额外的视觉提示")
    print("3. 即使颜色难以区分，用户仍可通过字体样式识别语法元素")
    print("4. 建议在VS Code中启用括号对着色以获得更好的结构化视觉提示")


if __name__ == '__main__':
    main()
