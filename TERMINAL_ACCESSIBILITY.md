# 终端无障碍性指南

本文档专门介绍如何在VS Code终端中最大化利用Accessible Light Theme的无障碍特性。

## 🖥️ 终端颜色优化

### ANSI颜色对比度
我们的主题为终端提供了完整的16色ANSI调色板，所有颜色都符合WCAG AA标准：

| 颜色 | 标准版本 | 对比度 | 明亮版本 | 用途 |
|------|----------|--------|----------|------|
| Black | `#1f2937` | 14.43:1 ✅ | `#374151` | 文本、边框 |
| Red | `#dc2626` | 4.75:1 ✅ | `#b91c1c` | 错误、警告 |
| Green | `#047857` | 5.39:1 ✅ | `#047857` | 成功、确认 |
| Yellow | `#c2410c` | 5.09:1 ✅ | `#a16207` | 警告、注意 |
| Blue | `#2563eb` | 5.08:1 ✅ | `#1d4ed8` | 信息、链接 |
| Magenta | `#7c2d92` | 7.80:1 ✅ | `#6b21a8` | 特殊标记 |
| Cyan | `#0e7490` | 4.52:1 ✅ | `#0e7490` | 高亮、强调 |
| White | `#6b7280` | 4.75:1 ✅ | `#1a1a1a` | 普通文本 |

## ⚙️ 推荐的终端设置

### 基础无障碍设置
```json
{
  // 启用最小对比度自动调整
  "terminal.integrated.minimumContrastRatio": 4.5,
  
  // 增大字体以提高可读性
  "terminal.integrated.fontSize": 14,
  "terminal.integrated.lineHeight": 1.4,
  
  // 启用光标闪烁
  "terminal.integrated.cursorBlinking": true,
  "terminal.integrated.cursorStyle": "block",
  
  // 启用选择高亮
  "terminal.integrated.copyOnSelection": false,
  "terminal.integrated.rightClickBehavior": "selectWord"
}
```

### 屏幕阅读器优化
```json
{
  // 启用屏幕阅读器支持
  "terminal.integrated.accessibilitySupport": "on",
  
  // 禁用动画以减少干扰
  "terminal.integrated.smoothScrolling": false,
  
  // 启用Tab焦点模式
  "editor.tabFocusMode": true,
  
  // 增加滚动缓冲区
  "terminal.integrated.scrollback": 10000
}
```

### 色盲用户设置
```json
{
  // 启用高对比度模式（如果需要）
  "workbench.colorCustomizations": {
    "[Accessible Light]": {
      // 进一步增强对比度
      "terminal.foreground": "#000000",
      "terminal.ansiRed": "#cc0000",
      "terminal.ansiGreen": "#006600"
    }
  }
}
```

## 🔧 终端无障碍功能

### 1. 可访问视图 (Alt+F2)
- 在终端中按 `Alt+F2` 打开可访问视图
- 逐字符、逐行检查终端内容
- 特别适合屏幕阅读器用户

### 2. 终端导航
- `Ctrl+Shift+O`: 在终端中跳转到符号
- `F6` / `Shift+F6`: 在面板间切换焦点
- `Ctrl+``: 打开/关闭终端

### 3. Shell集成功能
启用shell集成以获得更好的无障碍体验：
```bash
# 对于bash用户，添加到 ~/.bashrc
eval "$(code --locate-shell-integration-path bash)"

# 对于zsh用户，添加到 ~/.zshrc  
eval "$(code --locate-shell-integration-path zsh)"

# 对于fish用户，添加到 ~/.config/fish/config.fish
string replace -r ".*" "code --locate-shell-integration-path fish" | source
```

### 4. 命令历史导航
- `Ctrl+R`: 搜索命令历史
- `Ctrl+Shift+R`: 运行最近命令（需要shell集成）
- `Ctrl+Shift+G`: 跳转到最近目录（需要shell集成）

## 🎨 终端主题自定义

### 进一步提高对比度
如果需要更高的对比度，可以自定义颜色：

```json
{
  "workbench.colorCustomizations": {
    "[Accessible Light]": {
      // 使用纯黑色文本
      "terminal.foreground": "#000000",
      
      // 增强错误颜色
      "terminal.ansiRed": "#990000",
      
      // 增强成功颜色  
      "terminal.ansiGreen": "#006600",
      
      // 增强光标可见性
      "terminalCursor.foreground": "#ff0000",
      "terminalCursor.background": "#ffffff"
    }
  }
}
```

### 为特定工具优化
```json
{
  "workbench.colorCustomizations": {
    "[Accessible Light]": {
      // Git输出优化
      "terminal.ansiGreen": "#047857",  // git add
      "terminal.ansiRed": "#dc2626",   // git rm
      "terminal.ansiYellow": "#c2410c", // git modify
      
      // 测试输出优化
      "terminal.ansiBrightGreen": "#047857", // 测试通过
      "terminal.ansiBrightRed": "#b91c1c",   // 测试失败
      "terminal.ansiBrightYellow": "#a16207" // 测试警告
    }
  }
}
```

## 🧪 终端测试建议

### 对比度测试
使用我们的测试脚本验证终端颜色：
```bash
# 测试终端颜色对比度
python3 scripts/terminal-contrast-check.py
```

### 实际使用测试
1. **Git操作**: 运行 `git status`, `git diff` 检查颜色区分度
2. **编译输出**: 运行构建命令检查错误/警告颜色
3. **测试输出**: 运行测试套件检查通过/失败颜色
4. **日志查看**: 查看应用日志检查不同级别的可读性

### 色盲友好性验证
1. 使用色盲模拟器测试终端输出
2. 确保重要信息不仅依赖颜色（如添加符号）
3. 验证错误和成功状态在色盲条件下仍可区分

## 🚀 高级技巧

### 1. 自定义提示符
为提示符添加无障碍友好的元素：
```bash
# 在提示符中添加状态符号
PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
```

### 2. 别名优化
创建带有颜色输出的别名：
```bash
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias diff='diff --color=auto'
```

### 3. 工具配置
配置常用工具使用无障碍友好的颜色：
```bash
# Git配置
git config --global color.status.changed "yellow bold"
git config --global color.status.untracked "red bold"
git config --global color.status.added "green bold"
```

## 📞 反馈和支持

如果您在终端使用中遇到任何无障碍问题：

1. 检查VS Code的终端无障碍设置
2. 尝试调整 `terminal.integrated.minimumContrastRatio` 设置
3. 使用 `Alt+F1` 获取终端无障碍帮助
4. [提交Issue](https://github.com/donghao1393/vscode-accessible-light-theme/issues) 报告问题

我们致力于为所有用户提供最佳的终端体验！
