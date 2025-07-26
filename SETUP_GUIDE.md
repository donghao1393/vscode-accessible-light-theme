# 无障碍主题设置指南

本指南将帮助你充分利用 Accessible Light Theme 的所有无障碍特性。

## 🚀 快速开始

### 1. 安装主题
```bash
# 方法1: 从VSIX文件安装
code --install-extension accessible-light-theme-1.1.0.vsix

# 方法2: 从VS Code Marketplace安装（即将发布）
# 在扩展面板搜索 "Accessible Light Theme"
```

### 2. 激活主题
1. 打开 VS Code
2. 按 `Ctrl+Shift+P` (Windows/Linux) 或 `Cmd+Shift+P` (macOS)
3. 输入 "Color Theme"
4. 选择 "Accessible Light"

### 3. 应用推荐设置
选择适合你的设置方式：

#### 方法A: 完整设置（推荐）
1. 打开 VS Code 设置：`Ctrl+,` (Windows/Linux) 或 `Cmd+,` (macOS)
2. 点击右上角的 "Open Settings (JSON)" 图标
3. 将 `recommended-settings.json` 的内容复制到你的设置文件中

#### 方法B: 逐步设置
根据你的需求选择性添加设置：

```json
{
  // 基础无障碍设置
  "editor.accessibilitySupport": "auto",
  "accessibility.signals.lineHasError.sound": "on",
  "editor.fontSize": 14,
  "editor.lineHeight": 1.6,
  
  // 括号和缩进增强
  "editor.bracketPairColorization.enabled": true,
  "editor.guides.bracketPairs": "active",
  
  // 终端优化
  "terminal.integrated.minimumContrastRatio": 4.5,
  "terminal.integrated.fontSize": 14
}
```

## 👥 针对不同用户群体的设置

### 🔍 屏幕阅读器用户
```json
{
  "editor.accessibilitySupport": "on",
  "editor.tabFocusMode": true,
  "editor.minimap.enabled": false,
  "terminal.integrated.accessibilitySupport": "on",
  "workbench.reduceMotion": "on",
  "accessibility.signals.lineHasError.sound": "on",
  "accessibility.signals.lineHasWarning.sound": "on"
}
```

### 👁️ 低视力用户
```json
{
  "editor.fontSize": 18,
  "editor.lineHeight": 2.0,
  "editor.cursorWidth": 5,
  "terminal.integrated.fontSize": 16,
  "workbench.tree.indent": 25,
  "zoom.level": 1,
  "editor.renderLineHighlight": "all"
}
```

### 🎨 色盲用户
```json
{
  "git.decorations.enabled": true,
  "scm.diffDecorations": "all",
  "editor.renderControlCharacters": true,
  "editor.bracketPairColorization.enabled": true,
  "editor.guides.bracketPairs": "active"
}
```

### 📽️ 演示和教学
```json
{
  "editor.fontSize": 16,
  "editor.lineHeight": 1.8,
  "terminal.integrated.fontSize": 16,
  "editor.minimap.enabled": false,
  "workbench.activityBar.visible": true,
  "editor.rulers": [80],
  "zoom.level": 1
}
```

## 🔧 高级自定义

### 进一步提高对比度
如果需要更高的对比度：

```json
{
  "workbench.colorCustomizations": {
    "[Accessible Light]": {
      "editor.background": "#ffffff",
      "editor.foreground": "#000000",
      "terminal.foreground": "#000000",
      "terminal.ansiRed": "#cc0000",
      "terminal.ansiGreen": "#006600"
    }
  }
}
```

### 自定义字体样式
增强语法区分：

```json
{
  "editor.tokenColorCustomizations": {
    "[Accessible Light]": {
      "textMateRules": [
        {
          "scope": "variable",
          "settings": {
            "fontStyle": "italic underline"
          }
        },
        {
          "scope": "constant",
          "settings": {
            "fontStyle": "bold underline"
          }
        }
      ]
    }
  }
}
```

## 🧪 验证设置

### 1. 运行测试
```bash
# 检查对比度
make test-contrast

# 色盲模拟测试
make test-colorblind

# 完整测试
make test
```

### 2. 手动验证清单
- [ ] 所有文本清晰可读
- [ ] 错误和警告易于识别
- [ ] 语法高亮区分明显
- [ ] 终端输出清晰
- [ ] 括号匹配明显
- [ ] 光标和选择清晰可见

## 🔄 常见问题解决

### Q: 字体看起来太小/太大
A: 调整 `editor.fontSize` 和 `terminal.integrated.fontSize`

### Q: 颜色对比度不够
A: 启用 `terminal.integrated.minimumContrastRatio: 4.5`

### Q: 括号难以匹配
A: 确保启用 `editor.bracketPairColorization.enabled: true`

### Q: 屏幕阅读器支持不佳
A: 设置 `editor.accessibilitySupport: "on"`

### Q: 终端颜色不清晰
A: 检查终端的最小对比度设置

## 📱 跨平台注意事项

### Windows
- 确保启用高对比度模式兼容性
- 考虑使用 Windows 放大镜

### macOS
- 利用 VoiceOver 集成
- 考虑启用"减少动画"

### Linux
- 配置屏幕阅读器（如 Orca）
- 调整系统字体渲染

## 🔄 设置同步

### 使用 VS Code Settings Sync
1. 启用设置同步：`Ctrl+Shift+P` → "Settings Sync: Turn On"
2. 选择要同步的项目（包括设置和扩展）
3. 登录 GitHub 或 Microsoft 账户

### 手动备份
定期备份你的 `settings.json` 文件：
- Windows: `%APPDATA%\Code\User\settings.json`
- macOS: `~/Library/Application Support/Code/User/settings.json`
- Linux: `~/.config/Code/User/settings.json`

## 📞 获取帮助

如果遇到问题：
1. 查看 [ACCESSIBILITY.md](ACCESSIBILITY.md) 详细指南
2. 查看 [TERMINAL_ACCESSIBILITY.md](TERMINAL_ACCESSIBILITY.md) 终端指南
3. [提交 Issue](https://github.com/donghao1393/vscode-accessible-light-theme/issues)
4. 参考 VS Code 官方无障碍文档

记住：无障碍性是个人化的，请根据你的具体需求调整这些设置！
