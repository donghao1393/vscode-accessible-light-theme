# Accessible Light Theme for VS Code

A carefully crafted light theme optimized for accessibility, color-blind users, and projector/presentation scenarios.

## 🎯 Live Preview

[🌐 View Interactive Preview](./preview.html) | [📱 GitHub Preview](https://htmlpreview.github.io/?https://github.com/donghao1393/vscode-accessible-light-theme/blob/master/preview.html)

## 🎯 Quick Preview

**Enhanced syntax highlighting with accessibility in mind:**

```typescript
// Comment in gray (#7c7c7c)
import React, { useState } from 'react'; // import keywords in red

interface User {  // interface keyword in red, User type in orange
id: number;    // property in orange, type in orange  
name: string;  // string type in orange
isActive: boolean; // boolean type in orange
}

const App: React.FC = () => {  // const in red, App function in blue
const [users, setUsers] = useState<User[]>([]); // state hooks in blue
const maxUsers = 100; // number in orange

return (
<div className="app">  {/* HTML tags in red */}
<h1>{'User Management'}</h1>  {/* strings in green */}
</div>
);
};
```

**Color Palette (WCAG AA Compliant):**

- 🔴 **Red (#dc2626)** → Keywords (import, const, interface), HTML tags, errors
- 🟢 **Green (#047857)** → Strings, success states, added lines in diff
- 🟠 **Orange (#c2410c)** → Numbers, types, constants, changed files
- 🔵 **Blue (#2563eb)** → Functions, methods, links
- ⚫ **Gray (#6b7280)** → Comments, disabled text

## ✨ Features

- **🎯 WCAG AA Compliant**: All colors meet 4.5:1 contrast ratio requirements
- **♿ Accessibility Focused**: Color-blind friendly design with font style cues
- **📽️ Projector Optimized**: Clear visibility in presentation environments
- **🔍 Enhanced Borders**: Visible UI boundaries for better structure comprehension
- **🌈 Semantic Colors**: Meaningful color usage across syntax highlighting
- **🎨 Font Style Differentiation**: Bold, italic, and underline styles for better element distinction

## 🎨 Color Palette

| Color | Hex Code | Contrast Ratio | Usage |
|-------|----------|----------------|-------|
| 🔴 Red | `#dc2626` | 4.75:1 | Keywords, errors, important elements |
| 🟢 Green | `#047857` | 5.39:1 | Strings, success states, insertions |
| 🟠 Orange | `#c2410c` | 5.09:1 | Numbers, constants, types |
| 🔵 Blue | `#2563eb` | 5.08:1 | Functions, links, methods |
| ⚫ Gray | `#6b7280` | 4.75:1 | Comments, secondary information |

## 🚀 Enhanced Features

### Built-in Bracket Pair Colorization
The theme includes optimized colors for VS Code's built-in bracket pair colorization. Enable it with:

```json
{
  "editor.bracketPairColorization.enabled": true,
  "editor.guides.bracketPairs": "active"
}
```

### Terminal Integration
Consistent color scheme in the integrated terminal for better workflow integration.

### Git Integration
Enhanced diff view and git decoration colors for clearer version control visualization.

### Error Hierarchy
Clear distinction between errors, warnings, and information with appropriate color coding.

## ♿ Accessibility Guide

### WCAG Compliance
This theme is designed to meet **WCAG 2.1 AA standards**:
- All text colors have a contrast ratio of at least 4.5:1 against the background
- Color is not the only means of conveying information
- Font styles provide additional visual cues for different syntax elements

### For Color-Blind Users
The theme includes multiple accessibility features:

**Font Style Indicators:**
- **Bold**: Keywords, functions, numbers, constants
- **Italic**: Comments, strings, variables, attributes
- **Underline**: Type definitions and class names

**High Contrast Colors:**
- All colors have been tested and optimized for different types of color vision deficiency
- Even if colors appear similar, font styles help distinguish syntax elements

### Recommended VS Code Settings
For the best accessibility experience, add these settings to your VS Code configuration:

```json
{
  "editor.bracketPairColorization.enabled": true,
  "editor.guides.bracketPairs": "active",
  "editor.renderWhitespace": "boundary",
  "editor.rulers": [80, 120],
  "accessibility.signals.lineHasError.sound": "on",
  "accessibility.signals.lineHasWarning.sound": "on"
}
```

## 📦 Installation

### From VS Code Marketplace
1. Open VS Code
2. Go to Extensions (`Cmd+Shift+X` / `Ctrl+Shift+X`)
3. Search for "Accessible Light"
4. Click Install

### Manual Installation
1. Download the `.vsix` file from [releases](https://github.com/donghao1393/vscode-accessible-light-theme/releases)
2. Open VS Code
3. Press `Cmd+Shift+P` / `Ctrl+Shift+P`
4. Type "Extensions: Install from VSIX"
5. Select the downloaded file

## 📸 Screenshots

### Key Features

- **💻 TypeScript/React**: Enhanced syntax highlighting with clear color distinction
- **🔄 Terminal Integration**: Consistent colors in integrated terminal
- **🌱 Git Integration**: Clear diff visualization and git decorations
- **🔍 Error Highlighting**: Distinct colors for errors, warnings, and info
- **🔗 Bracket Pairs**: Built-in colorization support

> 📝 Screenshots will be added in future releases

## 🎯 Recommended Extensions

- **Error Lens**: Inline error display
- **Todo Highlight**: Highlight TODO comments
- **GitLens**: Enhanced Git capabilities

## 🧪 Testing & Development

This theme includes comprehensive accessibility testing tools:

```bash
# Run all accessibility tests
make test

# Quick contrast ratio check
make test-contrast

# Color-blind simulation test
make test-colorblind

# Check specific color pair
make check-color COLOR1=#dc2626 COLOR2=#fdfdfd
```

### Test Results
All colors in this theme have been verified to meet WCAG AA standards:
- ✅ Main text: 17.11:1 contrast ratio
- ✅ Keywords: 4.75:1 contrast ratio
- ✅ Strings: 5.39:1 contrast ratio
- ✅ Numbers: 5.09:1 contrast ratio
- ✅ Functions: 5.08:1 contrast ratio
- ✅ Comments: 4.75:1 contrast ratio

## 🔧 Customization

You can override any theme colors in your `settings.json`:

```json
{
  "workbench.colorCustomizations": {
    "[Accessible Light]": {
      "editor.background": "#fefefe"
    }
  }
}
```

## 🙏 Acknowledgments

Originally inspired by [Atom One X Github - Light Gray](https://github.com/softtama/vscode-theme-atom-one-x-github-light-gray) by [Rizki Pratama](https://github.com/softtama).

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you encounter any issues or have suggestions, please [open an issue](https://github.com/donghao1393/vscode-accessible-light-theme/issues).
