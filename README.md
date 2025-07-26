# Accessible Light Theme for VS Code

A light theme designed for **everyone** - including color-blind developers, screen reader users, and anyone who needs high contrast coding.

## 🎯 Live Preview

[🌐 View Interactive Preview](./preview.html) | [📱 GitHub Preview](https://htmlpreview.github.io/?https://github.com/donghao1393/vscode-accessible-light-theme/blob/master/preview.html)

## 🎯 What Makes This Special?

**Real accessibility, not just claims:**
- ✅ All colors tested to meet WCAG AA standards (4.5:1 contrast)
- ✅ Works great for red-green color blindness (most common type)
- ✅ Font styles (bold, italic) help distinguish code elements beyond just color
- ✅ Perfect for projectors and bright rooms
- ✅ Screen reader friendly with consistent color hierarchy

## 🎨 Color Palette

| Color | Hex Code | Contrast | Used For |
|-------|----------|----------|----------|
| 🔴 Red | `#dc2626` | 4.75:1 | Keywords (`function`, `if`, `class`) |
| 🟢 Green | `#047857` | 5.39:1 | Strings (`"hello world"`) |
| 🟠 Orange | `#c2410c` | 5.09:1 | Numbers (`42`, `3.14`) and types |
| 🔵 Blue | `#2563eb` | 5.08:1 | Function names (`myFunction()`) |
| ⚫ Gray | `#6b7280` | 4.75:1 | Comments (`// like this`) |

## 🚀 How to Install and Use

### Step 1: Install the Theme
**Option A: From VS Code Marketplace**
1. Open VS Code
2. Click the Extensions icon (or press `Ctrl+Shift+X`)
3. Search for "Accessible Light Theme"
4. Click "Install"

**Option B: From Downloaded File**
1. Download the `.vsix` file
2. Open VS Code
3. Press `Ctrl+Shift+P` and type "Extensions: Install from VSIX"
4. Select the downloaded file

### Step 2: Activate the Theme
1. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
2. Type "Preferences: Color Theme"
3. Select "Accessible Light"

### Step 3: Optimize Your Experience (Optional but Recommended)

To get the most out of this theme, you can add some settings to VS Code:

1. **Open VS Code Settings:**
   - Press `Ctrl+,` (Windows/Linux) or `Cmd+,` (Mac)
   - Click the "Open Settings (JSON)" icon in the top-right corner

2. **Add these settings to your `settings.json` file:**
   ```json
   {
     "editor.bracketPairColorization.enabled": true,
     "terminal.integrated.minimumContrastRatio": 4.5,
     "accessibility.signals.lineHasError.sound": "on"
   }
   ```

3. **Save the file** (Ctrl+S or Cmd+S)

**What do these settings do?**
- `bracketPairColorization`: Colors matching brackets so you can see code structure better
- `minimumContrastRatio`: Ensures terminal text is always readable
- `lineHasError.sound`: Plays a sound when there's an error (helpful for screen readers)

## 👥 Who This Helps

### 🎨 Color-Blind Developers
- **Font styles matter**: Keywords are **bold**, strings are *italic*, types are <u>underlined</u>
- **High contrast**: All colors tested with color-blind simulation
- **Multiple cues**: Important information never relies on color alone

### 🔊 Screen Reader Users
- Compatible with NVDA, JAWS, and VoiceOver
- Consistent color hierarchy for better navigation
- Optional sound alerts for errors and warnings

### 📽️ Teachers and Presenters
- Optimized for projectors and bright environments
- Clear visibility from the back of the room
- High contrast maintains readability on any screen

## ✅ Quality Guarantee

**All colors meet WCAG AA standards** (4.5:1 contrast ratio minimum):

| Element | Contrast Ratio | Status |
|---------|----------------|--------|
| Main text | 17.11:1 | ✅ Excellent |
| Keywords | 4.75:1 | ✅ Pass |
| Strings | 5.39:1 | ✅ Pass |
| Numbers | 5.09:1 | ✅ Pass |
| Functions | 5.08:1 | ✅ Pass |
| Comments | 4.75:1 | ✅ Pass |

**Want to verify yourself?**
- Run: `just test` (modern Rust-based task runner)
- Or: `uv run pytest tests/` (direct pytest command)

## 🔧 Advanced Customization

If you want to adjust colors further, you can override them in your VS Code settings:

1. Open your `settings.json` file (see Step 3 above)
2. Add a `workbench.colorCustomizations` section:
   ```json
   {
     "workbench.colorCustomizations": {
       "[Accessible Light]": {
         "editor.background": "#ffffff",
         "editor.foreground": "#000000"
       }
     }
   }
   ```

This example makes the background pure white and text pure black for even higher contrast.

## 🤝 Contributing

Found an accessibility issue? Have suggestions? 
- [Open an issue](https://github.com/donghao1393/vscode-accessible-light-theme/issues)
- [Read our accessibility guide](ACCESSIBILITY.md)

## 📄 License

MIT License - feel free to use and modify!

---

**Made with ❤️ for accessible coding**
