# Markdown Crash Course

What is markdown?
- Lightweight markup language with a plain text formatting syntax
- Can be converted into HTML/XHTML and other formats
- It's main purpose is readability and ease of use

Used for:
- README files and documentations
- Forum and Blog Posts
- Static Site Generators

Write markdown in any text editor, but nice to have preview(eg: VS Code with extensions)

<!-- Headings -->
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

<!-- Italics -->
*This text* is italics<br>
_This text_ is italics

<!-- Strong -->
**This text** is strong<br>
__This text__ is strong

<!-- Strikethrough -->
~~This text~~ is strikethrough

<!-- Horizontal Rule -->
---
___

<!-- Escape char -->
\*This text\* is not italics

<!-- Blockquote -->
> This is a quote

<!-- Links -->
[Link Text](https://google.com) <br>
[Link Text](https://google.com "Link Hover Title")

<!-- Unordered List -->
* Item 1
* Item 2
	* Nested Item 1

<!-- Ordered List -->
1. Item 1
1. Item 2

<!-- Inline Code Block -->
`<p> This is in an inline code block</p>`

<!-- Images -->
![Image Name](https://markdown-here/img/icon256.png)

<!-- Github Markdown -->

<!-- Code Blocks -->
```bash
npm install
npm start
```

```javascript
function add(num1, num2) {
	return num1 + num2;
}
```

```python
def add(num1, num2):
    return num1 + num2
```

<!-- Tables -->
| Name   | Email   |
|--------| ------- |
| John | j@x.com |
| Jane | jane@y.com |

<!-- Task Lists -->
* [x] Complete Task
* [ ] Incomplete Task