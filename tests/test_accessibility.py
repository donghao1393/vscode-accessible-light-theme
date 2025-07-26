"""
Accessibility tests for VS Code Accessible Light Theme
Tests WCAG AA compliance for all theme colors
"""

import pytest
import json
from pathlib import Path


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_luminance(r: int, g: int, b: int) -> float:
    """Calculate relative luminance of RGB color"""
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
    """Calculate contrast ratio between two colors"""
    rgb1 = hex_to_rgb(color1)
    rgb2 = hex_to_rgb(color2)
    
    lum1 = rgb_to_luminance(*rgb1)
    lum2 = rgb_to_luminance(*rgb2)
    
    lighter = max(lum1, lum2)
    darker = min(lum1, lum2)
    
    return (lighter + 0.05) / (darker + 0.05)


# Theme colors for testing
BACKGROUND = '#fdfdfd'
THEME_COLORS = {
    'main_text': '#1a1a1a',
    'keywords': '#dc2626',
    'strings': '#047857',
    'numbers': '#c2410c',
    'functions': '#2563eb',
    'comments': '#6b7280',
    'operators': '#1f2937'
}


class TestWCAGCompliance:
    """Test all theme colors for WCAG AA compliance (4.5:1 contrast ratio)"""
    
    def test_main_text_contrast(self):
        """Main text should have excellent contrast (>7:1 for AAA)"""
        ratio = contrast_ratio(THEME_COLORS['main_text'], BACKGROUND)
        assert ratio >= 7.0, f"Main text contrast {ratio:.2f}:1 below WCAG AAA standard"
    
    def test_keywords_contrast(self):
        """Keywords (red) should meet WCAG AA standard"""
        ratio = contrast_ratio(THEME_COLORS['keywords'], BACKGROUND)
        assert ratio >= 4.5, f"Keywords contrast {ratio:.2f}:1 below WCAG AA standard"
    
    def test_strings_contrast(self):
        """Strings (green) should meet WCAG AA standard"""
        ratio = contrast_ratio(THEME_COLORS['strings'], BACKGROUND)
        assert ratio >= 4.5, f"Strings contrast {ratio:.2f}:1 below WCAG AA standard"
    
    def test_numbers_contrast(self):
        """Numbers (orange) should meet WCAG AA standard"""
        ratio = contrast_ratio(THEME_COLORS['numbers'], BACKGROUND)
        assert ratio >= 4.5, f"Numbers contrast {ratio:.2f}:1 below WCAG AA standard"
    
    def test_functions_contrast(self):
        """Functions (blue) should meet WCAG AA standard"""
        ratio = contrast_ratio(THEME_COLORS['functions'], BACKGROUND)
        assert ratio >= 4.5, f"Functions contrast {ratio:.2f}:1 below WCAG AA standard"
    
    def test_comments_contrast(self):
        """Comments (gray) should meet WCAG AA standard"""
        ratio = contrast_ratio(THEME_COLORS['comments'], BACKGROUND)
        assert ratio >= 4.5, f"Comments contrast {ratio:.2f}:1 below WCAG AA standard"
    
    def test_operators_contrast(self):
        """Operators (dark gray) should meet WCAG AA standard"""
        ratio = contrast_ratio(THEME_COLORS['operators'], BACKGROUND)
        assert ratio >= 4.5, f"Operators contrast {ratio:.2f}:1 below WCAG AA standard"


def test_theme_json_validity():
    """Ensure theme JSON file is valid"""
    theme_path = Path(__file__).parent.parent / 'themes' / 'accessible-light-theme.json'
    assert theme_path.exists(), "Theme JSON file not found"
    
    with open(theme_path, 'r', encoding='utf-8') as f:
        theme_data = json.load(f)
    
    assert 'colors' in theme_data, "Theme missing 'colors' section"
    assert 'tokenColors' in theme_data, "Theme missing 'tokenColors' section"


def quick_check():
    """Quick accessibility check for CLI usage"""
    print("🎨 Accessible Light Theme - Quick Contrast Check")
    print("=" * 55)
    
    all_passed = True
    
    for name, color in THEME_COLORS.items():
        ratio = contrast_ratio(color, BACKGROUND)
        passed = ratio >= 4.5
        status = "✅ PASS" if passed else "❌ FAIL"
        
        print(f"{status} {name.replace('_', ' ').title():<12}: {ratio:.2f}:1")
        
        if not passed:
            all_passed = False
    
    print("=" * 55)
    
    if all_passed:
        print("🎉 All colors meet WCAG AA standards!")
    else:
        print("⚠️  Some colors need adjustment")
    
    return all_passed


if __name__ == "__main__":
    quick_check()
