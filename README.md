# Accessible Light Theme for VS Code

A carefully crafted light theme optimized for accessibility, color-blind users, and projector/presentation scenarios.

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

**Color Palette:**

- 🔴 **Red (#dc2626)** → Keywords (import, const, interface), HTML tags, errors
- 🟢 **Green (#059669)** → Strings, success states, added lines in diff
- 🟠 **Orange (#d97706)** → Numbers, types, constants, changed files
- 🔵 **Blue (#2563eb)** → Functions, methods, links
- ⚫ **Gray (#7c7c7c)** → Comments, disabled text

## ✨ Features

- **🎯 High Contrast**: Enhanced red-green contrast for better readability
- **♿ Accessibility Focused**: Color-blind friendly design with multiple visual cues
- **📽️ Projector Optimized**: Clear visibility in presentation environments
- **🔍 Enhanced Borders**: Visible UI boundaries for better structure comprehension
- **🌈 Semantic Colors**: Meaningful color usage across syntax highlighting

## 🎨 Color Palette

| Color | Hex Code | Usage |
|-------|----------|-------|
| 🔴 Red | `#dc2626` | Keywords, errors, important elements |
| 🟢 Green | `#059669` | Strings, success states, insertions |
| 🟠 Orange | `#d97706` | Numbers, constants, types |
| 🔵 Blue | `#2563eb` | Functions, links, methods |
| ⚫ Gray | `#7c7c7c` | Comments, secondary information |

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
