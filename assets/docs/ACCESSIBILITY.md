# 无障碍使用指南

本文档详细说明了 Accessible Light Theme 的无障碍特性以及如何最大化其效果。

## 🎯 设计原则

### WCAG 2.1 AA 合规性
- **对比度要求**: 所有文本颜色与背景的对比度至少为 4.5:1
- **颜色独立性**: 不仅依赖颜色传达信息，还使用字体样式作为辅助
- **一致性**: 相同类型的元素使用一致的视觉表示

### 色盲友好设计
- **多重视觉提示**: 颜色 + 字体样式 + 位置信息
- **高对比度**: 即使颜色感知有差异，仍能清晰区分
- **测试验证**: 通过色盲模拟器验证效果

## 🎨 颜色和样式映射

### 语法高亮元素

| 元素类型 | 颜色 | 字体样式 | 对比度 | 用途 |
|---------|------|----------|--------|------|
| 关键字 | 🔴 #dc2626 | **粗体** | 4.75:1 | `function`, `if`, `class` |
| 字符串 | 🟢 #047857 | *斜体* | 5.39:1 | `"hello"`, `'world'` |
| 数字 | 🟠 #c2410c | **粗体** | 5.09:1 | `42`, `3.14` |
| 函数名 | 🔵 #2563eb | **粗体** | 5.08:1 | `myFunction()` |
| 注释 | ⚫ #6b7280 | *斜体* | 4.75:1 | `// comment` |
| 类型定义 | 🟠 #c2410c | <u>下划线</u> | 5.09:1 | `interface User` |
| 变量 | 🔴 #dc2626 | *斜体* | 4.75:1 | `userName` |
| 常量 | 🟠 #c2410c | **粗体** | 5.09:1 | `MAX_SIZE` |

### UI 元素

| 元素 | 颜色 | 用途 |
|------|------|------|
| 错误 | 🔴 #dc2626 | 错误信息和标记 |
| 警告 | 🟠 #c2410c | 警告信息 |
| 信息 | 🔵 #2563eb | 提示信息 |
| 成功 | 🟢 #047857 | 成功状态 |

## 👁️ 不同视觉条件下的体验

### 正常色觉用户
- 享受完整的颜色体验
- 通过颜色快速识别语法元素
- 字体样式提供额外的视觉层次

### 红绿色盲用户 (最常见)
- **主要依赖**: 字体样式区分关键字和字符串
- **辅助信息**: 位置和上下文
- **建议**: 启用括号对着色获得更多结构信息

### 蓝黄色盲用户 (较少见)
- 蓝色函数名可能与其他颜色混淆
- **补偿机制**: 函数名使用粗体样式
- **建议**: 关注字体样式而非颜色

### 全色盲用户 (罕见)
- **完全依赖**: 字体样式和亮度对比
- 所有颜色转换为灰度仍保持足够对比度
- **优势**: 高对比度设计确保可读性

## ⚙️ 推荐的 VS Code 设置

### 基础无障碍设置
```json
{
  // 启用括号对着色
  "editor.bracketPairColorization.enabled": true,
  "editor.guides.bracketPairs": "active",
  
  // 显示空白字符
  "editor.renderWhitespace": "boundary",
  
  // 添加标尺线
  "editor.rulers": [80, 120],
  
  // 启用无障碍信号
  "accessibility.signals.lineHasError.sound": "on",
  "accessibility.signals.lineHasWarning.sound": "on",
  "accessibility.signals.lineHasBreakpoint.sound": "on",
  
  // 增强焦点指示
  "workbench.colorCustomizations": {
    "[Accessible Light]": {
      "focusBorder": "#dc2626",
      "editorCursor.foreground": "#dc2626"
    }
  }
}
```

### 屏幕阅读器用户
```json
{
  // 启用屏幕阅读器优化
  "editor.accessibilitySupport": "on",
  
  // 禁用小地图
  "editor.minimap.enabled": false,
  
  // 增加行高
  "editor.lineHeight": 1.6,
  
  // 启用声音提示
  "accessibility.signals.lineHasError.sound": "on",
  "accessibility.signals.lineHasWarning.sound": "on",
  "accessibility.signals.lineHasFoldedArea.sound": "on"
}
```

### 低视力用户
```json
{
  // 增大字体
  "editor.fontSize": 16,
  "editor.lineHeight": 1.8,
  
  // 增强光标
  "editor.cursorWidth": 3,
  "editor.cursorBlinking": "solid",
  
  // 高亮当前行
  "editor.renderLineHighlight": "all",
  
  // 增强选择高亮
  "editor.selectionHighlight": true,
  "editor.occurrencesHighlight": true
}
```

## 🧪 测试工具

### 自动化测试
```bash
# 运行所有无障碍测试
make test

# 检查对比度
make test-contrast

# 色盲模拟测试
make test-colorblind
```

### 手动验证
1. **对比度检查**: 使用浏览器开发者工具的对比度检查器
2. **色盲模拟**: 使用 Sim Daltonism (macOS) 或类似工具
3. **屏幕阅读器**: 使用 NVDA、JAWS 或 VoiceOver 测试

## 🔧 自定义建议

### 进一步提高对比度
如果需要更高的对比度，可以调整这些颜色：

```json
{
  "workbench.colorCustomizations": {
    "[Accessible Light]": {
      // 使用更深的绿色
      "editor.tokenColorCustomizations": {
        "strings": "#065f46"
      }
    }
  }
}
```

### 添加更多视觉提示
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
        }
      ]
    }
  }
}
```

## 📞 反馈和支持

如果您在使用过程中遇到任何无障碍问题，请：

1. [提交 Issue](https://github.com/donghao1393/vscode-accessible-light-theme/issues)
2. 描述您的具体需求和使用场景
3. 提供您的 VS Code 版本和操作系统信息

我们致力于为所有用户提供最佳的编程体验！
