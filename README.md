# Accessible Light Theme for VS Code

A carefully crafted light theme optimized for accessibility, color-blind users, and projector/presentation scenarios.

## 🎯 Interactive Preview

<details>
<summary>📺 Click to see live theme preview</summary>

<div style="font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace; background: #fdfdfd; color: #1a1a1a; padding: 20px; border: 1px solid #d0d0d0; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
  <div style="background: #fafafa; border-bottom: 1px solid #e0e0e0; padding: 8px 16px; color: #2c2c2c; font-size: 13px; display: flex; align-items: center; gap: 8px;">
    <div style="display: flex; gap: 6px;">
      <div style="width: 12px; height: 12px; border-radius: 50%; background: #ff5f57;"></div>
      <div style="width: 12px; height: 12px; border-radius: 50%; background: #ffbd2e;"></div>
      <div style="width: 12px; height: 12px; border-radius: 50%; background: #28ca42;"></div>
    </div>
    <span>VS Code - Accessible Light Theme</span>
  </div>
  
  <div style="display: flex; height: 400px;">
    <div style="width: 180px; background: #fafafa; border-right: 1px solid #e0e0e0; padding: 12px; font-size: 11px; color: #2c2c2c;">
      <div style="color: #dc2626; font-weight: bold; margin-bottom: 8px; text-transform: uppercase; font-size: 10px;">EXPLORER</div>
      <div style="padding: 2px 0;">📁 src/</div>
      <div style="padding: 2px 0;">├── 📄 components/</div>
      <div style="padding: 2px 0;">├── 📄 utils/</div>
      <div style="padding: 2px 0;">├── 📄 App.tsx</div>
      <div style="padding: 2px 0;">└── 📄 index.ts</div>
      <div style="padding: 2px 0;">📄 package.json</div>
    </div>
    <div style="flex: 1; display: flex; flex-direction: column;">
      <div style="background: #fafafa; border-bottom: 1px solid #e0e0e0; display: flex;">
        <div style="padding: 8px 16px; background: #fdfdfd; border-bottom: 2px solid #dc2626; font-size: 12px; color: #2c2c2c;">App.tsx</div>
      </div>
      <div style="flex: 1; background: #fdfdfd; padding: 16px; font-size: 13px; line-height: 1.6; overflow-y: auto;">
        <div style="margin-bottom: 2px;">
          <span style="display: inline-block; width: 25px; color: #a0a0a0; text-align: right; margin-right: 16px;">1</span>
          <span style="color: #dc2626; font-weight: bold;">import</span> 
          <span style="color: #dc2626;">React</span>
          <span style="color: #dc2626; font-weight: bold;">,</span> 
          <span>{</span> 
          <span style="color: #2563eb; font-weight: bold;">useState</span>
          <span style="color: #dc2626; font-weight: bold;">,</span> 
          <span style="color: #2563eb; font-weight: bold;">useEffect</span> 
          <span>}</span> 
          <span style="color: #dc2626; font-weight: bold;">from</span> 
          <span style="color: #059669; font-style: italic;">'react'</span>
          <span style="color: #dc2626; font-weight: bold;">;</span>
        </div>
        <div style="margin-bottom: 2px;">
          <span style="display: inline-block; width: 25px; color: #a0a0a0; text-align: right; margin-right: 16px;">2</span>
        </div>
        <div style="margin-bottom: 2px;">
          <span style="display: inline-block; width: 25px; color: #a0a0a0; text-align: right; margin-right: 16px;">3</span>
          <span style="color: #7c7c7c; font-style: italic;">// User interface definition</span>
        </div>
        <div style="margin-bottom: 2px;">
          <span style="display: inline-block; width: 25px; color: #2c2c2c; text-align: right; margin-right: 16px; font-weight: bold;">4</span>
          <span style="color: #dc2626; font-weight: bold;">interface</span> 
          <span style="color: #d97706; font-weight: bold;">User</span> 
          <span>{</span>
        </div>
        <div style="margin-bottom: 2px;">
          <span style="display: inline-block; width: 25px; color: #a0a0a0; text-align: right; margin-right: 16px;">5</span>
          <span style="padding-left: 16px;">
            <span style="color: #d97706;">id</span>
            <span style="color: #dc2626; font-weight: bold;">:</span> 
            <span style="color: #d97706;">number</span>
            <span style="color: #dc2626; font-weight: bold;">;</span>
          </span>
        </div>
        <div style="margin-bottom: 2px;">
          <span style="display: inline-block; width: 25px; color: #a0a0a0; text-align: right; margin-right: 16px;">6</span>
          <span style="padding-left: 16px;">
            <span style="color: #d97706;">name</span>
            <span style="color: #dc2626; font-weight: bold;">:</span> 
            <span style="color: #d97706;">string</span>
            <span style="color: #dc2626; font-weight: bold;">;</span>
          </span>
        </div>
        <div style="margin-bottom: 2px;">
          <span style="display: inline-block; width: 25px; color: #a0a0a0; text-align: right; margin-right: 16px;">7</span>
          <span style="padding-left: 16px;">
            <span style="color: #d97706;">isActive</span>
            <span style="color: #dc2626; font-weight: bold;">:</span> 
            <span style="color: #d97706;">boolean</span>
            <span style="color: #dc2626; font-weight: bold;">;</span>
          </span>
        </div>
        <div style="margin-bottom: 2px;">
          <span style="display: inline-block; width: 25px; color: #a0a0a0; text-align: right; margin-right: 16px;">8</span>
          <span>}</span>
        </div>
        <div style="margin-bottom: 2px;">
          <span style="display: inline-block; width: 25px; color: #a0a0a0; text-align: right; margin-right: 16px;">9</span>
        </div>
        <div style="margin-bottom: 2px;">
          <span style="display: inline-block; width: 25px; color: #a0a0a0; text-align: right; margin-right: 16px;">10</span>
          <span style="color: #dc2626; font-weight: bold;">const</span> 
          <span style="color: #2563eb; font-weight: bold;">App</span>
          <span style="color: #dc2626; font-weight: bold;">:</span> 
          <span style="color: #d97706; font-weight: bold;">React.FC</span> 
          <span style="color: #dc2626; font-weight: bold;">=</span> 
          <span>() </span>
          <span style="color: #dc2626; font-weight: bold;">=></span> 
          <span>{</span>
        </div>
        <div style="margin-bottom: 2px;">
          <span style="display: inline-block; width: 25px; color: #a0a0a0; text-align: right; margin-right: 16px;">11</span>
          <span style="padding-left: 16px;">
            <span style="color: #dc2626; font-weight: bold;">const</span> 
            <span>[</span>
            <span style="color: #dc2626;">users</span>
            <span style="color: #dc2626; font-weight: bold;">,</span> 
            <span style="color: #dc2626;">setUsers</span>
            <span>] </span>
            <span style="color: #dc2626; font-weight: bold;">=</span> 
            <span style="color: #2563eb; font-weight: bold;">useState</span>
            <span style="color: #dc2626; font-weight: bold;"><</span>
            <span style="color: #d97706; font-weight: bold;">User</span>
            <span>[]</span>
            <span style="color: #dc2626; font-weight: bold;">></span>
            <span>([]);</span>
          </span>
        </div>
        <div style="margin-bottom: 2px;">
          <span style="display: inline-block; width: 25px; color: #a0a0a0; text-align: right; margin-right: 16px;">12</span>
          <span style="padding-left: 16px;">
            <span style="color: #dc2626; font-weight: bold;">const</span> 
            <span style="color: #dc2626;">maxUsers</span> 
            <span style="color: #dc2626; font-weight: bold;">=</span> 
            <span style="color: #d97706; font-weight: bold;">100</span>
            <span style="color: #dc2626; font-weight: bold;">;</span>
          </span>
        </div>
      </div>
    </div>
  </div>
  
  <div style="background: #fafafa; border-top: 1px solid #e0e0e0; padding: 4px 16px; font-size: 11px; color: #2c2c2c; display: flex; justify-content: space-between;">
    <div>UTF-8 · LF · TypeScript React</div>
    <div>Ln 4, Col 18 · Accessible Light</div>
  </div>
</div>

</details>

## ✨ Features

- **🎯 High Contrast**: Enhanced red-green contrast for better readability
- **♿ Accessibility Focused**: Color-blind friendly design with multiple visual cues
- **📽️ Projector Optimized**: Clear visibility in presentation environments
- **🔍 Enhanced Borders**: Visible UI boundaries for better structure comprehension
- **🌈 Semantic Colors**: Meaningful color usage across syntax highlighting

## 🎨 Color Palette

<div style="display: flex; gap: 16px; margin: 16px 0; flex-wrap: wrap;">
  <div style="display: flex; align-items: center; gap: 8px; font-size: 14px;">
    <div style="width: 24px; height: 24px; border-radius: 6px; background: #dc2626; border: 1px solid #ccc;"></div>
    <span><strong>Red (#dc2626)</strong> - Keywords, errors, important elements</span>
  </div>
  <div style="display: flex; align-items: center; gap: 8px; font-size: 14px;">
    <div style="width: 24px; height: 24px; border-radius: 6px; background: #059669; border: 1px solid #ccc;"></div>
    <span><strong>Green (#059669)</strong> - Strings, success states, insertions</span>
  </div>
  <div style="display: flex; align-items: center; gap: 8px; font-size: 14px;">
    <div style="width: 24px; height: 24px; border-radius: 6px; background: #d97706; border: 1px solid #ccc;"></div>
    <span><strong>Orange (#d97706)</strong> - Numbers, constants, types</span>
  </div>
  <div style="display: flex; align-items: center; gap: 8px; font-size: 14px;">
    <div style="width: 24px; height: 24px; border-radius: 6px; background: #2563eb; border: 1px solid #ccc;"></div>
    <span><strong>Blue (#2563eb)</strong> - Functions, links, methods</span>
  </div>
  <div style="display: flex; align-items: center; gap: 8px; font-size: 14px;">
    <div style="width: 24px; height: 24px; border-radius: 6px; background: #7c7c7c; border: 1px solid #ccc;"></div>
    <span><strong>Gray (#7c7c7c)</strong> - Comments, secondary information</span>
  </div>
</div>

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

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">
  <div style="border: 1px solid #d0d0d0; border-radius: 8px; overflow: hidden;">
    <div style="background: #fafafa; padding: 8px 12px; border-bottom: 1px solid #e0e0e0; font-weight: bold; font-size: 12px; color: #2c2c2c;">TypeScript/React</div>
    <div style="background: #fdfdfd; padding: 12px; font-family: 'Monaco', 'Courier New', monospace; font-size: 12px; color: #1a1a1a;">Enhanced syntax highlighting<br/>with clear color distinction</div>
  </div>
  <div style="border: 1px solid #d0d0d0; border-radius: 8px; overflow: hidden;">
    <div style="background: #fafafa; padding: 8px 12px; border-bottom: 1px solid #e0e0e0; font-weight: bold; font-size: 12px; color: #2c2c2c;">Terminal Integration</div>
    <div style="background: #fdfdfd; padding: 12px; font-family: 'Monaco', 'Courier New', monospace; font-size: 12px; color: #1a1a1a;">Consistent colors in<br/>integrated terminal</div>
  </div>
  <div style="border: 1px solid #d0d0d0; border-radius: 8px; overflow: hidden;">
    <div style="background: #fafafa; padding: 8px 12px; border-bottom: 1px solid #e0e0e0; font-weight: bold; font-size: 12px; color: #2c2c2c;">Git Integration</div>
    <div style="background: #fdfdfd; padding: 12px; font-family: 'Monaco', 'Courier New', monospace; font-size: 12px; color: #1a1a1a;">Clear diff visualization<br/>and git decorations</div>
  </div>
</div>

> 📝 More screenshots will be added in future releases

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
