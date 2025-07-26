#!/usr/bin/env python3
"""
Theme accessibility tests using pytest
Run with: python3 -m pytest test_theme.py -v
"""

import pytest

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_luminance(r, g, b):
    """Calculate relative luminance of RGB color"""
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
    """Calculate contrast ratio between two colors"""
    rgb1 = hex_to_rgb(color1)
    rgb2 = hex_to_rgb(color2)
    
    lum1 = rgb_to_luminance(*rgb1)
    lum2 = rgb_to_luminance(*rgb2)
    
    lighter = max(lum1, lum2)
    darker = min(lum1, lum2)
    
    return (lighter + 0.05) / (darker + 0.05)

# Theme colors
BACKGROUND = '#fdfdfd'
COLORS = {
    'main_text': '#1a1a1a',
    'keywords': '#dc2626',
    'strings': '#047857',
    'numbers': '#c2410c',
    'functions': '#2563eb',
    'comments': '#6b7280',
    'operators': '#1f2937'
}

class TestAccessibility:
    """Test theme colors for WCAG AA compliance"""
    
    def test_main_text_contrast(self):
        """Main text should have excellent contrast"""
        ratio = contrast_ratio(COLORS['main_text'], BACKGROUND)
        assert ratio >= 4.5, f"Main text contrast {ratio:.2f}:1 below WCAG AA standard"
        assert ratio >= 7.0, f"Main text contrast {ratio:.2f}:1 below WCAG AAA standard"
    
    def test_keywords_contrast(self):
        """Keywords should meet WCAG AA standard"""
        ratio = contrast_ratio(COLORS['keywords'], BACKGROUND)
        assert ratio >= 4.5, f"Keywords contrast {ratio:.2f}:1 below WCAG AA standard"
    
    def test_strings_contrast(self):
        """Strings should meet WCAG AA standard"""
        ratio = contrast_ratio(COLORS['strings'], BACKGROUND)
        assert ratio >= 4.5, f"Strings contrast {ratio:.2f}:1 below WCAG AA standard"
    
    def test_numbers_contrast(self):
        """Numbers should meet WCAG AA standard"""
        ratio = contrast_ratio(COLORS['numbers'], BACKGROUND)
        assert ratio >= 4.5, f"Numbers contrast {ratio:.2f}:1 below WCAG AA standard"
    
    def test_functions_contrast(self):
        """Functions should meet WCAG AA standard"""
        ratio = contrast_ratio(COLORS['functions'], BACKGROUND)
        assert ratio >= 4.5, f"Functions contrast {ratio:.2f}:1 below WCAG AA standard"
    
    def test_comments_contrast(self):
        """Comments should meet WCAG AA standard"""
        ratio = contrast_ratio(COLORS['comments'], BACKGROUND)
        assert ratio >= 4.5, f"Comments contrast {ratio:.2f}:1 below WCAG AA standard"
    
    def test_operators_contrast(self):
        """Operators should meet WCAG AA standard"""
        ratio = contrast_ratio(COLORS['operators'], BACKGROUND)
        assert ratio >= 4.5, f"Operators contrast {ratio:.2f}:1 below WCAG AA standard"

def test_all_colors_summary():
    """Print summary of all color contrast ratios"""
    print("\n🎨 Theme Color Contrast Summary:")
    print("=" * 50)
    
    for name, color in COLORS.items():
        ratio = contrast_ratio(color, BACKGROUND)
        status = "✅ PASS" if ratio >= 4.5 else "❌ FAIL"
        print(f"{status} {name.replace('_', ' ').title():<12}: {ratio:.2f}:1")
    
    print("=" * 50)

if __name__ == "__main__":
    # Run tests directly
    test_all_colors_summary()
    
    # Run pytest if available
    try:
        import subprocess
        result = subprocess.run(['python3', '-m', 'pytest', __file__, '-v'], 
                              capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
    except:
        print("pytest not available, but manual tests completed above")
