# 导入 Flask 和 jsonify (jsonify 是一个能帮我们把Python字典转换成标准JSON格式的工具)
from flask import Flask, jsonify

# Flask 应用初始化
app = Flask(__name__)

# ==================================================
# 我们的“假数据库” (V2.5 - 全资源最终版)
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
                        "resource_url": "https://developer.mozilla.org/zh-CN/docs/Web/HTML",
                        "resource_type": "官方文档",
                        "reason": "Mozilla官方教程，内容全面更新，提供面向新手的HTML基础引导"
                    },
                    {
                        "resource_name": "编程狮(W3Cschool) – HTML 教程",
                        "resource_url": "https://www.w3cschool.cn/html/",
                        "resource_type": "文字教程",
                        "reason": "国内知名中文教程，讲解直观易懂，提供大量交互示例和练习"
                    },
                    {
                        "resource_name": "慕课网-《初识HTML5+CSS3》课程",
                        "resource_url": "https://www.imooc.com/learn/9",
                        "resource_type": "免费视频课程",
                        "reason": "免费入门级视频课程，零基础讲解HTML和CSS，每课配小案例实战"
                    },
                    {
                        "resource_name": "Learn HTML.org 互动教程",
                        "resource_url": "https://www.learn-html.org/",
                        "resource_type": "互动式教程",
                        "reason": "完全免费的互动式学习平台，让学习者边写边学，快速掌握HTML核心概念"
                    },
                    {
                        "resource_name": "web.dev 学习 HTML",
                        "resource_url": "https://web.dev/learn/html",
                        "resource_type": "文字教程",
                        "reason": "Google出品的现代HTML教程，注重实用性和语义化，内容新颖且实战导向"
                    },
                    {
                        "resource_name": "freeCodeCamp: Responsive Web Design Certification",
                        "resource_url": "https://www.freecodecamp.org/learn/2022/responsive-web-design/",
                        "resource_type": "互动式教程, 实战项目",
                        "reason": "通过从零开始构建五个真实项目，将HTML理论知识即时转化为动手实践"
                    },
                    {
                        "resource_name": "freeCodeCamp HTML 完整教程",
                        "resource_url": "https://www.youtube.com/watch?v=kUMe1FH4CHE",
                        "resource_type": "视频课程",
                        "reason": "超过3小时的完整HTML5教程，包含10个实践章节和项目实战，完全免费且广受好评"
                    },
                    {
                        "resource_name": "HTML Interactive Exercises",
                        "resource_url": "https://breatheco.de/interactive-exercise/html-exercises",
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
                        "resource_url": "https://developer.mozilla.org/zh-CN/docs/Web/CSS",
                        "resource_type": "官方文档",
                        "reason": "权威教程，从基础原理、语法到现代布局全面覆盖，新手友好"
                    },
                    {
                        "resource_name": "菜鸟教程- CSS 教程",
                        "resource_url": "http://www.runoob.com/css/css-tutorial.html",
                        "resource_type": "文字教程",
                        "reason": "中文教程，内容简洁清晰，涵盖选择器、盒模型、布局等，拥有数百在线示例"
                    },
                    {
                        "resource_name": "编程狮(W3Cschool) – CSS 教程",
                        "resource_url": "https://m.w3cschool.cn/css/",
                        "resource_type": "文字教程",
                        "reason": "免费中文教程，详细介绍各种样式应用，配有在线代码编辑器和上百实战案例"
                    },
                    {
                        "resource_name": "CSS-Tricks Complete Guide to Flexbox",
                        "resource_url": "https://css-tricks.com/snippets/css/a-guide-to-flexbox/",
                        "resource_type": "文字教程",
                        "reason": "业界公认最全面的Flexbox指南，配有可视化图解和实用代码示例，2024年持续更新"
                    },
                    {
                        "resource_name": "Josh Comeau 的互动 Flexbox 指南",
                        "resource_url": "https://www.joshwcomeau.com/css/interactive-guide-to-flexbox/",
                        "resource_type": "互动式教程",
                        "reason": "顶级前端专家制作的互动教程，通过动画演示深入理解Flexbox工作原理"
                    },
                    {
                        "resource_name": "CSS-Tricks Complete Guide to Grid",
                        "resource_url": "https://css-tricks.com/snippets/css/complete-guide-grid/",
                        "resource_type": "文字教程",
                        "reason": "CSS Grid的权威指南，详尽的属性说明配合实例，是掌握现代布局的必备资源"
                    },
                    {
                        "resource_name": "An Interactive Guide to CSS Grid",
                        "resource_url": "https://www.joshwcomeau.com/css/interactive-guide-to-grid/",
                        "resource_type": "互动式教程, 文字教程",
                        "reason": "通过高质量的交互式示例和清晰的心理模型，将复杂的CSS Grid概念解释得极其直观易懂"
                    },
                    {
                        "resource_name": "CSS-Tricks 完整指南",
                        "resource_url": "https://css-tricks.com/",
                        "resource_type": "文字教程",
                        "reason": "业界最受欢迎的CSS资源网站，提供丰富的实例代码和最新的CSS技术文章"
                    },
                    {
                        "resource_name": "Kevin Powell CSS 频道",
                        "resource_url": "https://www.youtube.com/channel/UCJZv4d5rbIKd4QHMPkcABCw",
                        "resource_type": "视频课程",
                        "reason": "被誉为“CSS之王”的Kevin Powell制作的高质量教学视频，深受开发者社区喜爱"
                    },
                    {
                        "resource_name": "Flexbox Froggy",
                        "resource_url": "https://flexboxfroggy.com/",
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
                        "resource_url": "https://developer.mozilla.org/zh-CN/docs/Learn_web_development/Getting_started/Your_first_website/Adding_interactivity",
                        "resource_type": "教程",
                        "reason": "Mozilla官方教程，新手友好，介绍现代JavaScript基础语法、DOM操作、异步编程等内容"
                    },
                    {
                        "resource_name": "编程狮(W3Cschool) – JavaScript 教程",
                        "resource_url": "https://www.w3cschool.cn/article/22792294.html",
                        "resource_type": "文字教程",
                        "reason": "系统讲解JS语法与DOM，语句易懂全面，包括回调、Promise等异步特性，拥有大量交互示例"
                    },
                    {
                        "resource_name": "JavaScript.info",
                        "resource_url": "https://javascript.info/",
                        "resource_type": "文字教程, 类官方文档",
                        "reason": "涵盖现代JavaScript的免费在线教程，内容新颖完整，配有互动示例和实战练习"
                    },
                    {
                        "resource_name": "Eloquent JavaScript (在线免费版)",
                        "resource_url": "https://eloquentjavascript.net/",
                        "resource_type": "文字教程, 书籍, 实战项目",
                        "reason": "经典JavaScript学习书籍的免费在线版，理论与实践并重，配有大量练习题"
                    },
                    {
                        "resource_name": "JavaScript30 - 30天原生JS挑战",
                        "resource_url": "https://javascript30.com/",
                        "resource_type": "实战项目",
                        "reason": "Wes Bos出品的30个纯JavaScript项目，完全免费，强化DOM操作和实战能力"
                    },
                    {
                        "resource_name": "The Modern JavaScript Tutorial",
                        "resource_url": "https://javascript.info",
                        "resource_type": "文字教程, 类官方文档",
                        "reason": "当代最全面、结构最清晰、内容最深入的JavaScript在线教程，是构建扎实JS知识体系的首选"
                    },
                    {
                        "resource_name": "freeCodeCamp: JavaScript Full Course",
                        "resource_url": "https://www.youtube.com/watch?v=PkZNo7MFNFG",
                        "resource_type": "视频课程, 互动式教程",
                        "reason": "专为视觉学习者设计，通过视频形式系统讲解JS核心概念，并包含大量小型实践项目"
                    },
                    {
                        "resource_name": "JavaScript DOM 操作教程",
                        "resource_url": "https://www.youtube.com/watch?v=jlyBx0Yh4rl",
                        "resource_type": "视频课程",
                        "reason": "1小时完整的DOM操作实战教程，包含事件处理、动画和实际项目演示"
                    },
                    {
                        "resource_name": "W3Schools JavaScript ES6",
                        "resource_url": "https://www.w3schools.com/js/js_es6.asp",
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
                        "resource_url": "https://zh-hans.react.dev/",
                        "resource_type": "官方文档",
                        "reason": "由React团队维护的权威教程，全面讲解组件、Hooks、路由等关键概念，具有中文版"
                    },
                    {
                        "resource_name": "菜鸟教程 - React 教程",
                        "resource_url": "http://www.runoob.com/react/react-tutorial.html",
                        "resource_type": "文字教程",
                        "reason": "中文基础教程，介绍React核心特性，可在线编辑示例代码并即时查看效果"
                    },
                    {
                        "resource_name": "Scrimba - Learn React 免费课程",
                        "resource_url": "https://v1.scrimba.com/playlist/p7P5Hd",
                        "resource_type": "互动式教程",
                        "reason": "交互式视频课程，包含59个互动单元，通过实战项目掌握React基础与进阶用法"
                    },
                    {
                        "resource_name": "React 官方教程",
                        "resource_url": "https://react.dev/learn",
                        "resource_type": "官方文档",
                        "reason": "React官方新版教程，从零开始讲解现代React，权威且最新"
                    },
                    {
                        "resource_name": "Full Stack Open - React 部分",
                        "resource_url": "https://fullstackopen.com/en/",
                        "resource_type": "文字教程",
                        "reason": "赫尔辛基大学出品的免费全栈课程，React部分内容深入且配有大量实战练习"
                    },
                    {
                        "resource_name": "React 实战项目教程",
                        "resource_url": "https://github.com/gopinav/React-Tutorials",
                        "resource_type": "实战项目",
                        "reason": "GitHub上星级很高的React项目合集，从简单组件到完整应用，代码清晰易懂"
                    },
                    {
                        "resource_name": "React.dev - Learn React",
                        "resource_url": "https://react.dev/learn",
                        "resource_type": "官方文档, 互动式教程",
                        "reason": "全新改版的React官方文档本身就是一套顶级的互动式课程，是学习现代React最权威的起点"
                    },
                    {
                        "resource_name": "Scrimba: Learn React for Free",
                        "resource_url": "https://scrimba.com/learn/learnreact",
                        "resource_type": "视频课程, 互动式教程",
                        "reason": "由金牌讲师Bob Ziroll主讲，通过构建多个真实有趣的项目，将React概念融会贯通"
                    },
                    {
                        "resource_name": "Full Stack Open",
                        "resource_url": "https://fullstackopen.com/en/",
                        "resource_type": "文字教程, 实战项目",
                        "reason": "由赫尔辛基大学出品的免费顶级课程，其React部分以极其深入和实践的方式，引导学生构建完整应用"
                    },
                    {
                        "resource_name": "React 2024 完整初学者教程",
                        "resource_url": "https://www.youtube.com/watch?v=x4rFhThSX04",
                        "resource_type": "视频课程",
                        "reason": "2024年最新的React教程，通过实际项目学习组件、状态管理和现代React开发"
                    },
                    {
                        "resource_name": "W3Schools React 教程",
                        "resource_url": "https://www.w3schools.com/REACT/DEFAULT.ASP",
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
                        "resource_url": "https://nodejs.org/en/docs/",
                        "resource_type": "官方文档",
                        "reason": "Node.js官方权威文档，涵盖所有核心模块和API，是学习服务器端JS的必备参考"
                    },
                    {
                        "resource_name": "Express 官方文档",
                        "resource_url": "https://expressjs.com/zh-cn",
                        "resource_type": "官方文档",
                        "reason": "官方指南提供详尽示例，介绍Express核心功能和中间件用法，支持多语言"
                    },
                    {
                        "resource_name": "菜鸟教程 - Node.js 教程",
                        "resource_url": "http://www.runoob.com/nodejs/nodejs-tutorial.html",
                        "resource_type": "文字教程",
                        "reason": "简明介绍Node.js平台与特点，新手友好地阐述事件驱动架构和高性能优势"
                    },
                    {
                        "resource_name": "廖雪峰 - Node.js 入门",
                        "resource_url": "https://liaoxuefeng.com/books/javascript/nodejs/index.html",
                        "resource_type": "文字教程",
                        "reason": "专业教程第三部分“Node.js”，从安装到模块化开发全流程讲解，通过案例展示为何“Node.js将JS带入后端”"
                    },
                    {
                        "resource_name": "Node.js Design Patterns 在线版",
                        "resource_url": "https://github.com/PacktPublishing/Node.js-Design-Patterns-Third-Edition",
                        "resource_type": "文字教程",
                        "reason": "深入讲解Node.js核心概念和设计模式，GitHub开源版本，适合进阶学习"
                    },
                    {
                        "resource_name": "NodeSchool 互动学习",
                        "resource_url": "https://nodeschool.io/",
                        "resource_type": "互动式教程",
                        "reason": "通过命令行互动学习Node.js，边做边学的方式掌握异步编程和核心模块"
                    },
                    {
                        "resource_name": "Node.js 2024 完整课程",
                        "resource_url": "https://www.youtube.com/watch?v=32M1al-Y6Ag",
                        "resource_type": "视频课程",
                        "reason": "Traversy Media制作的2024年最新Node.js教程，涵盖核心模块和服务器开发实战"
                    },
                    {
                        "resource_name": "W3Schools Node.js 教程",
                        "resource_url": "https://www.w3schools.com/nodejs/",
                        "resource_type": "互动式教程",
                        "reason": "提供在线编辑器的Node.js学习环境，适合初学者掌握服务器端JavaScript开发"
                    },
                    {
                        "resource_name": "MDN 学习区 - Express/Node 入门教程",
                        "resource_url": "https://developer.mozilla.org/zh-CN/docs/Learn/web_development/Extensions/Server-side/Express_Nodejs/Introduction",
                        "resource_type": "文字教程",
                        "reason": "Mozilla提供的Express教程，从Node、Express基础到REST API构建，内容清晰有条理"
                    },
                    {
                        "resource_name": "Express.js 官方指南",
                        "resource_url": "https://expressjs.com/en/guide/routing.html",
                        "resource_type": "官方文档",
                        "reason": "Express官方完整指南，从路由到中间件的权威教程，代码示例丰富"
                    },
                    {
                        "resource_name": "REST API 实战教程",
                        "resource_url": "https://github.com/hagopj13/node-express-boilerplate",
                        "resource_type": "实战项目",
                        "reason": "GitHub高星级的Express项目模板，展示了完整的REST API最佳实践和项目结构"
                    },
                    {
                        "resource_name": "Express.js 完整教程系列",
                        "resource_url": "https://github.com/microsoft/nodejs-guidelines",
                        "resource_type": "文字教程",
                        "reason": "微软出品的Node.js开发指南，包含Express最佳实践和企业级开发规范"
                    },
                    {
                        "resource_name": "MDN Web Docs: Express/Node.js Introduction",
                        "resource_url": "https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/Introduction",
                        "resource_type": "文字教程, 类官方文档",
                        "reason": "在动手编码前，提供了对Node.js和Express核心概念最全面、最清晰的理论解释"
                    },
                    {
                        "resource_name": "freeCodeCamp: Node.js and Express.js - Full Course",
                        "resource_url": "https://www.youtube.com/watch?v=Oe421EPjeBE",
                        "resource_type": "视频课程, 实战项目",
                        "reason": "一个非常实用的代码跟随视频教程，完整演示了从零搭建一个Express服务器的过程"
                    },
                    {
                        "resource_name": "Express 2024 速成课程",
                        "resource_url": "https://www.youtube.com/watch?v=CnH3kAXSrmU",
                        "resource_type": "视频课程",
                        "reason": "Traversy Media制作的1.5小时Express速成教程，涵盖路由、中间件和API开发"
                    },
                    {
                        "resource_name": "Codecademy Learn Express",
                        "resource_url": "https://www.codecademy.com/learn/learn-express",
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
                        "resource_url": "https://liaoxuefeng.com/books/git/what-is-git/index.html",
                        "resource_type": "文字教程",
                        "reason": "国内资深作者撰写的免费教程，从概念到命令逐步讲解，风格通俗幽默，社区广泛使用"
                    },
                    {
                        "resource_name": "菜鸟教程 - Git 教程",
                        "resource_url": "http://www.runoob.com/git/git-tutorial.html",
                        "resource_type": "文字教程",
                        "reason": "中文入门教程，介绍Git原理与常用命令，内容直观易懂，配有示例操作"
                    },
                    {
                        "resource_name": "Pro Git (中文版)",
                        "resource_url": "https://www.progit.cn/",
                        "resource_type": "官方文档/书籍",
                        "reason": "由Git社区翻译发布的免费电子书，详尽介绍Git使用与原理，帮助学习者从初学者成长为专家"
                    },
                    {
                        "resource_name": "Pro Git 官方书籍",
                        "resource_url": "https://git-scm.com/book",
                        "resource_type": "官方文档",
                        "reason": "Git官方权威教程，从入门到精通，有完整中文翻译版本，完全免费"
                    },
                    {
                        "resource_name": "Learn Git Branching 互动教程",
                        "resource_url": "https://learngitbranching.js.org/",
                        "resource_type": "互动式教程",
                        "reason": "可视化的Git学习工具，通过动画演示分支操作，支持中文，寓教于乐"
                    },
                    {
                        "resource_name": "GitHub Skills",
                        "resource_url": "https://skills.github.com/",
                        "resource_type": "实战项目",
                        "reason": "GitHub官方提供的实践课程，在真实仓库中学习Git和GitHub工作流"
                    },
                    {
                        "resource_name": "GitHub Docs: Hello World",
                        "resource_url": "https://docs.github.com/en/get-started/quickstart/hello-world",
                        "resource_type": "互动式教程, 官方文档",
                        "reason": "无需安装任何软件，通过纯网页操作，完美地介绍了GitHub协作流程的核心概念"
                    },
                    {
                        "resource_name": "freeCodeCamp: Git and GitHub for Beginners - Crash Course",
                        "resource_url": "https://www.youtube.com/watch?v=RGOj5yH7evk",
                        "resource_type": "视频课程",
                        "reason": "作为一部引导式教程，它将GitHub的概念与本地的命令行实践连接起来，完整演示了从创建项目到发起Pull Request的全过程"
                    },
                    {
                        "resource_name": "Git 官方文档",
                        "resource_url": "https://git-scm.com/doc",
                        "resource_type": "官方文档",
                        "reason": "Git官方维护的权威文档，提供完整的命令参考和最佳实践指导"
                    },
                    {
                        "resource_name": "Git 和 GitHub 2024 完整教程",
                        "resource_url": "https://www.youtube.com/watch?v=l2yrJtwoC_E",
                        "resource_type": "视频课程",
                        "reason": "近2小时的2024年最新教程，涵盖Git基础到高级操作和GitHub协作流程"
                    },
                    {
                        "resource_name": "GitHub Learning Lab",
                        "resource_url": "https://lab.github.com/",
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
                        "resource_url": "http://www.runoob.com/sql/sql-tutorial.html",
                        "resource_type": "文字教程",
                        "reason": "标准化SQL语言教程，系统介绍关系型数据库基础操作，包含众多例子，新手易上手"
                    },
                    {
                        "resource_name": "树懒学堂 - SQL 教程",
                        "resource_url": "https://www.shulanxt.com/database/sql/sql-tutorial",
                        "resource_type": "文字教程",
                        "reason": "中文SQL学习资源，覆盖数据库操作核心语句，每章配实际使用示例，帮助巩固CRUD概念"
                    },
                    {
                        "resource_name": "SQLZoo - 交互式教程",
                        "resource_url": "https://sqlzoo.net/wiki/SQL_Tutorial",
                        "resource_type": "互动式教程",
                        "reason": "免费在线学习平台，通过逐步练习和实时反馈掌握SQL，配有练习题和测验"
                    },
                    {
                        "resource_name": "SQLBolt 互动 SQL 教程",
                        "resource_url": "https://sqlbolt.com/",
                        "resource_type": "互动式教程",
                        "reason": "界面极其简洁，通过一系列“先学后练”的交互式课程，让初学者在浏览器中直接编写和执行SQL查询"
                    },
                    {
                        "resource_name": "W3Schools SQL 教程",
                        "resource_url": "https://www.w3schools.com/sql/",
                        "resource_type": "文字教程",
                        "reason": "结构化的SQL基础教程，配有在线编辑器，可以直接运行SQL语句练习"
                    },
                    {
                        "resource_name": "SQL Murder Mystery",
                        "resource_url": "https://mystery.knightlab.com/",
                        "resource_type": "互动式教程",
                        "reason": "通过破案游戏学习SQL查询，寓教于乐的方式掌握复杂的JOIN和聚合查询"
                    },
                    {
                        "resource_name": "Mode: The SQL Tutorial for Data Analysis",
                        "resource_url": "https://mode.com/sql-tutorial/",
                        "resource_type": "文字教程",
                        "reason": "一套非常全面、结构化的文本教程，在数据分析的背景下讲解SQL，提供了更深入的概念解释"
                    },
                    {
                        "resource_name": "W3Schools SQL 教程",
                        "resource_url": "https://www.w3schools.com/sql/",
                        "resource_type": "互动式教程",
                        "reason": "提供在线SQL编辑器的完整教程，涵盖所有主流数据库系统，适合初学者掌握CRUD操作"
                    },
                    {
                        "resource_name": "SQLBolt 交互式课程",
                        "resource_url": "https://sqlbolt.com/",
                        "resource_type": "互动式教程",
                        "reason": "广受开发者推荐的免费SQL学习平台，通过实际数据库练习掌握查询技能"
                    },
                    {
                        "resource_name": "Mode Analytics SQL 教程",
                        "resource_url": "https://mode.com/sql-tutorial/",
                        "resource_type": "文字教程",
                        "reason": "专为数据分析设计的SQL教程，提供真实数据集和实际业务场景的查询练习"
                    }
                ]
            }
        ]
    }
}
# ==================================================

# 这是我们新开发的、真正的业务API接口
@app.route("/api/roadmaps/<string:roadmap_slug>")
def get_roadmap_data(roadmap_slug):
    # 从我们的“假数据库”里，根据用户请求的 roadmap_slug 查找数据
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
        return jsonify({"error": "Not Found", "message": "The requested learning roadmap was not found."}), 404
