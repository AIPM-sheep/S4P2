from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许所有来源的跨域请求

# ==================================================
# 我们的“假数据库”
# ==================================================
mock_db = {
    "web-full-stack": {
        "roadmap_title": "Web 全栈开发者",
        "stages": [
            # --- 主干道技能 ---
            {
                "step": 1,
                "skill": "HTML",
                "prerequisites": [],
                "resources": [
                    {
                        "resource_name": "MDN Web Docs – HTML",
                        "resource_url": "[https://developer.mozilla.org/zh-CN/docs/Web/HTML](https://developer.mozilla.org/zh-CN/docs/Web/HTML)",
                        "resource_type": "官方文档",
                        "reason": "Mozilla官方教程，内容全面更新，提供面向新手的HTML基础引导"
                    },
                    {
                        "resource_name": "编程狮(W3Cschool) – HTML 教程",
                        "resource_url": "[https://www.w3cschool.cn/html/](https://www.w3cschool.cn/html/)",
                        "resource_type": "文字教程",
                        "reason": "国内知名中文教程，讲解直观易懂，提供大量交互示例和练习"
                    },
                    {
                        "resource_name": "慕课网-《初识HTML5+CSS3》课程",
                        "resource_url": "[https://www.imooc.com/learn/9](https://www.imooc.com/learn/9)",
                        "resource_type": "免费视频课程",
                        "reason": "免费入门级视频课程，零基础讲解HTML和CSS，每课配小案例实战"
                    },
                    {
                        "resource_name": "Learn HTML.org 互动教程",
                        "resource_url": "[https://www.learn-html.org/](https://www.learn-html.org/)",
                        "resource_type": "互动式教程",
                        "reason": "完全免费的互动式学习平台，让学习者边写边学，快速掌握HTML核心概念"
                    },
                    {
                        "resource_name": "web.dev 学习 HTML",
                        "resource_url": "[https://web.dev/learn/html](https://web.dev/learn/html)",
                        "resource_type": "文字教程",
                        "reason": "Google出品的现代HTML教程，注重实用性和语义化，内容新颖且实战导向"
                    },
                    {
                        "resource_name": "freeCodeCamp: Responsive Web Design Certification",
                        "resource_url": "[https://www.freecodecamp.org/learn/2022/responsive-web-design/](https://www.freecodecamp.org/learn/2022/responsive-web-design/)",
                        "resource_type": "互动式教程, 实战项目",
                        "reason": "通过从零开始构建五个真实项目，将HTML理论知识即时转化为动手实践"
                    },
                    {
                        "resource_name": "freeCodeCamp HTML 完整教程",
                        "resource_url": "[https://www.youtube.com/watch?v=kUMe1FH4CHE](https://www.youtube.com/watch?v=kUMe1FH4CHE)",
                        "resource_type": "视频课程",
                        "reason": "超过3小时的完整HTML5教程，包含10个实践章节和项目实战，完全免费且广受好评"
                    },
                    {
                        "resource_name": "HTML Interactive Exercises",
                        "resource_url": "[https://breatheco.de/interactive-exercise/html-exercises](https://breatheco.de/interactive-exercise/html-exercises)",
                        "resource_type": "互动式教程",
                        "reason": "提供逐步引导的交互式练习环境，让学习者通过实际编码掌握HTML标签和语义化"
                    }
                ]
            },
            {
                "step": 2,
                "skill": "CSS",
                "prerequisites": ["HTML"],
                "resources": [
                    {
                        "resource_name": "MDN Web Docs - CSS",
                        "resource_url": "[https://developer.mozilla.org/zh-CN/docs/Web/CSS](https://developer.mozilla.org/zh-CN/docs/Web/CSS)",
                        "resource_type": "官方文档",
                        "reason": "权威教程，从基础原理、语法到现代布局全面覆盖，新手友好"
                    },
                    {
                        "resource_name": "菜鸟教程- CSS 教程",
                        "resource_url": "[http://www.runoob.com/css/css-tutorial.html](http://www.runoob.com/css/css-tutorial.html)",
                        "resource_type": "文字教程",
                        "reason": "中文教程，内容简洁清晰，涵盖选择器、盒模型、布局等，拥有数百在线示例"
                    },
                    {
                        "resource_name": "编程狮(W3Cschool) – CSS 教程",
                        "resource_url": "[https://m.w3cschool.cn/css/](https://m.w3cschool.cn/css/)",
                        "resource_type": "文字教程",
                        "reason": "免费中文教程，详细介绍各种样式应用，配有在线代码编辑器和上百实战案例"
                    },
                    {
                        "resource_name": "CSS-Tricks Complete Guide to Flexbox",
                        "resource_url": "[https://css-tricks.com/snippets/css/a-guide-to-flexbox/](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)",
                        "resource_type": "文字教程",
                        "reason": "业界公认最全面的Flexbox指南，配有可视化图解和实用代码示例，2024年持续更新"
                    },
                    {
                        "resource_name": "Josh Comeau 的互动 Flexbox 指南",
                        "resource_url": "[https://www.joshwcomeau.com/css/interactive-guide-to-flexbox/](https://www.joshwcomeau.com/css/interactive-guide-to-flexbox/)",
                        "resource_type": "互动式教程",
                        "reason": "顶级前端专家制作的互动教程，通过动画演示深入理解Flexbox工作原理"
                    },
                    {
                        "resource_name": "CSS-Tricks Complete Guide to Grid",
                        "resource_url": "[https://css-tricks.com/snippets/css/complete-guide-grid/](https://css-tricks.com/snippets/css/complete-guide-grid/)",
                        "resource_type": "文字教程",
                        "reason": "CSS Grid的权威指南，详尽的属性说明配合实例，是掌握现代布局的必备资源"
                    },
                    {
                        "resource_name": "An Interactive Guide to CSS Grid",
                        "resource_url": "[https://www.joshwcomeau.com/css/interactive-guide-to-grid/](https://www.joshwcomeau.com/css/interactive-guide-to-grid/)",
                        "resource_type": "互动式教程, 文字教程",
                        "reason": "通过高质量的交互式示例和清晰的心理模型，将复杂的CSS Grid概念解释得极其直观易懂"
                    },
                    {
                        "resource_name": "CSS-Tricks 完整指南",
                        "resource_url": "[https://css-tricks.com/](https://css-tricks.com/)",
                        "resource_type": "文字教程",
                        "reason": "业界最受欢迎的CSS资源网站，提供丰富的实例代码和最新的CSS技术文章"
                    },
                    {
                        "resource_name": "Kevin Powell CSS 频道",
                        "resource_url": "[https://www.youtube.com/channel/UCJZv4d5rbIKd4QHMPkcABCw](https://www.youtube.com/channel/UCJZv4d5rbIKd4QHMPkcABCw)",
                        "resource_type": "视频课程",
                        "reason": "被誉为“CSS之王”的Kevin Powell制作的高质量教学视频，深受开发者社区喜爱"
                    },
                    {
                        "resource_name": "Flexbox Froggy",
                        "resource_url": "[https://flexboxfroggy.com/](https://flexboxfroggy.com/)",
                        "resource_type": "互动式教程",
                        "reason": "通过有趣的游戏方式学习CSS Flexbox布局，寓教于乐且效果显著"
                    }
                ]
            },
            {
                "step": 3,
                "skill": "JavaScript",
                "prerequisites": ["HTML", "CSS"],
                "resources": [
                    {
                        "resource_name": "MDN Web Docs – JavaScript 指南",
                        "resource_url": "[https://developer.mozilla.org/zh-CN/docs/Learn_web_development/Getting_started/Your_first_website/Adding_interactivity](https://developer.mozilla.org/zh-CN/docs/Learn_web_development/Getting_started/Your_first_website/Adding_interactivity)",
                        "resource_type": "教程",
                        "reason": "Mozilla官方教程，新手友好，介绍现代JavaScript基础语法、DOM操作、异步编程等内容"
                    },
                    {
                        "resource_name": "编程狮(W3Cschool) – JavaScript 教程",
                        "resource_url": "[https://www.w3cschool.cn/article/22792294.html](https://www.w3cschool.cn/article/22792294.html)",
                        "resource_type": "文字教程",
                        "reason": "系统讲解JS语法与DOM，语句易懂全面，包括回调、Promise等异步特性，拥有大量交互示例"
                    },
                    {
                        "resource_name": "JavaScript.info",
                        "resource_url": "[https://javascript.info/](https://javascript.info/)",
                        "resource_type": "文字教程, 类官方文档",
                        "reason": "涵盖现代JavaScript的免费在线教程，内容新颖完整，配有互动示例和实战练习"
                    },
                    {
                        "resource_name": "Eloquent JavaScript (在线免费版)",
                        "resource_url": "[https://eloquentjavascript.net/](https://eloquentjavascript.net/)",
                        "resource_type": "文字教程, 书籍, 实战项目",
                        "reason": "经典JavaScript学习书籍的免费在线版，理论与实践并重，配有大量练习题"
                    },
                    {
                        "resource_name": "JavaScript30 - 30天原生JS挑战",
                        "resource_url": "[https://javascript30.com/](https://javascript30.com/)",
                        "resource_type": "实战项目",
                        "reason": "Wes Bos出品的30个纯JavaScript项目，完全免费，强化DOM操作和实战能力"
                    },
                    {
                        "resource_name": "The Modern JavaScript Tutorial",
                        "resource_url": "[https://javascript.info](https://javascript.info)",
                        "resource_type": "文字教程, 类官方文档",
                        "reason": "当代最全面、结构最清晰、内容最深入的JavaScript在线教程，是构建扎实JS知识体系的首选"
                    },
                    {
                        "resource_name": "freeCodeCamp: JavaScript Full Course",
                        "resource_url": "[https://www.youtube.com/watch?v=PkZNo7MFNFG](https://www.youtube.com/watch?v=PkZNo7MFNFG)",
                        "resource_type": "视频课程, 互动式教程",
                        "reason": "专为视觉学习者设计，通过视频形式系统讲解JS核心概念，并包含大量小型实践项目"
                    },
                    {
                        "resource_name": "JavaScript DOM 操作教程",
                        "resource_url": "[https://www.youtube.com/watch?v=jlyBx0Yh4rl](https://www.youtube.com/watch?v=jlyBx0Yh4rl)",
                        "resource_type": "视频课程",
                        "reason": "1小时完整的DOM操作实战教程，包含事件处理、动画和实际项目演示"
                    },
                    {
                        "resource_name": "W3Schools JavaScript ES6",
                        "resource_url": "[https://www.w3schools.com/js/js_es6.asp](https://www.w3schools.com/js/js_es6.asp)",
                        "resource_type": "互动式教程",
                        "reason": "系统性介绍ES6+新特性，提供在线编辑器即时练习，适合初学者掌握现代JavaScript"
                    }
                ]
            },
            {
                "step": 4,
                "skill": "React.js",
                "prerequisites": ["HTML", "CSS", "JavaScript"],
                "resources": [
                    {
                        "resource_name": "React 官方文档",
                        "resource_url": "[https://zh-hans.react.dev/](https://zh-hans.react.dev/)",
                        "resource_type": "官方文档",
                        "reason": "由React团队维护的权威教程，全面讲解组件、Hooks、路由等关键概念，具有中文版"
                    },
                    {
                        "resource_name": "菜鸟教程 - React 教程",
                        "resource_url": "[http://www.runoob.com/react/react-tutorial.html](http://www.runoob.com/react/react-tutorial.html)",
                        "resource_type": "文字教程",
                        "reason": "中文基础教程，介绍React核心特性，可在线编辑示例代码并即时查看效果"
                    },
                    {
                        "resource_name": "Scrimba - Learn React 免费课程",
                        "resource_url": "[https://v1.scrimba.com/playlist/p7P5Hd](https://v1.scrimba.com/playlist/p7P5Hd)",
                        "resource_type": "互动式教程",
                        "reason": "交互式视频课程，包含59个互动单元，通过实战项目掌握React基础与进阶用法"
                    },
                    {
                        "resource_name": "React 官方教程",
                        "resource_url": "[https://react.dev/learn](https://react.dev/learn)",
                        "resource_type": "官方文档",
                        "reason": "React官方新版教程，从零开始讲解现代React，权威且最新"
                    },
                    {
                        "resource_name": "Full Stack Open - React 部分",
                        "resource_url": "[https://fullstackopen.com/en/](https://fullstackopen.com/en/)",
                        "resource_type": "文字教程",
                        "reason": "赫尔辛基大学出品的免费全栈课程，React部分内容深入且配有大量实战练习"
                    },
                    {
                        "resource_name": "React 实战项目教程",
                        "resource_url": "[https://github.com/gopinav/React-Tutorials](https://github.com/gopinav/React-Tutorials)",
                        "resource_type": "实战项目",
                        "reason": "GitHub上星级很高的React项目合集，从简单组件到完整应用，代码清晰易懂"
                    },
                    {
                        "resource_name": "React.dev - Learn React",
                        "resource_url": "[https://react.dev/learn](https://react.dev/learn)",
                        "resource_type": "官方文档, 互动式教程",
                        "reason": "全新改版的React官方文档本身就是一套顶级的互动式课程，是学习现代React最权威的起点"
                    },
                    {
                        "resource_name": "Scrimba: Learn React for Free",
                        "resource_url": "[https://scrimba.com/learn/learnreact](https://scrimba.com/learn/learnreact)",
                        "resource_type": "视频课程, 互动式教程",
                        "reason": "由金牌讲师Bob Ziroll主讲，通过构建多个真实有趣的项目，将React概念融会贯通"
                    },
                    {
                        "resource_name": "Full Stack Open",
                        "resource_url": "[https://fullstackopen.com/en/](https://fullstackopen.com/en/)",
                        "resource_type": "文字教程, 实战项目",
                        "reason": "由赫尔辛基大学出品的免费顶级课程，其React部分以极其深入和实践的方式，引导学生构建完整应用"
                    },
                    {
                        "resource_name": "React 2024 完整初学者教程",
                        "resource_url": "[https://www.youtube.com/watch?v=x4rFhThSX04](https://www.youtube.com/watch?v=x4rFhThSX04)",
                        "resource_type": "视频课程",
                        "reason": "2024年最新的React教程，通过实际项目学习组件、状态管理和现代React开发"
                    },
                    {
                        "resource_name": "W3Schools React 教程",
                        "resource_url": "[https://www.w3schools.com/REACT/DEFAULT.ASP](https://www.w3schools.com/REACT/DEFAULT.ASP)",
                        "resource_type": "互动式教程",
                        "reason": "提供在线编辑器的交互式学习环境，适合初学者理解React组件化思想"
                    }
                ]
            },
             {
                "step": 5,
                "skill": "Node.js & Express.js",
                "prerequisites": ["JavaScript"],
                "resources": [
                    {
                        "resource_name": "Node.js 官方文档",
                        "resource_url": "[https://nodejs.org/en/docs/](https://nodejs.org/en/docs/)",
                        "resource_type": "官方文档",
                        "reason": "Node.js官方权威文档，涵盖所有核心模块和API，是学习服务器端JS的必备参考"
                    },
                    {
                        "resource_name": "Express 官方文档",
                        "resource_url": "[https://expressjs.com/zh-cn](https://expressjs.com/zh-cn)",
                        "resource_type": "官方文档",
                        "reason": "官方指南提供详尽示例，介绍Express核心功能和中间件用法，支持多语言"
                    },
                    {
                        "resource_name": "菜鸟教程 - Node.js 教程",
                        "resource_url": "[http://www.runoob.com/nodejs/nodejs-tutorial.html](http://www.runoob.com/nodejs/nodejs-tutorial.html)",
                        "resource_type": "文字教程",
                        "reason": "简明介绍Node.js平台与特点，新手友好地阐述事件驱动架构和高性能优势"
                    },
                    {
                        "resource_name": "廖雪峰 - Node.js 入门",
                        "resource_url": "[https://liaoxuefeng.com/books/javascript/nodejs/index.html](https://liaoxuefeng.com/books/javascript/nodejs/index.html)",
                        "resource_type": "文字教程",
                        "reason": "专业教程第三部分“Node.js”，从安装到模块化开发全流程讲解，通过案例展示为何“Node.js将JS带入后端”"
                    },
                    {
                        "resource_name": "Node.js Design Patterns 在线版",
                        "resource_url": "[https://github.com/PacktPublishing/Node.js-Design-Patterns-Third-Edition](https://github.com/PacktPublishing/Node.js-Design-Patterns-Third-Edition)",
                        "resource_type": "文字教程",
                        "reason": "深入讲解Node.js核心概念和设计模式，GitHub开源版本，适合进阶学习"
                    },
                    {
                        "resource_name": "NodeSchool 互动学习",
                        "resource_url": "[https://nodeschool.io/](https://nodeschool.io/)",
                        "resource_type": "互动式教程",
                        "reason": "通过命令行互动学习Node.js，边做边学的方式掌握异步编程和核心模块"
                    },
                    {
                        "resource_name": "Node.js 2024 完整课程",
                        "resource_url": "[https://www.youtube.com/watch?v=32M1al-Y6Ag](https://www.youtube.com/watch?v=32M1al-Y6Ag)",
                        "resource_type": "视频课程",
                        "reason": "Traversy Media制作的2024年最新Node.js教程，涵盖核心模块和服务器开发实战"
                    },
                    {
                        "resource_name": "W3Schools Node.js 教程",
                        "resource_url": "[https://www.w3schools.com/nodejs/](https://www.w3schools.com/nodejs/)",
                        "resource_type": "互动式教程",
                        "reason": "提供在线编辑器的Node.js学习环境，适合初学者掌握服务器端JavaScript开发"
                    },
                    {
                        "resource_name": "MDN 学习区 - Express/Node 入门教程",
                        "resource_url": "[https://developer.mozilla.org/zh-CN/docs/Learn/web_development/Extensions/Server-side/Express_Nodejs/Introduction](https://developer.mozilla.org/zh-CN/docs/Learn/web_development/Extensions/Server-side/Express_Nodejs/Introduction)",
                        "resource_type": "文字教程",
                        "reason": "Mozilla提供的Express教程，从Node、Express基础到REST API构建，内容清晰有条理"
                    },
                    {
                        "resource_name": "Express.js 官方指南",
                        "resource_url": "[https://expressjs.com/en/guide/routing.html](https://expressjs.com/en/guide/routing.html)",
                        "resource_type": "官方文档",
                        "reason": "Express官方完整指南，从路由到中间件的权威教程，代码示例丰富"
                    },
                    {
                        "resource_name": "REST API 实战教程",
                        "resource_url": "[https://github.com/hagopj13/node-express-boilerplate](https://github.com/hagopj13/node-express-boilerplate)",
                        "resource_type": "实战项目",
                        "reason": "GitHub高星级的Express项目模板，展示了完整的REST API最佳实践和项目结构"
                    },
                    {
                        "resource_name": "Express.js 完整教程系列",
                        "resource_url": "[https://github.com/microsoft/nodejs-guidelines](https://github.com/microsoft/nodejs-guidelines)",
                        "resource_type": "文字教程",
                        "reason": "微软出品的Node.js开发指南，包含Express最佳实践和企业级开发规范"
                    },
                    {
                        "resource_name": "MDN Web Docs: Express/Node.js Introduction",
                        "resource_url": "[https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/Introduction](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/Introduction)",
                        "resource_type": "文字教程, 类官方文档",
                        "reason": "在动手编码前，提供了对Node.js和Express核心概念最全面、最清晰的理论解释"
                    },
                    {
                        "resource_name": "freeCodeCamp: Node.js and Express.js - Full Course",
                        "resource_url": "[https://www.youtube.com/watch?v=Oe421EPjeBE](https://www.youtube.com/watch?v=Oe421EPjeBE)",
                        "resource_type": "视频课程, 实战项目",
                        "reason": "一个非常实用的代码跟随视频教程，完整演示了从零搭建一个Express服务器的过程"
                    },
                    {
                        "resource_name": "Express 2024 速成课程",
                        "resource_url": "[https://www.youtube.com/watch?v=CnH3kAXSrmU](https://www.youtube.com/watch?v=CnH3kAXSrmU)",
                        "resource_type": "视频课程",
                        "reason": "Traversy Media制作的1.5小时Express速成教程，涵盖路由、中间件和API开发"
                    },
                    {
                        "resource_name": "Codecademy Learn Express",
                        "resource_url": "[https://www.codecademy.com/learn/learn-express](https://www.codecademy.com/learn/learn-express)",
                        "resource_type": "互动式教程",
                        "reason": "提供交互式编程环境学习Express框架，包含实际项目和CRUD操作练习"
                    }
                ]
            },
            # --- 独立技能 (可以在任何时候学习) ---
            {
                "step": None,
                "skill": "Git & GitHub",
                "prerequisites": [],
                "resources": [
                    {
                        "resource_name": "廖雪峰 - Git 教程",
                        "resource_url": "[https://liaoxuefeng.com/books/git/what-is-git/index.html](https://liaoxuefeng.com/books/git/what-is-git/index.html)",
                        "resource_type": "文字教程",
                        "reason": "国内资深作者撰写的免费教程，从概念到命令逐步讲解，风格通俗幽默，社区广泛使用"
                    },
                    {
                        "resource_name": "菜鸟教程 - Git 教程",
                        "resource_url": "[http://www.runoob.com/git/git-tutorial.html](http://www.runoob.com/git/git-tutorial.html)",
                        "resource_type": "文字教程",
                        "reason": "中文入门教程，介绍Git原理与常用命令，内容直观易懂，配有示例操作"
                    },
                    {
                        "resource_name": "Pro Git (中文版)",
                        "resource_url": "[https://www.progit.cn/](https://www.progit.cn/)",
                        "resource_type": "官方文档/书籍",
                        "reason": "由Git社区翻译发布的免费电子书，详尽介绍Git使用与原理，帮助学习者从初学者成长为专家"
                    },
                    {
                        "resource_name": "Pro Git 官方书籍",
                        "resource_url": "[https://git-scm.com/book](https://git-scm.com/book)",
                        "resource_type": "官方文档",
                        "reason": "Git官方权威教程，从入门到精通，有完整中文翻译版本，完全免费"
                    },
                    {
                        "resource_name": "Learn Git Branching 互动教程",
                        "resource_url": "[https://learngitbranching.js.org/](https://learngitbranching.js.org/)",
                        "resource_type": "互动式教程",
                        "reason": "可视化的Git学习工具，通过动画演示分支操作，支持中文，寓教于乐"
                    },
                    {
                        "resource_name": "GitHub Skills",
                        "resource_url": "[https://skills.github.com/](https://skills.github.com/)",
                        "resource_type": "实战项目",
                        "reason": "GitHub官方提供的实践课程，在真实仓库中学习Git和GitHub工作流"
                    },
                    {
                        "resource_name": "GitHub Docs: Hello World",
                        "resource_url": "[https://docs.github.com/en/get-started/quickstart/hello-world](https://docs.github.com/en/get-started/quickstart/hello-world)",
                        "resource_type": "互动式教程, 官方文档",
                        "reason": "无需安装任何软件，通过纯网页操作，完美地介绍了GitHub协作流程的核心概念"
                    },
                    {
                        "resource_name": "freeCodeCamp: Git and GitHub for Beginners - Crash Course",
                        "resource_url": "[https://www.youtube.com/watch?v=RGOj5yH7evk](https://www.youtube.com/watch?v=RGOj5yH7evk)",
                        "resource_type": "视频课程",
                        "reason": "作为一部引导式教程，它将GitHub的概念与本地的命令行实践连接起来，完整演示了从创建项目到发起Pull Request的全过程"
                    },
                    {
                        "resource_name": "Git 官方文档",
                        "resource_url": "[https://git-scm.com/doc](https://git-scm.com/doc)",
                        "resource_type": "官方文档",
                        "reason": "Git官方维护的权威文档，提供完整的命令参考和最佳实践指导"
                    },
                    {
                        "resource_name": "Git 和 GitHub 2024 完整教程",
                        "resource_url": "[https://www.youtube.com/watch?v=l2yrJtwoC_E](https://www.youtube.com/watch?v=l2yrJtwoC_E)",
                        "resource_type": "视频课程",
                        "reason": "近2小时的2024年最新教程，涵盖Git基础到高级操作和GitHub协作流程"
                    },
                    {
                        "resource_name": "GitHub Learning Lab",
                        "resource_url": "[https://lab.github.com/](https://lab.github.com/)",
                        "resource_type": "互动式教程",
                        "reason": "GitHub官方提供的实践课程，通过真实项目学习Git和GitHub工作流程"
                    }
                ]
            },
            {
                "step": None,
                "skill": "SQL",
                "prerequisites": [],
                "resources": [
                    {
                        "resource_name": "菜鸟教程- SQL 教程",
                        "resource_url": "[http://www.runoob.com/sql/sql-tutorial.html](http://www.runoob.com/sql/sql-tutorial.html)",
                        "resource_type": "文字教程",
                        "reason": "标准化SQL语言教程，系统介绍关系型数据库基础操作，包含众多例子，新手易上手"
                    },
                    {
                        "resource_name": "树懒学堂 - SQL 教程",
                        "resource_url": "[https://www.shulanxt.com/database/sql/sql-tutorial](https://www.shulanxt.com/database/sql/sql-tutorial)",
                        "resource_type": "文字教程",
                        "reason": "中文SQL学习资源，覆盖数据库操作核心语句，每章配实际使用示例，帮助巩固CRUD概念"
                    },
                    {
                        "resource_name": "SQLZoo - 交互式教程",
                        "resource_url": "[https://sqlzoo.net/wiki/SQL_Tutorial](https://sqlzoo.net/wiki/SQL_Tutorial)",
                        "resource_type": "互动式教程",
                        "reason": "免费在线学习平台，通过逐步练习和实时反馈掌握SQL，配有练习题和测验"
                    },
                    {
                        "resource_name": "SQLBolt 互动 SQL 教程",
                        "resource_url": "[https://sqlbolt.com/](https://sqlbolt.com/)",
                        "resource_type": "互动式教程",
                        "reason": "界面极其简洁，通过一系列“先学后练”的交互式课程，让初学者在浏览器中直接编写和执行SQL查询"
                    },
                    {
                        "resource_name": "W3Schools SQL 教程",
                        "resource_url": "[https://www.w3schools.com/sql/](https://www.w3schools.com/sql/)",
                        "resource_type": "文字教程",
                        "reason": "结构化的SQL基础教程，配有在线编辑器，可以直接运行SQL语句练习"
                    },
                    {
                        "resource_name": "SQL Murder Mystery",
                        "resource_url": "[https://mystery.knightlab.com/](https://mystery.knightlab.com/)",
                        "resource_type": "互动式教程",
                        "reason": "通过破案游戏学习SQL查询，寓教于乐的方式掌握复杂的JOIN和聚合查询"
                    },
                    {
                        "resource_name": "Mode: The SQL Tutorial for Data Analysis",
                        "resource_url": "[https://mode.com/sql-tutorial/](https://mode.com/sql-tutorial/)",
                        "resource_type": "文字教程",
                        "reason": "一套非常全面、结构化的文本教程，在数据分析的背景下讲解SQL，提供了更深入的概念解释"
                    },
                    {
                        "resource_name": "W3Schools SQL 教程",
                        "resource_url": "[https://www.w3schools.com/sql/](https://www.w3schools.com/sql/)",
                        "resource_type": "互动式教程",
                        "reason": "提供在线SQL编辑器的完整教程，涵盖所有主流数据库系统，适合初学者掌握CRUD操作"
                    },
                    {
                        "resource_name": "SQLBolt 交互式课程",
                        "resource_url": "[https://sqlbolt.com/](https://sqlbolt.com/)",
                        "resource_type": "互动式教程",
                        "reason": "广受开发者推荐的免费SQL学习平台，通过实际数据库练习掌握查询技能"
                    },
                    {
                        "resource_name": "Mode Analytics SQL 教程",
                        "resource_url": "[https://mode.com/sql-tutorial/](https://mode.com/sql-tutorial/)",
                        "resource_type": "文字教程",
                        "reason": "专为数据分析设计的SQL教程，提供真实数据集和实际业务场景的查询练习"
                    }
                ]
            }
        ]
    },
    "ai-agent-engineer": {
        "roadmap_title": "AI Agent 工程师",
        "stages": [
            # Stage 1 - 基础准备
            {
                "step": 1,
                "skill": "精通 Python 编程",
                "prerequisites": [],
                "resources": [
                    {
                        "resource_name": "Python 官方文档 - asyncio",
                        "resource_url": "[https://docs.python.org/3/library/asyncio.html](https://docs.python.org/3/library/asyncio.html)",
                        "resource_type": "官方文档",
                        "reason": "最权威、最全面的第一手资料，定义了async/await，是理解所有异步框架的基础。"
                    },
                    {
                        "resource_name": "ArjanCodes - \"A Complete Guide to Async/Await in Python\"",
                        "resource_url": "[https://www.youtube.com/watch?v=16w3F22_18s](https://www.youtube.com/watch?v=16w3F22_18s)",
                        "resource_type": "视频课程",
                        "reason": "质量极高的视频教程，通过重构实战，让你直观感受异步编程带来的性能提升。"
                    }
                ]
            },
            {
                "step": 1,
                "skill": "软件工程与 API 基础",
                "prerequisites": ["精通 Python 编程"],
                "resources": [
                    {
                        "resource_name": "FastAPI 官方文档 - 入门教程",
                        "resource_url": "[https://fastapi.tiangolo.com/tutorial/](https://fastapi.tiangolo.com/tutorial/)",
                        "resource_type": "官方教程",
                        "reason": "业界标杆级的交互式教程，让你在学习中即时获得一个带自动化文档的高性能API。"
                    },
                    {
                        "resource_name": "freeCodeCamp - \"FastAPI Course for Beginners\"",
                        "resource_url": "[https://www.youtube.com/watch?v=7t2alSnE2-I](https://www.youtube.com/watch?v=7t2alSnE2-I)",
                        "resource_type": "视频课程",
                        "reason": "完整的项目视频课程，手把手带你完成从零到一的搭建、测试和部署，快速建立全局观。"
                    }
                ]
            },

            # Stage 2 - LLM 核心交互
            {
                "step": 2,
                "skill": "LLM 理论入门",
                "prerequisites": ["精通 Python 编程"],
                "resources": [
                    {
                        "resource_name": "Jay Alammar - \"The Illustrated Transformer\"",
                        "resource_url": "[https://jalammar.github.io/illustrated-transformer/](https://jalammar.github.io/illustrated-transformer/)",
                        "resource_type": "深度文章",
                        "reason": "无法被超越的经典，用极其直观的动图和比喻解释了复杂的Attention机制，入门必读。"
                    },
                    {
                        "resource_name": "3Blue1Brown - \"Attention in Transformers, visually explained\"",
                        "resource_url": "[https://www.youtube.com/watch?v=mMa20_sJ4IU](https://www.youtube.com/watch?v=mMa20_sJ4IU)",
                        "resource_type": "视频课程",
                        "reason": "从数学思想的层面，让你对Attention机制的巧妙之处建立深刻的科学直觉。"
                    }
                ]
            },
            {
                "step": 2,
                "skill": "高级提示工程",
                "prerequisites": ["LLM 理论入门"],
                "resources": [
                    {
                        "resource_name": "OpenAI - \"Function calling\" 官方文档",
                        "resource_url": "[https://platform.openai.com/docs/guides/function-calling](https://platform.openai.com/docs/guides/function-calling)",
                        "resource_type": "官方文档",
                        "reason": "理解模型原生的工具调用能力，是掌握现代Agent框架底层逻辑的关键一步。"
                    },
                    {
                        "resource_name": "\"Let's build the GPT-4 function calling API from scratch\" by AI Jason",
                        "resource_url": "[https://www.youtube.com/watch?v=tjYo4jU-i-s](https://www.youtube.com/watch?v=tjYo4jU-i-s)",
                        "resource_type": "视频课程",
                        "reason": "带你手写一个函数调用调度器，让你彻底告别“黑箱API调用者”的身份，理解其核心原理。"
                    }
                ]
            },

            # Stage 3 - 构建第一个Agent
            {
                "step": 3,
                "skill": "Agentic 框架入门 (LangChain)",
                "prerequisites": ["高级提示工程"],
                "resources": [
                    {
                        "resource_name": "LangChain 官方教程 - \"Build an Agent\"",
                        "resource_url": "[https://python.langchain.com/docs/tutorials/agents](https://python.langchain.com/docs/tutorials/agents)",
                        "resource_type": "官方教程",
                        "reason": "学习任何框架，官方的“Get Started”教程永远是第一选择，确保你使用的是最新的实践方式。"
                    },
                    {
                        "resource_name": "James Briggs - \"Code a LangChain Agent From Scratch\"",
                        "resource_url": "[https://www.youtube.com/watch?v=2y_uB1wK-e8](https://www.youtube.com/watch?v=2y_uB1wK-e8)",
                        "resource_type": "视频课程",
                        "reason": "通过“手搓”一个迷你版的Agent循环，能让你对框架的抽象（如AgentExecutor）有更深刻的体感。"
                    }
                ]
            },
            {
                "step": 3,
                "skill": "掌握核心 Agent 模式 (ReAct)",
                "prerequisites": ["Agentic 框架入门 (LangChain)"],
                "resources": [
                    {
                        "resource_name": "ReAct 论文官方实现",
                        "resource_url": "[https://github.com/ysymyth/ReAct](https://github.com/ysymyth/ReAct)",
                        "resource_type": "开源项目",
                        "reason": "直接运行论文作者的<200行最小化实现，剥离所有框架封装，直击ReAct循环的本质。"
                    },
                    {
                        "resource_name": "LangChain - \"Build a ReAct agent from scratch with LangGraph\"",
                        "resource_url": "[https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/)",
                        "resource_type": "官方教程",
                        "reason": "学习LangGraph如何用“图”的思想来工程化地实现ReAct模式，深入理解框架的设计哲学。"
                    }
                ]
            },

            # Stage 4 - 为 Agent 注入知识与记忆
            {
                "step": 4,
                "skill": "向量数据库入门",
                "prerequisites": ["LLM 理论入门"], # 修正：理解向量数据库需要LLM基础，但不依赖于Agent框架
                "resources": [
                    {
                        "resource_name": "FAISS 官方Wiki - \"Guidelines to choose an index\"",
                        "resource_url": "[https://github.com/facebookresearch/faiss/wiki/Guidelines-to-choose-an-index](https://github.com/facebookresearch/faiss/wiki/Guidelines-to-choose-an-index)",
                        "resource_type": "官方文档",
                        "reason": "压榨检索性能的“优化圣经”，指导你在不同数据规模下选择最优索引，实现毫秒级检索。"
                    },
                    {
                        "resource_name": "ChromaDB 官方博客 - \"Scaling Chroma: A Technical Deep Dive\"",
                        "resource_url": "[https://www.trychroma.com/blog/scaling-chroma](https://www.trychroma.com/blog/scaling-chroma)",
                        "resource_type": "深度文章",
                        "reason": "讲解ChromaDB的架构以及如何进行横向扩展，是向量数据库从“单机”走向“分布式服务”的蓝图。"
                    }
                ]
            },
            {
                "step": 4,
                "skill": "检索增强生成 (RAG) 全流程",
                "prerequisites": ["向量数据库入门", "掌握核心 Agent 模式 (ReAct)"], # 修正：实现RAG需要数据库和Agent框架知识
                "resources": [
                    {
                        "resource_name": "LlamaIndex 官方文档 - \"RAG Techniques\"",
                        "resource_url": "[https://docs.llamaindex.ai/en/stable/optimizing/production_rag/](https://docs.llamaindex.ai/en/stable/optimizing/production_rag/)",
                        "resource_type": "官方教程",
                        "reason": "RAG优化的“军火库”，详细介绍了分块策略、重排序、多路召回等所有你需要知道的高级技巧。"
                    },
                    {
                        "resource_name": "\"Advanced RAG 01: The RAG Triad\" by AI Jason",
                        "resource_url": "[https://www.youtube.com/watch?v=E2t1_aAayHw](https://www.youtube.com/watch?v=E2t1_aAayHw)",
                        "resource_type": "视频课程",
                        "reason": "用清晰的“RAG三元悖论”来解释RAG评估的核心，并介绍如何系统性地提升RAG质量。"
                    }
                ]
            },

            # Stage 5 - 进阶 Agent
            {
                "step": 5,
                "skill": "状态管理与复杂流 (LangGraph)",
                "prerequisites": ["掌握核心 Agent 模式 (ReAct)"], # 修正：LangGraph是实现复杂Agent流的工具
                "resources": [
                    {
                        "resource_name": "LangGraph 官方文档",
                        "resource_url": "[https://langchain-ai.github.io/langgraph/](https://langchain-ai.github.io/langgraph/)",
                        "resource_type": "官方文档",
                        "reason": "理解LangGraph如何用图（Graph）来定义循环和状态，掌握其作为“状态机”的本质。"
                    },
                    {
                        "resource_name": "Bilibili - \"LangGraph快速入门与智能体开发实战\" by 九天Hector",
                        "resource_url": "[https://www.bilibili.com/video/BV1Kx3CzyE6Q?vd_source=14a017f1942e66549c878a8ddcc8bc2b](https://www.bilibili.com/video/BV1Kx3CzyE6Q?vd_source=14a017f1942e66549c878a8ddcc8bc2b)",
                        "resource_type": "视频教程",
                        "reason": "优秀的中文社区实战教程，从零开始，用中文语境讲解，非常适合国内学习者快速上手。"
                    }
                ]
            },
            {
                "step": 5,
                "skill": "多 Agent 协作 (CrewAI)",
                "prerequisites": ["掌握核心 Agent 模式 (ReAct)"], # 修正：多Agent协作依赖于对单个Agent的理解
                "resources": [
                    {
                        "resource_name": "CrewAI 官方文档 - \"Examples\"",
                        "resource_url": "[https://docs.crewai.com/examples/](https://docs.crewai.com/examples/)",
                        "resource_type": "官方示例",
                        "reason": "官方示例库是最好的学习材料，提供了各种协作模式的即用代码，是快速启动多Agent项目的“模板库”。"
                    },
                    {
                        "resource_name": "GitHub - \"CrewAI Agent Templates\" by joaomdmoura",
                        "resource_url": "[https://github.com/joaomdmoura/crewAI-examples](https://github.com/joaomdmoura/crewAI-examples)",
                        "resource_type": "开源项目",
                        "reason": "直接学习框架作者提供的项目模板，比任何教程都更贴近最佳实践，可直接复用，极大加速开发。"
                    }
                ]
            },

            # Stage 6 - 生产化与部署
            {
                "step": 6,
                "skill": "监控、评估与调试",
                "prerequisites": ["检索增强生成 (RAG) 全流程", "多 Agent 协作 (CrewAI)"],
                "resources": [
                    {
                        "resource_name": "RAGAs: Retrieval-Augmented Generation Assessment",
                        "resource_url": "[https://docs.ragas.io/](https://docs.ragas.io/)",
                        "resource_type": "开源框架",
                        "reason": "提供评估RAG系统性能的量化指标，让你能用数据驱动的方式优化Agent。"
                    },
                    {
                        "resource_name": "LangSmith 官方文档 - \"Automated Evaluation\"",
                        "resource_url": "[https://docs.smith.langchain.com/evaluation/automating](https://docs.smith.langchain.com/evaluation/automating)",
                        "resource_type": "官方教程",
                        "reason": "学习如何创建自定义评估器，在每次代码提交后自动运行评估，是CI/CD的关键一环。"
                    }
                ]
            },
            {
                "step": 6,
                "skill": "安全与伦理",
                "prerequisites": ["监控、评估与调试"],
                "resources": [
                    {
                        "resource_name": "OWASP Top 10 for Large Language Model Applications",
                        "resource_url": "[https://owasp.org/www-project-top-10-for-large-language-model-applications/](https://owasp.org/www-project-top-10-for-large-language-model-applications/)",
                        "resource_type": "行业标准",
                        "reason": "从关注Prompt注入，升级到关注OWASP总结的LLM应用十大安全风险，建立系统性安全思维。"
                    },
                    {
                        "resource_name": "Rebuff.ai - \"The LLM Security Leaderboard\"",
                        "resource_url": "[https://github.com/protectai/rebuff](https://github.com/protectai/rebuff)",
                        "resource_type": "开源工具",
                        "reason": "开源的Prompt注入“蜜罐”和“防火墙”，让你了解当前最新的攻击技术和防御效果。"
                    }
                ]
            }
        ]
    },
    "backend-engineer": {
        "roadmap_title": "后端工程师",
        "stages": [
            {
                "stage_name": "阶段一: 编程与计算机科学基础 (CS & Language Fundamentals)",
                "steps": [
                    {
                        "step": 1,
                        "skill": "Python 高级编程 (OOP, 装饰器)",
                        "prerequisites": [],
                        "resources": [
                            {
                                "resource_name": "Real Python: OOP in Python 3",
                                "resource_url": "[https://realpython.com/python3-object-oriented-programming/](https://realpython.com/python3-object-oriented-programming/)",
                                "resource_type": "深度文章/教程系列",
                                "language": "EN",
                                "reason": "全球公认的高质量教程，用海量代码示例和图解透彻讲解Python OOP。"
                            },
                            {
                                "resource_name": "廖雪峰的Python教程-面向对象高级编程",
                                "resource_url": "[https://www.liaoxuefeng.com/wiki/1016959663602400/1017496031529184](https://www.liaoxuefeng.com/wiki/1016959663602400/1017496031529184)",
                                "resource_type": "中文在线教程",
                                "language": "CN",
                                "reason": "国内广受好评的免费教程，简明扼要，直击Python高级OOP特性的重点。"
                            }
                        ]
                    },
                    {
                        "step": 2,
                        "skill": "数据结构与算法 (Data Structures & Algorithms)",
                        "prerequisites": ["Python 高级编程 (OOP, 装饰器)"],
                        "resources": [
                            {
                                "resource_name": "《Hello 算法》",
                                "resource_url": "[https://github.com/krahets/hello-algo](https://github.com/krahets/hello-algo)",
                                "resource_type": "开源电子书/动画图解",
                                "language": "CN/EN",
                                "reason": "国产优秀开源项目，通过动画图解生动展示算法原理，对国内学习者极其友好。"
                            },
                            {
                                "resource_name": "NeetCode.io",
                                "resource_url": "[https://neetcode.io/](https://neetcode.io/)",
                                "resource_type": "互动教程/刷题平台",
                                "language": "EN",
                                "reason": "LeetCode题目的精华路线图，提供清晰图解和多语言视频题解，实战性极强。"
                            }
                        ]
                    },
                    {
                        "step": 3,
                        "skill": "版本控制 (Git 核心工作流)",
                        "prerequisites": [],
                        "resources": [
                            {
                                "resource_name": "Learn Git Branching",
                                "resource_url": "[https://learngitbranching.js.org/?locale=zh_CN](https://learngitbranching.js.org/?locale=zh_CN)",
                                "resource_type": "互动教程/可视化学习",
                                "language": "EN/CN",
                                "reason": "革命性的可视化学习工具，通过网页虚拟操作，让分支等核心概念变得异常直观。"
                            },
                            {
                                "resource_name": "Pro Git (中文版)",
                                "resource_url": "[https://git-scm.com/book/zh/v2](https://git-scm.com/book/zh/v2)",
                                "resource_type": "官方书籍/权威文档",
                                "language": "CN/EN",
                                "reason": "Git官方权威“圣经”，内容全面、严谨、深入，任何希望精通Git的工程师都应通读。"
                            }
                        ]
                    }
                ]
            },
            {
                "stage_name": "阶段二: API 开发与框架 (API Development & Frameworks)",
                "steps": [
                    {
                        "step": 4,
                        "skill": "RESTful API 设计原则",
                        "prerequisites": [],
                        "resources": [
                            {
                                "resource_name": "Microsoft - RESTful web API design",
                                "resource_url": "[https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design)",
                                "resource_type": "官方最佳实践文档",
                                "language": "EN",
                                "reason": "业界关于RESTful API设计的最佳实践指南之一，构建专业API的必备参考。"
                            },
                            {
                                "resource_name": "阮一峰的网络日志 - RESTful API 设计指南",
                                "resource_url": "[https://www.ruanyifeng.com/blog/2014/05/restful_api.html](https://www.ruanyifeng.com/blog/2014/05/restful_api.html)",
                                "resource_type": "中文博客文章",
                                "language": "CN",
                                "reason": "国内后端开发者的启蒙读物，用通俗易懂的语言快速建立对RESTful风格的理解。"
                            }
                        ]
                    },
                    {
                        "step": 5,
                        "skill": "Web 框架 (FastAPI 或 Flask)",
                        "prerequisites": ["Python 高级编程 (OOP, 装饰器)", "RESTful API 设计原则"],
                        "resources": [
                            {
                                "resource_name": "FastAPI Official Tutorial",
                                "resource_url": "[https://fastapi.tiangolo.com/tutorial/](https://fastapi.tiangolo.com/tutorial/)",
                                "resource_type": "官方文档/互动教程",
                                "language": "EN",
                                "reason": "开源项目文档的典范，手把手教你构建完整API，实战性无出其右。"
                            },
                            {
                                "resource_name": "The Flask Mega-Tutorial by Miguel Grinberg",
                                "resource_url": "[https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)",
                                "resource_type": "博客教程系列",
                                "language": "EN",
                                "reason": "无法绕过的Flask经典教程，带领学习者从零构建一个功能完整的博客应用。"
                            }
                        ]
                    }
                ]
            },
            {
                "stage_name": "阶段三: 数据库技术 (Database Technologies)",
                "steps": [
                    {
                        "step": 6,
                        "skill": "关系型数据库 (PostgreSQL) 与 SQL 进阶",
                        "prerequisites": [],
                        "resources": [
                            {
                                "resource_name": "PGExercises",
                                "resource_url": "[https://pgexercises.com/](https://pgexercises.com/)",
                                "resource_type": "互动练习平台",
                                "language": "EN",
                                "reason": "“做中学”提高SQL技能最有效的方法之一，提供难度递增的在线练习和即时反馈。"
                            },
                            {
                                "resource_name": "The Art of PostgreSQL",
                                "resource_url": "[https://theartofpostgresql.com/](https://theartofpostgresql.com/)",
                                "resource_type": "在线书籍/深度指南",
                                "language": "EN",
                                "reason": "深度挖掘PG能力的免费在线书籍，讲解如何写出更高效、更优雅的SQL。"
                            }
                        ]
                    },
                    {
                        "step": 7,
                        "skill": "NoSQL 数据库 (MongoDB)",
                        "prerequisites": [],
                        "resources": [
                            {
                                "resource_name": "MongoDB University - M001: MongoDB Basics",
                                "resource_url": "[https://learn.mongodb.com/courses/m001-mongodb-basics](https://learn.mongodb.com/courses/m001-mongodb-basics)",
                                "resource_type": "官方免费课程/互动实验",
                                "language": "EN",
                                "reason": "官方权威入门课程，结合视频、测验和云端实验，动手掌握核心概念。"
                            },
                            {
                                "resource_name": "freeCodeCamp - MongoDB Full Course",
                                "resource_url": "[https://www.youtube.com/watch?v=E-1xI85Zog8](https://www.youtube.com/watch?v=E-1xI85Zog8)",
                                "resource_type": "视频课程",
                                "language": "EN",
                                "reason": "提供了对MongoDB更全面的讲解，深入数据建模、索引策略和性能优化等高级主题。"
                            }
                        ]
                    },
                    {
                        "step": 8,
                        "skill": "缓存技术 (Redis)",
                        "prerequisites": ["数据结构与算法 (Data Structures & Algorithms)"],
                        "resources": [
                            {
                                "resource_name": "《Redis 设计与实现》Read the Docs",
                                "resource_url": "[https://redisbook.readthedocs.io/en/latest/](https://redisbook.readthedocs.io/en/latest/)",
                                "resource_type": "开源在线书籍",
                                "language": "CN/EN",
                                "reason": "国产经典之作，从源码层面深度剖析Redis内部原理，助你从“会用”到“理解”。"
                            }
                        ]
                    }
                ]
            },
            {
                "stage_name": "阶段四: 容器化与 CI/CD (Containerization & CI/CD)",
                "steps": [
                    {
                        "step": 9,
                        "skill": "容器化 (Docker & Docker Compose)",
                        "prerequisites": [],
                        "resources": [
                            {
                                "resource_name": "Docker — From Zero to Hero (Prakhar Srivastav)",
                                "resource_url": "[https://prakhar.me/docker-curriculum/](https://prakhar.me/docker-curriculum/)",
                                "resource_type": "互动教程/博客系列",
                                "language": "EN",
                                "reason": "从零开始的Docker课程，通过实际操作讲解核心概念，非常适合初学者。"
                            },
                            {
                                "resource_name": "《Docker — 从入门到实践》",
                                "resource_url": "[https://vuepress.mirror.docker-practice.com/](https://vuepress.mirror.docker-practice.com/)",
                                "resource_type": "开源中文书籍",
                                "language": "CN",
                                "reason": "国内最受欢迎的Docker开源书籍之一，内容全面，覆盖了从基础到实践的方方面面。"
                            }
                        ]
                    },
                    {
                        "step": 10,
                        "skill": "CI/CD (GitHub Actions)",
                        "prerequisites": ["版本控制 (Git 核心工作流)", "容器化 (Docker & Docker Compose)"],
                        "resources": [
                            {
                                "resource_name": "GitHub Actions Documentation",
                                "resource_url": "[https://docs.github.com/en/actions](https://docs.github.com/en/actions)",
                                "resource_type": "官方文档",
                                "language": "EN/CN",
                                "reason": "学习任何技术的最佳起点，官方文档最权威、最准确。"
                            },
                            {
                                "resource_name": "CI/CD with GitHub Actions - Full Course",
                                "resource_url": "[https://www.youtube.com/watch?v=R8_veQiY-c8](https://www.youtube.com/watch?v=R8_veQiY-c8)",
                                "resource_type": "视频课程",
                                "language": "EN",
                                "reason": "freeCodeCamp出品的免费课程，系统性地讲解了如何使用GitHub Actions构建完整的CI/CD流水线。"
                            }
                        ]
                    }
                ]
            },
            {
                "stage_name": "阶段五: 可观测性与监控 (Observability & Monitoring)",
                "steps": [
                    {
                        "step": 11,
                        "skill": "日志 (Logging)",
                        "prerequisites": ["Web 框架 (FastAPI 或 Flask)"],
                        "resources": [
                            {
                                "resource_name": "Python Logging HOWTO",
                                "resource_url": "[https://docs.python.org/3/howto/logging.html](https://docs.python.org/3/howto/logging.html)",
                                "resource_type": "官方文档/指南",
                                "language": "EN",
                                "reason": "Python官方的日志指南，是理解和正确使用logging模块的最权威资料。"
                            }
                        ]
                    },
                    {
                        "step": 12,
                        "skill": "监控 (Prometheus & Grafana)",
                        "prerequisites": ["Web 框架 (FastAPI 或 Flask)", "容器化 (Docker & Docker Compose)"],
                        "resources": [
                            {
                                "resource_name": "Prometheus - Overview",
                                "resource_url": "[https://prometheus.io/docs/introduction/overview/](https://prometheus.io/docs/introduction/overview/)",
                                "resource_type": "官方文档",
                                "language": "EN",
                                "reason": "Prometheus官方文档，快速理解其架构和核心概念。"
                            },
                            {
                                "resource_name": "Grafana Fundamentals",
                                "resource_url": "[https://grafana.com/tutorials/grafana-fundamentals/](https://grafana.com/tutorials/grafana-fundamentals/)",
                                "resource_type": "官方教程",
                                "language": "EN",
                                "reason": "Grafana官方的基础教程，手把手教你创建第一个Dashboard。"
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "frontend-engineer": {
        "roadmap_title": "前端工程师",
        "stages": [
            {
                "step": 1,
                "skill": "HTML",
                "prerequisites": [],
                "resources": [
                    {
                        "resource_name": "MDN Web Docs – HTML",
                        "resource_url": "[https://developer.mozilla.org/zh-CN/docs/Web/HTML](https://developer.mozilla.org/zh-CN/docs/Web/HTML)",
                        "resource_type": "官方文档",
                        "reason": "Mozilla官方教程，内容全面更新，提供面向新手的HTML基础引导。"
                    },
                    {
                        "resource_name": "freeCodeCamp: Responsive Web Design",
                        "resource_url": "[https://www.freecodecamp.org/learn/2022/responsive-web-design/](https://www.freecodecamp.org/learn/2022/responsive-web-design/)",
                        "resource_type": "互动式教程, 实战项目",
                        "reason": "通过从零开始构建五个真实项目，将HTML理论知识即时转化为动手实践。"
                    }
                ]
            },
            {
                "step": 2,
                "skill": "CSS",
                "prerequisites": ["HTML"],
                "resources": [
                    {
                        "resource_name": "MDN Web Docs - CSS",
                        "resource_url": "[https://developer.mozilla.org/zh-CN/docs/Web/CSS](https://developer.mozilla.org/zh-CN/docs/Web/CSS)",
                        "resource_type": "官方文档",
                        "reason": "权威教程，从基础原理、语法到现代布局全面覆盖，新手友好。"
                    },
                    {
                        "resource_name": "CSS-Tricks Complete Guide to Flexbox",
                        "resource_url": "[https://css-tricks.com/snippets/css/a-guide-to-flexbox/](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)",
                        "resource_type": "文字教程",
                        "reason": "业界公认最全面的Flexbox指南，配有可视化图解和实用代码示例。"
                    },
                    {
                        "resource_name": "An Interactive Guide to CSS Grid",
                        "resource_url": "[https://www.joshwcomeau.com/css/interactive-guide-to-grid/](https://www.joshwcomeau.com/css/interactive-guide-to-grid/)",
                        "resource_type": "互动式教程, 文字教程",
                        "reason": "通过高质量的交互式示例和清晰的心理模型，将复杂的CSS Grid概念解释得极其直观易懂。"
                    },
                    {
                        "resource_name": "Flexbox Froggy",
                        "resource_url": "[https://flexboxfroggy.com/](https://flexboxfroggy.com/)",
                        "resource_type": "互动式教程",
                        "reason": "通过有趣的游戏方式学习CSS Flexbox布局，寓教于乐且效果显著。"
                    }
                ]
            },
            {
                "step": 3,
                "skill": "JavaScript",
                "prerequisites": ["HTML", "CSS"],
                "resources": [
                    {
                        "resource_name": "JavaScript.info",
                        "resource_url": "[https://javascript.info/](https://javascript.info/)",
                        "resource_type": "文字教程, 类官方文档",
                        "reason": "当代最全面、结构最清晰、内容最深入的JavaScript在线教程，是构建扎实JS知识体系的首选。"
                    },
                    {
                        "resource_name": "Eloquent JavaScript (在线免费版)",
                        "resource_url": "[https://eloquentjavascript.net/](https://eloquentjavascript.net/)",
                        "resource_type": "文字教程, 书籍, 实战项目",
                        "reason": "经典JavaScript学习书籍的免费在线版，理论与实践并重，配有大量练习题。"
                    },
                    {
                        "resource_name": "JavaScript30 - 30天原生JS挑战",
                        "resource_url": "[https://javascript30.com/](https://javascript30.com/)",
                        "resource_type": "实战项目",
                        "reason": "Wes Bos出品的30个纯JavaScript项目，完全免费，强化DOM操作和实战能力。"
                    }
                ]
            },
            {
                "step": 4,
                "skill": "Git & GitHub",
                "prerequisites": [],
                "resources": [
                    {
                        "resource_name": "Learn Git Branching 互动教程",
                        "resource_url": "[https://learngitbranching.js.org/](https://learngitbranching.js.org/)",
                        "resource_type": "互动式教程",
                        "reason": "可视化的Git学习工具，通过动画演示分支操作，支持中文，寓教于乐。"
                    },
                    {
                        "resource_name": "GitHub Docs: Hello World",
                        "resource_url": "[https://docs.github.com/en/get-started/quickstart/hello-world](https://docs.github.com/en/get-started/quickstart/hello-world)",
                        "resource_type": "互动式教程, 官方文档",
                        "reason": "无需安装任何软件，通过纯网页操作，完美地介绍了GitHub协作流程的核心概念。"
                    },
                    {
                        "resource_name": "Pro Git (中文版)",
                        "resource_url": "[https://www.progit.cn/](https://www.progit.cn/)",
                        "resource_type": "官方文档/书籍",
                        "reason": "由Git社区翻译发布的免费电子书，详尽介绍Git使用与原理，帮助学习者从初学者成长为专家。"
                    }
                ]
            },
            {
                "step": 5,
                "skill": "TypeScript 核心",
                "prerequisites": ["JavaScript"],
                "resources": [
                    {
                        "resource_name": "TypeScript 官方手册 (Handbook)",
                        "resource_url": "[https://www.typescriptlang.org/docs/handbook/intro.html](https://www.typescriptlang.org/docs/handbook/intro.html)",
                        "resource_type": "官方文档",
                        "reason": "学习TS最权威、最准确的起点，内容与时俱进，并提供可在Playground中实时运行的示例。"
                    },
                    {
                        "resource_name": "TypeScript Deep Dive",
                        "resource_url": "[https://basarat.gitbook.io/typescript/](https://basarat.gitbook.io/typescript/)",
                        "resource_type": "免费在线书籍",
                        "reason": "备受社区推崇的免费在线书，深入剖析TS设计哲学和复杂概念，完美补充官方文档。"
                    },
                    {
                        "resource_name": "Total TypeScript (免费部分)",
                        "resource_url": "[https://www.totaltypescript.com/](https://www.totaltypescript.com/)",
                        "resource_type": "互动教程",
                        "reason": "顶级TS专家出品，通过在浏览器中解决类型挑战来学习，对掌握泛型等抽象概念极有效。"
                    }
                ]
            },
            {
                "step": 6,
                "skill": "现代构建工具 (Vite)",
                "prerequisites": ["JavaScript"],
                "resources": [
                    {
                        "resource_name": "Vite 官方文档",
                        "resource_url": "[https://vitejs.dev/guide/](https://vitejs.dev/guide/)",
                        "resource_type": "官方文档",
                        "reason": "理解Vite基于原生ESM的革命性优势和所有核心功能的基石，是学习和查阅的首选。"
                    },
                    {
                        "resource_name": "Awesome Vite.js",
                        "resource_url": "[https://github.com/vitejs/awesome-vite](https://github.com/vitejs/awesome-vite)",
                        "resource_type": "资源集合",
                        "reason": "由官方维护的Vite生态资源大全，包含海量插件、模板和实战项目，是进阶必备的宝库。"
                    }
                ]
            },
            {
                "step": 7,
                "skill": "现代样式方案 (Tailwind CSS)",
                "prerequisites": ["CSS"],
                "resources": [
                    {
                        "resource_name": "Tailwind CSS 官方文档",
                        "resource_url": "[https://tailwindcss.com/docs/installation](https://tailwindcss.com/docs/installation)",
                        "resource_type": "官方文档/互动手册",
                        "reason": "文档本身就是革命性的学习产品，搜索功能强大，提供实时预览，实用性极强。"
                    }
                ]
            },
            {
                "step": 8,
                "skill": "React.js 核心",
                "prerequisites": ["JavaScript"],
                "resources": [
                    {
                        "resource_name": "React.dev - Learn React",
                        "resource_url": "[https://react.dev/learn](https://react.dev/learn)",
                        "resource_type": "官方文档, 互动式教程",
                        "reason": "全新改版的React官方文档本身就是一套顶级的互动式课程，是学习现代React最权威的起点。"
                    },
                    {
                        "resource_name": "Scrimba: Learn React for Free",
                        "resource_url": "[https://scrimba.com/learn/learnreact](https://scrimba.com/learn/learnreact)",
                        "resource_type": "视频课程, 互动式教程",
                        "reason": "由金牌讲师Bob Ziroll主讲，通过构建多个真实有趣的项目，将React概念融会贯通。"
                    },
                    {
                        "resource_name": "Full Stack Open",
                        "resource_url": "https://fullstackopen.com/en/",
                        "resource_type": "文字教程, 实战项目",
                        "reason": "由赫尔辛基大学出品的免费顶级课程，其React部分以极其深入和实践的方式，引导学生构建完整应用。"
                    }
                ]
            },
            {
                "step": 9,
                "skill": "Next.js 核心",
                "prerequisites": ["React.js 核心"],
                "resources": [
                    {
                        "resource_name": "Next.js Learn (官方互动教程)",
                        "resource_url": "https://nextjs.org/learn",
                        "resource_type": "官方文档/互动教程",
                        "reason": "业界教程典范，通过构建一个真实应用系统讲解App Router所有核心概念，是学习现代Next.js的不二之选。"
                    },
                    {
                        "resource_name": "Vercel 官方模板库",
                        "resource_url": "https://vercel.com/templates/next.js",
                        "resource_type": "开源项目/模板代码",
                        "reason": "Vercel官方提供的最佳实践项目，覆盖博客、电商等场景，是学习生产环境代码的捷径。"
                    },
                    {
                        "resource_name": "Lee Robinson 的博客",
                        "resource_url": "https://leerob.io/",
                        "resource_type": "深度文章",
                        "reason": "Vercel开发者关系副总裁的博客，提供关于Next.js和React前沿技术的最深度、最前瞻的见解。"
                    }
                ]
            },
            {
                "step": 10,
                "skill": "前端测试",
                "prerequisites": ["JavaScript"],
                "resources": [
                    {
                        "resource_name": "Vitest 官方文档",
                        "resource_url": "https://vitest.dev/guide/",
                        "resource_type": "官方文档",
                        "reason": "专为Vite设计，速度极快，文档清晰介绍了Mocking、Snapshot等核心测试功能。"
                    },
                    {
                        "resource_name": "React Testing Library 官方文档",
                        "resource_url": "https://testing-library.com/docs/react-testing-library/intro/",
                        "resource_type": "官方文档",
                        "reason": "核心在于其‘像用户一样测试’的哲学，必须先阅读其理念，再学习API。"
                    },
                    {
                        "resource_name": "Kent C. Dodds 的博客",
                        "resource_url": "https://kentcdodds.com/blog",
                        "resource_type": "深度文章/教程",
                        "reason": "React Testing Library作者的博客，提供了关于测试策略和最佳实践最权威的解读。"
                    }
                ]
            },
            {
                "step": 11,
                "skill": "Web 性能优化",
                "prerequisites": ["HTML", "CSS", "JavaScript"],
                "resources": [
                    {
                        "resource_name": "web.dev - Core Web Vitals",
                        "resource_url": "https://web.dev/vitals/",
                        "resource_type": "官方文档/深度文章",
                        "reason": "Google官方的CWV最终权威信息源，深入剖析LCP, INP, CLS的测量方法与优化策略。"
                    },
                    {
                        "resource_name": "Next.js 文档 - 性能优化",
                        "resource_url": "https://nextjs.org/docs/app/building-your-application/optimizing",
                        "resource_type": "官方文档/最佳实践",
                        "reason": "将性能理论与框架实践完美结合，讲解如何利用next/image, next/font等优化CWV。"
                    },
                    {
                        "resource_name": "Google for Developers - YouTube",
                        "resource_url": "https://www.youtube.com/@GoogleDevelopers",
                        "resource_type": "视频教程/工具教学",
                        "reason": "官方开发者频道，包含大量使用Lighthouse和DevTools诊断性能瓶颈的视频教程。"
                    }
                ]
            },
            {
                "step": 12,
                "skill": "Web 可访问性",
                "prerequisites": ["HTML"],
                "resources": [
                    {
                        "resource_name": "WAI-ARIA Authoring Practices Guide (APG)",
                        "resource_url": "https://www.w3.org/WAI/ARIA/apg/",
                        "resource_type": "官方实践指南",
                        "reason": "将WCAG标准付诸实践的‘圣经’，为复杂动态组件提供了符合ARIA规范的最佳实现范例。"
                    },
                    {
                        "resource_name": "MDN - Web Accessibility",
                        "resource_url": "https://developer.mozilla.org/en-US/docs/Web/Accessibility",
                        "resource_type": "官方文档/教程",
                        "reason": "MDN提供的系统性无障碍学习路径，内容全面且持续更新，是比单个视频系列更可靠的基础资源。"
                    },
                    {
                        "resource_name": "WebAIM 资源中心",
                        "resource_url": "https://webaim.org/resources/",
                        "resource_type": "实战指南/工具",
                        "reason": "提供了屏幕阅读器测试指南、WCAG检查清单等高质量免费资源，是动手实践的唯一途径。"
                    }
                ]
            }
        ]
    },
    "devops-engineer": {
        "roadmap_title": "DevOps工程师",
        "stages": [
            {
                "stage_name": "阶段一: 基础核心 (Foundation)",
                "steps": [
                    {
                        "step": 1,
                        "skill": "Linux 命令行与系统管理",
                        "prerequisites": [],
                        "resources": [
                            {
                                "resource_name": "《The Linux Command Line》",
                                "resource_url": "https://linuxcommand.org/tlcl.php",
                                "resource_type": "免费电子书",
                                "reason": "全球公认的Linux命令行‘圣经’，系统性强，从零到精通，打下坚实基础。"
                            },
                            {
                                "resource_name": "linuxjourney",
                                "resource_url": "https://linuxjourney.com/",
                                "resource_type": "互动教程",
                                "reason": "‘小步快跑’的互动式学习平台，通过在线练习快速掌握核心概念，适合初学者。"
                            }
                        ]
                    },
                    {
                        "step": 2,
                        "skill": "计算机网络基础",
                        "prerequisites": [],
                        "resources": [
                            {
                                "resource_name": "Hussein Nasser's YouTube Channel",
                                "resource_url": "https://www.youtube.com/@hnasr/playlists",
                                "resource_type": "视频课程",
                                "reason": "深入讲解网络协议的本质，图解清晰，帮你建立超越面试知识点的深度理解。"
                            },
                            {
                                "resource_name": "Julia Evans's Blog & Zines",
                                "resource_url": "https://jvns.ca/",
                                "resource_type": "深度文章/漫画",
                                "reason": "用有趣、可视化的方式解释复杂网络概念，如DNS、HTTP，高效且易于记忆。"
                            }
                        ]
                    },
                    {
                        "step": 3,
                        "skill": "脚本编程 (Python 或 Go)",
                        "prerequisites": [],
                        "resources": [
                            {
                                "resource_name": "Automate the Boring Stuff with Python",
                                "resource_url": "https://automatetheboringstuff.com/",
                                "resource_type": "免费电子书/课程",
                                "reason": "完美契合DevOps需求，不教软件工程，专教如何用Python实现自动化任务。"
                            },
                            {
                                "resource_name": "A Tour of Go",
                                "resource_url": "https://go.dev/tour/welcome/1",
                                "resource_type": "官方互动教程",
                                "reason": "Go语言官方出品，在浏览器中边学边练，是学习Go语言的权威第一站。"
                            }
                        ]
                    },
                    {
                        "step": 4,
                        "skill": "版本控制 (Git)",
                        "prerequisites": [],
                        "resources": [
                            {
                                "resource_name": "Pro Git (中文版)",
                                "resource_url": "https://git-scm.com/book/zh/v2",
                                "resource_type": "官方电子书",
                                "reason": "Git官方权威书籍，不仅教‘如何用’，更教‘为什么’，深入理解底层原理。"
                            },
                            {
                                "resource_name": "Learn Git Branching",
                                "resource_url": "https://learngitbranching.js.org/",
                                "resource_type": "互动可视化教程",
                                "reason": "游戏化的方式让抽象的Git分支、合并、变基操作直观可见，掌握复杂工作流神器。"
                            }
                        ]
                    }
                ]
            },
            {
                "stage_name": "阶段二: CI/CD 与自动化构建",
                "steps": [
                    {
                        "step": 5,
                        "skill": "GitHub Actions",
                        "prerequisites": ["版本控制 (Git)"],
                        "resources": [
                            {
                                "resource_name": "GitHub Actions 官方文档与快速入门",
                                "resource_url": "https://docs.github.com/en/actions/quickstart",
                                "resource_type": "官方文档",
                                "reason": "学习任何工具的最佳起点，官方文档权威、全面，示例丰富，紧跟最新特性。"
                            },
                            {
                                "resource_name": "GitHub Actions Tutorial by TechWorld with Nana",
                                "resource_url": "https://www.youtube.com/watch?v=R8_veQiYBjI&list=PLy7NrYWoggjzSIlwxeBbcgfAdYoxCIrM2",
                                "resource_type": "视频课程",
                                "reason": "顶级DevOps讲师Nana出品，从零开始系统讲解GitHub Actions所有核心概念和实战技巧。"
                            }
                        ]
                    }
                ]
            },
            {
                "stage_name": "阶段三: 容器化与编排",
                "steps": [
                    {
                        "step": 6,
                        "skill": "容器化基础 (Docker)",
                        "prerequisites": ["Linux 命令行与系统管理"],
                        "resources": [
                            {
                                "resource_name": "Docker 官方入门教程 (Get Started)",
                                "resource_url": "https://docs.docker.com/get-started/",
                                "resource_type": "官方文档/教程",
                                "reason": "官方手把手教程，覆盖Dockerfile、Compose等核心知识，建立可靠的知识体系。"
                            },
                            {
                                "resource_name": "Play with Docker",
                                "resource_url": "https://labs.play-with-docker.com/",
                                "resource_type": "交互式实验环境",
                                "reason": "无需本地安装，直接在浏览器中获得一个真实的Docker环境进行动手实验。"
                            }
                        ]
                    },
                    {
                        "step": 7,
                        "skill": "容器编排 (Kubernetes)",
                        "prerequisites": ["容器化基础 (Docker)", "计算机网络基础"],
                        "resources": [
                            {
                                "resource_name": "Kubernetes 官方文档 (中文版)",
                                "resource_url": "https://kubernetes.io/zh-cn/docs/home/",
                                "resource_type": "官方文档",
                                "reason": "学习K8s最权威、最准确的资源，没有之一，备考CKA/CKAD必备。"
                            },
                            {
                                "resource_name": "Killercoda - Interactive K8s Scenarios",
                                "resource_url": "https://killercoda.com/",
                                "resource_type": "交互式实验环境",
                                "reason": "在浏览器中获得真实K8s集群，完成部署、排错等任务，将理论转化为实践技能。"
                            },
                            {
                                "resource_name": "TechWorld with Nana - K8s Tutorial",
                                "resource_url": "https://www.youtube.com/watch?v=X48VuDVv0do",
                                "resource_type": "视频课程",
                                "reason": "广受好评的入门视频，用生动的动画和图示解释K8s复杂架构，是系统学习前的绝佳领路人。"
                            }
                        ]
                    }
                ]
            },
            {
                "stage_name": "阶段四: IaC 与配置管理",
                "steps": [
                    {
                        "step": 8,
                        "skill": "基础设施即代码 (Terraform)",
                        "prerequisites": ["脚本编程 (Python 或 Go)"],
                        "resources": [
                            {
                                "resource_name": "HashiCorp Learn - Terraform Tutorials",
                                "resource_url": "https://developer.hashicorp.com/terraform/tutorials",
                                "resource_type": "官方互动教程",
                                "reason": "Terraform创造者官方出品，质量极高，覆盖从基础到多云、GitOps等高级主题。"
                            },
                            {
                                "resource_name": "freeCodeCamp - Terraform Course (2024)",
                                "resource_url": "https://www.youtube.com/watch?v=7xngnjfIlK4",
                                "resource_type": "视频课程",
                                "reason": "2024年最新版Terraform入门教程，从零开始讲解核心概念，并部署实际的AWS基础设施。"
                            }
                        ]
                    },
                    {
                        "step": 9,
                        "skill": "配置管理 (Ansible)",
                        "prerequisites": ["Linux 命令行与系统管理"],
                        "resources": [
                            {
                                "resource_name": "Ansible 官方文档 - User Guide",
                                "resource_url": "https://docs.ansible.com/ansible/latest/user_guide/index.html",
                                "resource_type": "官方文档",
                                "reason": "最权威的参考资料，系统介绍Playbooks, Roles, Modules等核心概念。"
                            },
                            {
                                "resource_name": "Jeff Geerling's YouTube Channel",
                                "resource_url": "https://www.youtube.com/c/JeffGeerling",
                                "resource_type": "视频教程/文章",
                                "reason": "Ansible社区公认的专家，其教程非常实用，紧跟社区最佳实践。"
                            }
                        ]
                    }
                ]
            },
            {
                "stage_name": "阶段五: 监控、日志与可观测性",
                "steps": [
                    {
                        "step": 10,
                        "skill": "监控与告警 (Prometheus & Grafana)",
                        "prerequisites": ["Linux 命令行与系统管理", "计算机网络基础"],
                        "resources": [
                            {
                                "resource_name": "Prometheus 官方文档",
                                "resource_url": "https://prometheus.io/docs/introduction/overview/",
                                "resource_type": "官方文档",
                                "reason": "理解Prometheus核心概念（如PromQL）最准确的地方，使用者必读。"
                            },
                            {
                                "resource_name": "Grafana Fundamentals (Official Tutorial)",
                                "resource_url": "https://grafana.com/tutorials/grafana-fundamentals/",
                                "resource_type": "官方实战教程",
                                "reason": "Grafana官方出品，通过Docker一键启动包含Prometheus的完整环境，动手实践整个可观测性工作流。"
                            }
                        ]
                    },
                    {
                        "step": 11,
                        "skill": "日志管理 (ELK Stack)",
                        "prerequisites": ["Linux 命令行与系统管理"],
                        "resources": [
                            {
                                "resource_name": "Get started with the Elastic Stack",
                                "resource_url": "https://www.elastic.co/start",
                                "resource_type": "官方入门指南",
                                "reason": "Elastic官方最新的云优先入门路径，通过免费云服务在几分钟内搭建功能齐全的日志平台。"
                            },
                            {
                                "resource_name": "DigitalOcean - EFK on Kubernetes",
                                "resource_url": "https://www.digitalocean.com/community/tutorials/how-to-set-up-an-elasticsearch-fluentd-and-kibana-efk-logging-stack-on-kubernetes",
                                "resource_type": "深度实战文章",
                                "reason": "高质量实战教程，展示了如何在K8s中部署日志系统，体现云原生最佳实践。"
                            }
                        ]
                    }
                ]
            },
            {
                "stage_name": "阶段六: 云平台实践",
                "steps": [
                    {
                        "step": 12,
                        "skill": "核心云服务 (AWS)",
                        "prerequisites": ["Linux 命令行与系统管理", "计算机网络基础"],
                        "resources": [
                            {
                                "resource_name": "AWS Workshops",
                                "resource_url": "https://workshops.aws/",
                                "resource_type": "官方互动实验",
                                "reason": "AWS官方免费动手实验平台，在真实环境中构建应用，是转化知识为技能的最佳方式。"
                            },
                            {
                                "resource_name": "freeCodeCamp - AWS CCP Course",
                                "resource_url": "https://www.youtube.com/watch?v=SOTamWNgDKc",
                                "resource_type": "视频课程",
                                "reason": "系统且清晰地讲解AWS核心服务(IAM, VPC, EC2, S3)，帮你建立宏观认知。"
                            }
                        ]
                    }
                ]
            }
        ]
    }
}

# ==================================================
# API 路由 (Endpoints)
# ==================================================

# --- 获取所有学习路径的概览 --- 
@app.route('/api/roadmaps', methods=['GET'])
def get_roadmaps():
    """
    返回所有可用学习路径的概览列表 (slug 和 title)。
    这是为了让前端可以动态生成导航菜单。
    """
    roadmap_overviews = [
        {
            "slug": slug,
            "title": data.get("roadmap_title", "Untitled Roadmap") # 使用 .get() 增加健壮性
        }
        for slug, data in mock_db.items()
    ]
    return jsonify(roadmap_overviews), 200

# --- 根据 slug 获取特定学习路径的详细信息 ---
@app.route('/api/roadmaps/<string:roadmap_slug>', methods=['GET'])
def get_roadmap_by_slug(roadmap_slug):
    """
    根据提供的 slug，返回单个学习路径的完整数据。
    """
    roadmap_data = mock_db.get(roadmap_slug)

    # 如果找到了数据
    
    if roadmap_data:
        # 使用 jsonify 把我们的字典数据转换成标准的JSON格式返回给前端
        # 同时返回 200 状态码，表示“成功”
        return jsonify(roadmap_data), 200
    # 如果没找到数据
    else:
        # 就返回我们API文档里定义的那个 404 错误信息
        # 同时返回 404 状态码，表示“未找到”
        return jsonify({"error": "Not Found", "message": f"Roadmap with slug '{roadmap_slug}' not found."}), 404

# ==================================================
# 启动 Flask 应用
# ==================================================
if __name__ == '__main__':
    # 使用 debug=True 可以在修改代码后自动重启服务
    # port=5001 是为了方便本地同时运行多个应用，你可以根据需要修改
    app.run(debug=True, port=5001)