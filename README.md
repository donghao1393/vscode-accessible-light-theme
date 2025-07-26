# Clean Light Theme for VS Code

*Finally, a light theme that doesn't hurt your eyes.*

## 🎯 Why This Theme?

**Tired of ugly VS Code themes?** So was I. Most light themes are either:
- Too cluttered and distracting
- Have terrible color choices  
- Hard to read during long coding sessions
- Look awful when presenting code

This theme is different: **clean, simple, and actually pleasant to look at.**

## 🌟 Live Preview

[🌐 **Try Interactive Preview**](https://htmlpreview.github.io/?https://github.com/donghao1393/vscode-accessible-light-theme/blob/master/assets/preview/preview.html)

See exactly how your code will look before installing!

## ✨ What Makes It Special?

### 🎨 **Clean Design**
- No visual noise or distracting colors
- Each color has a clear purpose
- Consistent and predictable highlighting

### 👁️ **Easy on Your Eyes**
- High contrast ratios (your eyes will thank you)
- Perfect for long coding sessions
- Works great in bright rooms and on projectors

### 🎯 **Smart Color Choices**
| What | Color | Why |
|------|-------|-----|
| Keywords (`function`, `if`) | 🔴 Red | Important syntax stands out |
| Strings (`"hello"`) | 🟢 Green | Easy to spot text content |
| Numbers (`42`, `3.14`) | 🟠 Orange | Data values are clear |
| Functions (`myFunction()`) | 🔵 Blue | Method calls are obvious |
| Comments (`// notes`) | ⚫ Gray | Subtle, won't distract |

## 🚀 How to Use It

### Step 1: Download
1. Go to [Releases](https://github.com/donghao1393/vscode-accessible-light-theme/releases)
2. Download the latest `.vsix` file

### Step 2: Install
1. Open VS Code
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
3. Type "Extensions: Install from VSIX"
4. Select the downloaded `.vsix` file

### Step 3: Activate  
1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
2. Type "Preferences: Color Theme"  
3. Choose "Accessible Light"

**That's it!** Your code should now look clean and readable.

## 🔧 Make It Even Better (Optional)

Want to get the most out of this theme? Add these settings to VS Code:

1. **Open Settings**: Press `Ctrl+,` (or `Cmd+,` on Mac)
2. **Click the file icon** in the top-right corner (opens settings.json)
3. **Add these lines**:

```json
{
  "editor.bracketPairColorization.enabled": true,
  "editor.guides.bracketPairs": "active",
  "editor.fontLigatures": true,
  "editor.renderWhitespace": "boundary",
  "editor.rulers": [80, 120],
  "terminal.integrated.minimumContrastRatio": 4.5,
  "workbench.colorCustomizations": {
    "[Accessible Light]": {
      "terminal.background": "#fdfdfd"
    }
  }
}
```

**What do these do?**
- **Bracket colors**: Matching brackets get the same color (easier to spot)
- **Bracket guides**: Shows lines connecting matching brackets
- **Font ligatures**: Makes symbols like `=>` and `!=` look prettier
- **Show spaces**: Helps you spot extra spaces and indentation
- **Rulers**: Vertical lines at 80 and 120 characters (coding guidelines)
- **Terminal contrast**: Ensures terminal text is always readable
- **Terminal background**: Matches the editor background for consistency

## 🎯 Perfect For

### 👨‍💻 **Daily Coding**
- Clean enough to focus on your code
- Comfortable for hours of programming
- Colors help you spot different parts quickly

### 📽️ **Presentations & Teaching**  
- High contrast shows up clearly on projectors
- Students can read code from the back of the room
- Professional appearance for demos

### 👥 **Code Reviews**
- Easy to spot different syntax elements
- Reduces eye strain during long review sessions
- Works well on different monitors and lighting

## 🤔 Common Questions

### "How is this different from other light themes?"
Most light themes try to do too much. This one focuses on being **clean and readable**. Every color choice has a purpose.

### "Will this work with my favorite extensions?"
Yes! It's designed to work well with popular extensions like GitLens, Prettier, and ESLint.

### "Can I customize the colors?"
Absolutely! You can override any color in your VS Code settings. Check the [customization guide](https://code.visualstudio.com/docs/getstarted/themes#_customizing-a-color-theme).

### "Does it work for all programming languages?"
Yes, it's designed to work with any language VS Code supports - JavaScript, Python, Go, Rust, you name it.

## 🎨 Want to See More?

- **Color palette details**: Check out the theme file at `themes/accessible-light-theme.json`
- **Report issues**: Found something that looks weird? [Let me know](https://github.com/donghao1393/vscode-accessible-light-theme/issues)
- **Suggest improvements**: Have ideas? Open an issue!

## 📝 The Story

I got tired of switching between ugly VS Code themes. Some were too bright, others too cluttered, most just looked unprofessional. 

So I made this one: **simple, clean, and easy on the eyes**. 

If you're also tired of visually noisy themes, this might be exactly what you need.

---

**Made by a developer who cares about clean code AND clean design** ✨