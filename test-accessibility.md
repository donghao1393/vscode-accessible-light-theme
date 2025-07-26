# 无障碍主题字体样式测试

这个文件用于测试我们的字体样式改进是否有效。

## 字体样式映射

### 已添加字体样式的元素：

1. **注释** - `italic` (斜体)
   ```javascript
   // 这是一个注释，应该显示为斜体
   /* 多行注释也应该是斜体 */
   ```

2. **字符串** - `italic` (斜体)
   ```javascript
   const message = "这是字符串，应该是绿色斜体";
   const template = `模板字符串也应该是斜体`;
   ```

3. **类型定义** - `underline` (下划线)
   ```typescript
   interface User {  // User 应该有下划线
     name: string;
   }
   class MyClass {  // MyClass 应该有下划线
   }
   ```

4. **常量** - `bold` (粗体)
   ```javascript
   const MAX_SIZE = 100;  // MAX_SIZE 应该是橙色粗体
   const PI = 3.14159;    // PI 应该是橙色粗体
   ```

5. **数字** - `bold` (粗体)
   ```javascript
   let count = 42;        // 42 应该是橙色粗体
   let price = 99.99;     // 99.99 应该是橙色粗体
   ```

6. **关键字** - `bold` (粗体)
   ```javascript
   function test() {      // function 应该是红色粗体
     if (true) {          // if 应该是红色粗体
       return false;      // return 应该是红色粗体
     }
   }
   ```

7. **函数名** - `bold` (粗体)
   ```javascript
   function myFunction() {}  // myFunction 应该是蓝色粗体
   const arrow = () => {};   // arrow 应该是蓝色粗体
   ```

8. **变量** - `italic` (斜体)
   ```javascript
   let userName = "John";    // userName 应该是红色斜体
   var oldStyle = true;      // oldStyle 应该是红色斜体
   ```

9. **支持函数** - `italic` (斜体)
   ```javascript
   console.log("test");      // console.log 应该是绿色斜体
   Math.random();            // Math.random 应该是绿色斜体
   ```

10. **属性名** - `italic` (斜体)
    ```html
    <div class="container">   <!-- class 应该是橙色斜体 -->
    <img src="image.jpg">     <!-- src 应该是橙色斜体 -->
    ```

## 色盲友好性测试

这些字体样式组合应该帮助色盲用户区分不同的语法元素：

- **红色关键字** + 粗体 vs **红色变量** + 斜体
- **绿色字符串** + 斜体 vs **绿色支持函数** + 斜体  
- **橙色数字** + 粗体 vs **橙色类型** + 下划线 vs **橙色属性** + 斜体

即使颜色难以区分，字体样式也能提供额外的视觉提示。
