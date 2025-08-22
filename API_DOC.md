# Programmer Roadmap 项目 API 文档 (V1.1 - 最终版)

本文档用于说明 Programmer Roadmap 项目后端 API 的使用方法。

---

## 学习路径 (Learning Roadmaps)

### 1. 获取所有学习路径的概览

获取系统支持的所有学习路径的列表，每个路径包含其唯一标识符（slug）和标题。

* **接口路径**: `/api/roadmaps`
* **请求方法**: `GET`
* **请求参数**: 无
* **成功返回示例 (Success 200 OK)**:

    ```json
    [
        {
            "slug": "web-full-stack",
            "title": "Web 全栈开发者"
        },
        {
            "slug": "ai-agent-engineer",
            "title": "AI Agent 工程师"
        },
        {
            "slug": "backend-engineer",
            "title": "后端工程师"
        },
        {
            "slug": "frontend-engineer",
            "title": "前端工程师"
        },
        {
            "slug": "devops-engineer",
            "title": "DevOps工程师"
        },
        {
            "slug": "data-engineer",
            "title": "数据工程师"
        },
        {
            "slug": "mobile-developer",
            "title": "移动应用开发者"
        },
    ]
    ```

### 2. 获取特定学习路径下的所有资源
根据提供的路径标识符（如 `web-full-stack`），获取该学习路径下的所有教学资源节点，并按学习顺序排列。

* **接口路径**: `/api/roadmaps/{roadmap_slug}`
    * *路径参数 (Path Parameter)*:
        * `roadmap_slug` (string, required): 学习路径的唯一标识。例如: `web-full-stack`。

* **请求方法**: `GET`

* **请求参数**: 无

* **成功返回示例 (Success 200 OK)**:
    * 当 `roadmap_slug` 为 `web-full-stack` 时，返回的数据结构如下：

    ```json
    {
      "roadmap_title": "Web 全栈开发者",
      "stages": [
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
          "prerequisites": [
            "HTML"
          ],
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
          "prerequisites": [
            "HTML",
            "CSS"
          ],
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
              "resource_url": "https://javascript.info/",
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
          "prerequisites": [
            "HTML",
            "CSS",
            "JavaScript"
          ],
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
          "prerequisites": [
            "JavaScript"
          ],
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
        {
          "step": 6,
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
          "step": 7,
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

根据提供的路径标识符（`ai-agent-engineerr`），获取该学习路径下的所有教学资源节点，并按学习顺序排列。

* **接口路径**: `/api/roadmaps/{roadmap_slug}`
    * *路径参数 (Path Parameter)*:
        * `roadmap_slug` (string, required): 学习路径的唯一标识。例如: `ai-agent-engineer`。

* **请求方法**: `GET`

* **请求参数**: 无

* **成功返回示例 (Success 200 OK)**:
    * 当 `roadmap_slug` 为 `ai-agent-engineer` 时，返回的数据结构如下：

    ```json
    {
      "roadmap_title": "AI Agent 工程师",
      "stages": [
        {
          "step": 1,
          "skill": "精通 Python 编程",
          "prerequisites": [],
          "resources": [
            {
              "resource_name": "Python 官方文档 - asyncio",
              "resource_url": "https://docs.python.org/3/library/asyncio.html",
              "resource_type": "官方文档",
              "reason": "最权威、最全面的第一手资料，定义了async/await，是理解所有异步框架的基础。"
            },
            {
              "resource_name": "ArjanCodes - \"A Complete Guide to Async/Await in Python\"",
              "resource_url": "https://www.youtube.com/watch?v=16w3F22_18s",
              "resource_type": "视频课程",
              "reason": "质量极高的视频教程，通过重构实战，让你直观感受异步编程带来的性能提升。"
            }
          ]
        },
        {
          "step": 1,
          "skill": "软件工程与 API 基础",
          "prerequisites": [
            "精通 Python 编程"
          ],
          "resources": [
            {
              "resource_name": "FastAPI 官方文档 - 入门教程",
              "resource_url": "https://fastapi.tiangolo.com/tutorial/",
              "resource_type": "官方教程",
              "reason": "业界标杆级的交互式教程，让你在学习中即时获得一个带自动化文档的高性能API。"
            },
            {
              "resource_name": "freeCodeCamp - \"FastAPI Course for Beginners\"",
              "resource_url": "https://www.youtube.com/watch?v=7t2alSnE2-I",
              "resource_type": "视频课程",
              "reason": "完整的项目视频课程，手把手带你完成从零到一的搭建、测试和部署，快速建立全局观。"
            }
          ]
        },
        {
          "step": 2,
          "skill": "LLM 理论入门",
          "prerequisites": [
            "精通 Python 编程"
          ],
          "resources": [
            {
              "resource_name": "Jay Alammar - \"The Illustrated Transformer\"",
              "resource_url": "https://jalammar.github.io/illustrated-transformer/",
              "resource_type": "深度文章",
              "reason": "无法被超越的经典，用极其直观的动图和比喻解释了复杂的Attention机制，入门必读。"
            },
            {
              "resource_name": "3Blue1Brown - \"Attention in Transformers, visually explained\"",
              "resource_url": "https://www.youtube.com/watch?v=mMa20_sJ4IU",
              "resource_type": "视频课程",
              "reason": "从数学思想的层面，让你对Attention机制的巧妙之处建立深刻的科学直觉。"
            }
          ]
        },
        {
          "step": 2,
          "skill": "高级提示工程",
          "prerequisites": [
            "LLM 理论入门"
          ],
          "resources": [
            {
              "resource_name": "OpenAI - \"Function calling\" 官方文档",
              "resource_url": "https://platform.openai.com/docs/guides/function-calling",
              "resource_type": "官方文档",
              "reason": "理解模型原生的工具调用能力，是掌握现代Agent框架底层逻辑的关键一步。"
            },
            {
              "resource_name": "\"Let's build the GPT-4 function calling API from scratch\" by AI Jason",
              "resource_url": "https://www.youtube.com/watch?v=tjYo4jU-i-s",
              "resource_type": "视频课程",
              "reason": "带你手写一个函数调用调度器，让你彻底告别“黑箱API调用者”的身份，理解其核心原理。"
            }
          ]
        },
        {
          "step": 3,
          "skill": "Agentic 框架入门 (LangChain)",
          "prerequisites": [
            "高级提示工程"
          ],
          "resources": [
            {
              "resource_name": "LangChain 官方教程 - \"Build an Agent\"",
              "resource_url": "https://python.langchain.com/docs/tutorials/agents",
              "resource_type": "官方教程",
              "reason": "学习任何框架，官方的“Get Started”教程永远是第一选择，确保你使用的是最新的实践方式。"
            },
            {
              "resource_name": "James Briggs - \"Code a LangChain Agent From Scratch\"",
              "resource_url": "https://www.youtube.com/watch?v=2y_uB1wK-e8",
              "resource_type": "视频课程",
              "reason": "通过“手搓”一个迷你版的Agent循环，能让你对框架的抽象（如AgentExecutor）有更深刻的体感。"
            }
          ]
        },
        {
          "step": 3,
          "skill": "掌握核心 Agent 模式 (ReAct)",
          "prerequisites": [
            "Agentic 框架入门 (LangChain)"
          ],
          "resources": [
            {
              "resource_name": "ReAct 论文官方实现",
              "resource_url": "https://github.com/ysymyth/ReAct",
              "resource_type": "开源项目",
              "reason": "直接运行论文作者的<200行最小化实现，剥离所有框架封装，直击ReAct循环的本质。"
            },
            {
              "resource_name": "LangChain - \"Build a ReAct agent from scratch with LangGraph\"",
              "resource_url": "https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/",
              "resource_type": "官方教程",
              "reason": "学习LangGraph如何用“图”的思想来工程化地实现ReAct模式，深入理解框架的设计哲学。"
            }
          ]
        },
        {
          "step": 4,
          "skill": "向量数据库入门",
          "prerequisites": [
            "LLM 理论入门"
          ],
          "resources": [
            {
              "resource_name": "FAISS 官方Wiki - \"Guidelines to choose an index\"",
              "resource_url": "https://github.com/facebookresearch/faiss/wiki/Guidelines-to-choose-an-index",
              "resource_type": "官方文档",
              "reason": "压榨检索性能的“优化圣经”，指导你在不同数据规模下选择最优索引，实现毫秒级检索。"
            },
            {
              "resource_name": "ChromaDB 官方博客 - \"Scaling Chroma: A Technical Deep Dive\"",
              "resource_url": "https://www.trychroma.com/blog/scaling-chroma",
              "resource_type": "深度文章",
              "reason": "讲解ChromaDB的架构以及如何进行横向扩展，是向量数据库从“单机”走向“分布式服务”的蓝图。"
            }
          ]
        },
        {
          "step": 4,
          "skill": "检索增强生成 (RAG) 全流程",
          "prerequisites": [
            "向量数据库入门",
            "掌握核心 Agent 模式 (ReAct)"
          ],
          "resources": [
            {
              "resource_name": "LlamaIndex 官方文档 - \"RAG Techniques\"",
              "resource_url": "https://docs.llamaindex.ai/en/stable/optimizing/production_rag/",
              "resource_type": "官方教程",
              "reason": "RAG优化的“军火库”，详细介绍了分块策略、重排序、多路召回等所有你需要知道的高级技巧。"
            },
            {
              "resource_name": "\"Advanced RAG 01: The RAG Triad\" by AI Jason",
              "resource_url": "https://www.youtube.com/watch?v=E2t1_aAayHw",
              "resource_type": "视频课程",
              "reason": "用清晰的“RAG三元悖论”来解释RAG评估的核心，并介绍如何系统性地提升RAG质量。"
            }
          ]
        },
        {
          "step": 5,
          "skill": "状态管理与复杂流 (LangGraph)",
          "prerequisites": [
            "掌握核心 Agent 模式 (ReAct)"
          ],
          "resources": [
            {
              "resource_name": "LangGraph 官方文档",
              "resource_url": "https://langchain-ai.github.io/langgraph/",
              "resource_type": "官方文档",
              "reason": "理解LangGraph如何用图（Graph）来定义循环和状态，掌握其作为“状态机”的本质。"
            },
            {
              "resource_name": "Bilibili - \"LangGraph快速入门与智能体开发实战\" by 九天Hector",
              "resource_url": "https://www.bilibili.com/video/BV1Kx3CzyE6Q?vd_source=14a017f1942e66549c878a8ddcc8bc2b",
              "resource_type": "视频教程",
              "reason": "优秀的中文社区实战教程，从零开始，用中文语境讲解，非常适合国内学习者快速上手。"
            }
          ]
        },
        {
          "step": 5,
          "skill": "多 Agent 协作 (CrewAI)",
          "prerequisites": [
            "掌握核心 Agent 模式 (ReAct)"
          ],
          "resources": [
            {
              "resource_name": "CrewAI 官方文档 - \"Examples\"",
              "resource_url": "https://docs.crewai.com/examples/",
              "resource_type": "官方示例",
              "reason": "官方示例库是最好的学习材料，提供了各种协作模式的即用代码，是快速启动多Agent项目的“模板库”。"
            },
            {
              "resource_name": "GitHub - \"CrewAI Agent Templates\" by joaomdmoura",
              "resource_url": "https://github.com/joaomdmoura/crewAI-examples",
              "resource_type": "开源项目",
              "reason": "直接学习框架作者提供的项目模板，比任何教程都更贴近最佳实践，可直接复用，极大加速开发。"
            }
          ]
        },
        {
          "step": 6,
          "skill": "监控、评估与调试",
          "prerequisites": [
            "检索增强生成 (RAG) 全流程",
            "多 Agent 协作 (CrewAI)"
          ],
          "resources": [
            {
              "resource_name": "RAGAs: Retrieval-Augmented Generation Assessment",
              "resource_url": "https://docs.ragas.io/",
              "resource_type": "开源框架",
              "reason": "提供评估RAG系统性能的量化指标，让你能用数据驱动的方式优化Agent。"
            },
            {
              "resource_name": "LangSmith 官方文档 - \"Automated Evaluation\"",
              "resource_url": "https://docs.smith.langchain.com/evaluation/automating",
              "resource_type": "官方教程",
              "reason": "学习如何创建自定义评估器，在每次代码提交后自动运行评估，是CI/CD的关键一环。"
            }
          ]
        },
        {
          "step": 6,
          "skill": "安全与伦理",
          "prerequisites": [
            "监控、评估与调试"
          ],
          "resources": [
            {
              "resource_name": "OWASP Top 10 for Large Language Model Applications",
              "resource_url": "https://owasp.org/www-project-top-10-for-large-language-model-applications/",
              "resource_type": "行业标准",
              "reason": "从关注Prompt注入，升级到关注OWASP总结的LLM应用十大安全风险，建立系统性安全思维。"
            },
            {
              "resource_name": "Rebuff.ai - \"The LLM Security Leaderboard\"",
              "resource_url": "https://github.com/protectai/rebuff",
              "resource_type": "开源工具",
              "reason": "开源的Prompt注入“蜜罐”和“防火墙”，让你了解当前最新的攻击技术和防御效果。"
            }
          ]
        }
      ]
    }

根据提供的路径标识符（`backend-engineer`），获取该学习路径下的所有教学资源节点，并按学习顺序排列。

* **接口路径**: `/api/roadmaps/{roadmap_slug}`
    * *路径参数 (Path Parameter)*:
        * `roadmap_slug` (string, required): 学习路径的唯一标识。例如: `backend-engineer`。

* **请求方法**: `GET`

* **请求参数**: 无

* **成功返回示例 (Success 200 OK)**:
    * 当 `roadmap_slug` 为 `backend-engineer` 时，返回的数据结构如下：

```json
{
  "roadmap_title": "后端工程师",
  "stages": [
    {
      "step": 1,
      "skill": "Python 高级编程 (OOP, 装饰器)",
      "prerequisites": [],
      "resources": [
        {
          "resource_name": "Real Python: OOP in Python 3",
          "resource_url": "https://realpython.com/python3-object-oriented-programming/",
          "resource_type": "深度文章/教程系列",
          "language": "EN",
          "reason": "全球公认的高质量教程，用海量代码示例和图解透彻讲解Python OOP。"
        },
        {
          "resource_name": "廖雪峰的Python教程-面向对象高级编程",
          "resource_url": "https://www.liaoxuefeng.com/wiki/1016959663602400/1017496031529184",
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
          "resource_url": "https://github.com/krahets/hello-algo",
          "resource_type": "开源电子书/动画图解",
          "language": "CN/EN",
          "reason": "国产优秀开源项目，通过动画图解生动展示算法原理，对国内学习者极其友好。"
        },
        {
          "resource_name": "NeetCode.io",
          "resource_url": "https://neetcode.io/",
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
          "resource_url": "https://learngitbranching.js.org/?locale=zh_CN",
          "resource_type": "互动教程/可视化学习",
          "language": "EN/CN",
          "reason": "革命性的可视化学习工具，通过网页虚拟操作，让分支等核心概念变得异常直观。"
        },
        {
          "resource_name": "Pro Git (中文版)",
          "resource_url": "https://git-scm.com/book/zh/v2",
          "resource_type": "官方书籍/权威文档",
          "language": "CN/EN",
          "reason": "Git官方权威“圣经”，内容全面、严谨、深入，任何希望精通Git的工程师都应通读。"
        }
      ]
    },
    {
      "step": 4,
      "skill": "RESTful API 设计原则",
      "prerequisites": [],
      "resources": [
        {
          "resource_name": "Microsoft - RESTful web API design",
          "resource_url": "https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design",
          "resource_type": "官方最佳实践文档",
          "language": "EN",
          "reason": "业界关于RESTful API设计的最佳实践指南之一，构建专业API的必备参考。"
        },
        {
          "resource_name": "阮一峰的网络日志 - RESTful API 设计指南",
          "resource_url": "https://www.ruanyifeng.com/blog/2014/05/restful_api.html",
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
          "resource_url": "https://fastapi.tiangolo.com/tutorial/",
          "resource_type": "官方文档/互动教程",
          "language": "EN",
          "reason": "开源项目文档的典范，手把手教你构建完整API，实战性无出其右。"
        },
        {
          "resource_name": "The Flask Mega-Tutorial by Miguel Grinberg",
          "resource_url": "https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world",
          "resource_type": "博客教程系列",
          "language": "EN",
          "reason": "无法绕过的Flask经典教程，带领学习者从零构建一个功能完整的博客应用。"
        }
      ]
    },
    {
      "step": 6,
      "skill": "关系型数据库 (PostgreSQL) 与 SQL 进阶",
      "prerequisites": [],
      "resources": [
        {
          "resource_name": "PGExercises",
          "resource_url": "https://pgexercises.com/",
          "resource_type": "互动练习平台",
          "language": "EN",
          "reason": "“做中学”提高SQL技能最有效的方法之一，提供难度递增的在线练习和即时反馈。"
        },
        {
          "resource_name": "The Art of PostgreSQL",
          "resource_url": "https://theartofpostgresql.com/",
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
          "resource_url": "https://learn.mongodb.com/courses/m001-mongodb-basics",
          "resource_type": "官方免费课程/互动实验",
          "language": "EN",
          "reason": "官方权威入门课程，结合视频、测验和云端实验，动手掌握核心概念。"
        },
        {
          "resource_name": "freeCodeCamp - MongoDB Full Course",
          "resource_url": "https://www.youtube.com/watch?v=E-1xI85Zog8",
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
          "resource_url": "https://redisbook.readthedocs.io/en/latest/",
          "resource_type": "开源在线书籍",
          "language": "CN/EN",
          "reason": "国产经典之作，从源码层面深度剖析Redis内部原理，助你从“会用”到“理解”。"
        }
      ]
    },
    {
      "step": 9,
      "skill": "容器化 (Docker & Docker Compose)",
      "prerequisites": [],
      "resources": [
        {
          "resource_name": "Docker — From Zero to Hero (Prakhar Srivastav)",
          "resource_url": "https://prakhar.me/docker-curriculum/",
          "resource_type": "互动教程/博客系列",
          "language": "EN",
          "reason": "从零开始的Docker课程，通过实际操作讲解核心概念，非常适合初学者。"
        },
        {
          "resource_name": "《Docker — 从入门到实践》",
          "resource_url": "https://vuepress.mirror.docker-practice.com/",
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
          "resource_url": "https://docs.github.com/en/actions",
          "resource_type": "官方文档",
          "language": "EN/CN",
          "reason": "学习任何技术的最佳起点，官方文档最权威、最准确。"
        },
        {
          "resource_name": "CI/CD with GitHub Actions - Full Course",
          "resource_url": "https://www.youtube.com/watch?v=R8_veQiY-c8",
          "resource_type": "视频课程",
          "language": "EN",
          "reason": "freeCodeCamp出品的免费课程，系统性地讲解了如何使用GitHub Actions构建完整的CI/CD流水线。"
        }
      ]
    },
    {
      "step": 11,
      "skill": "日志 (Logging)",
      "prerequisites": ["Web 框架 (FastAPI 或 Flask)"],
      "resources": [
        {
          "resource_name": "Python Logging HOWTO",
          "resource_url": "https://docs.python.org/3/howto/logging.html",
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
          "resource_url": "https://prometheus.io/docs/introduction/overview/",
          "resource_type": "官方文档",
          "language": "EN",
          "reason": "Prometheus官方文档，快速理解其架构和核心概念。"
        },
        {
          "resource_name": "Grafana Fundamentals",
          "resource_url": "https://grafana.com/tutorials/grafana-fundamentals/",
          "resource_type": "官方教程",
          "language": "EN",
          "reason": "Grafana官方的基础教程，手把手教你创建第一个Dashboard。"
        }
      ]
    }
  ]
}
```
// ... existing code ...

根据提供的路径标识符（`frontend-engineer`），获取该学习路径下的所有教学资源节点，并按学习顺序排列。

* **接口路径**: `/api/roadmaps/{roadmap_slug}/`
    * *路径参数 (Path Parameter)*:
        * `roadmap_slug` (string, required): 学习路径的唯一标识。例如: `frontend-engineer`。

* **请求方法**: `GET`

* **请求参数**: 无

* **成功返回示例 (Success 200 OK)**:
    * 当 `roadmap_slug` 为 `frontend-engineer` 时，返回的数据结构如下：

    ```json
    {
      "roadmap_title": "前端工程师",
      "stages": [
        {
          "step": 1,
          "skill": "HTML",
          "prerequisites": [],
          "resources": [
            {
              "resource_name": "MDN Web Docs – HTML",
              "resource_url": "https://developer.mozilla.org/zh-CN/docs/Web/HTML",
              "resource_type": "官方文档",
              "reason": "Mozilla官方教程，内容全面更新，提供面向新手的HTML基础引导。"
            },
            {
              "resource_name": "freeCodeCamp: Responsive Web Design",
              "resource_url": "https://www.freecodecamp.org/learn/2022/responsive-web-design/",
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
              "resource_url": "https://developer.mozilla.org/zh-CN/docs/Web/CSS",
              "resource_type": "官方文档",
              "reason": "权威教程，从基础原理、语法到现代布局全面覆盖，新手友好。"
            },
            {
              "resource_name": "CSS-Tricks Complete Guide to Flexbox",
              "resource_url": "https://css-tricks.com/snippets/css/a-guide-to-flexbox/",
              "resource_type": "文字教程",
              "reason": "业界公认最全面的Flexbox指南，配有可视化图解和实用代码示例。"
            },
            {
              "resource_name": "An Interactive Guide to CSS Grid",
              "resource_url": "https://www.joshwcomeau.com/css/interactive-guide-to-grid/",
              "resource_type": "互动式教程, 文字教程",
              "reason": "通过高质量的交互式示例和清晰的心理模型，将复杂的CSS Grid概念解释得极其直观易懂。"
            },
            {
              "resource_name": "Flexbox Froggy",
              "resource_url": "https://flexboxfroggy.com/",
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
              "resource_url": "https://javascript.info/",
              "resource_type": "文字教程, 类官方文档",
              "reason": "当代最全面、结构最清晰、内容最深入的JavaScript在线教程，是构建扎实JS知识体系的首选。"
            },
            {
              "resource_name": "Eloquent JavaScript (在线免费版)",
              "resource_url": "https://eloquentjavascript.net/",
              "resource_type": "文字教程, 书籍, 实战项目",
              "reason": "经典JavaScript学习书籍的免费在线版，理论与实践并重，配有大量练习题。"
            },
            {
              "resource_name": "JavaScript30 - 30天原生JS挑战",
              "resource_url": "https://javascript30.com/",
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
              "resource_url": "https://learngitbranching.js.org/",
              "resource_type": "互动式教程",
              "reason": "可视化的Git学习工具，通过动画演示分支操作，支持中文，寓教于乐。"
            },
            {
              "resource_name": "GitHub Docs: Hello World",
              "resource_url": "https://docs.github.com/en/get-started/quickstart/hello-world",
              "resource_type": "互动式教程, 官方文档",
              "reason": "无需安装任何软件，通过纯网页操作，完美地介绍了GitHub协作流程的核心概念。"
            },
            {
              "resource_name": "Pro Git (中文版)",
              "resource_url": "https://www.progit.cn/",
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
              "resource_url": "https://www.typescriptlang.org/docs/handbook/intro.html",
              "resource_type": "官方文档",
              "reason": "学习TS最权威、最准确的起点，内容与时俱进，并提供可在Playground中实时运行的示例。"
            },
            {
              "resource_name": "TypeScript Deep Dive",
              "resource_url": "https://basarat.gitbook.io/typescript/",
              "resource_type": "免费在线书籍",
              "reason": "备受社区推崇的免费在线书，深入剖析TS设计哲学和复杂概念，完美补充官方文档。"
            },
            {
              "resource_name": "Total TypeScript (免费部分)",
              "resource_url": "https://www.totaltypescript.com/",
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
              "resource_url": "https://vitejs.dev/guide/",
              "resource_type": "官方文档",
              "reason": "理解Vite基于原生ESM的革命性优势和所有核心功能的基石，是学习和查阅的首选。"
            },
            {
              "resource_name": "Awesome Vite.js",
              "resource_url": "https://github.com/vitejs/awesome-vite",
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
              "resource_url": "https://tailwindcss.com/docs/installation",
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
              "resource_url": "https://react.dev/learn",
              "resource_type": "官方文档, 互动式教程",
              "reason": "全新改版的React官方文档本身就是一套顶级的互动式课程，是学习现代React最权威的起点。"
            },
            {
              "resource_name": "Scrimba: Learn React for Free",
              "resource_url": "https://scrimba.com/learn/learnreact",
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
    }
    ```

根据提供的路径标识符（`roadmap_slug`），获取该学习路径下的所有教学资源节点。

* **接口路径**: `/api/roadmaps/{roadmap_slug}`
    *   *路径参数 (Path Parameter)*:
        *   `roadmap_slug` (string, required): 学习路径的唯一标识。例如: `devops-engineer`。
*   **请求方法**: `GET`
*   **请求参数**: 无
* **成功返回示例 (Success 200 OK)**:
    * 当 `roadmap_slug` 为 `devops-engineer` 时，返回的数据结构如下（已按阶段分组，并在每个阶段下包含 steps 列表）：

```json
{
  "roadmap_title": "DevOps工程师",
  "stages": [
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
    },
    {
      "step": 5,
      "skill": "GitHub Actions",
      "prerequisites": [
        "版本控制 (Git)"
      ],
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
    },
    {
      "step": 6,
      "skill": "容器化基础 (Docker)",
      "prerequisites": [
        "Linux 命令行与系统管理"
      ],
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
      "prerequisites": [
        "容器化基础 (Docker)",
        "计算机网络基础"
      ],
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
    },
    {
      "step": 8,
      "skill": "基础设施即代码 (Terraform)",
      "prerequisites": [
        "脚本编程 (Python 或 Go)"
      ],
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
      "prerequisites": [
        "Linux 命令行与系统管理"
      ],
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
    },
    {
      "step": 10,
      "skill": "监控与告警 (Prometheus & Grafana)",
      "prerequisites": [
        "Linux 命令行与系统管理",
        "计算机网络基础"
      ],
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
      "prerequisites": [
        "Linux 命令行与系统管理"
      ],
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
    },
    {
      "step": 12,
      "skill": "核心云服务 (AWS)",
      "prerequisites": [
        "Linux 命令行与系统管理",
        "计算机网络基础"
      ],
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
```

根据提供的路径标识符（roadmap_slug），获取该学习路径下的所有教学资源节点，并按学习顺序排列。

* 接口路径: `/api/roadmaps/{roadmap_slug}`
  * 路径参数 (Path Parameter):
    * `roadmap_slug` (string, required): 学习路径的唯一标识。例如: `data-engineer`。

* 请求方法: `GET`

* 请求参数: 无

* 成功返回示例 (Success 200 OK):
  * 当 `roadmap_slug` 为 `data-engineer` 时，返回的数据结构如下（stages 为“扁平化字典列表”）：

    ```json
    {
      "roadmap_title": "数据工程师",
      "stages": [
        {
          "step": 1,
          "skill": "Python for Data (Pandas & NumPy)",
          "prerequisites": [],
          "resources": [
            {
              "resource_name": "Kaggle - Pandas Course",
              "resource_url": "https://www.kaggle.com/learn/pandas",
              "resource_type": "互动教程/动手实验",
              "reason": "在全球最大的数据科学社区，通过交互式Notebook快速动手实践Pandas核心操作。"
            },
            {
              "resource_name": "freeCodeCamp - Data Analysis with Python",
              "resource_url": "https://www.freecodecamp.org/learn/data-analysis-with-python/",
              "resource_type": "认证项目/视频课程",
              "reason": "通过完成五个基于真实数据集的分析项目来获得认证，项目驱动，实战性极强。"
            },
            {
              "resource_name": "Pandas 官方入门教程",
              "resource_url": "https://pandas.pydata.org/docs/getting_started/tutorials.html",
              "resource_type": "官方文档",
              "reason": "理解Pandas设计哲学和“惯用”代码风格的最佳途径，权威且系统。"
            }
          ]
        },
        {
          "step": 2,
          "skill": "高级 SQL (窗口函数, CTEs)",
          "prerequisites": [],
          "resources": [
            {
              "resource_name": "Mode - Advanced SQL Tutorial",
              "resource_url": "https://mode.com/sql-tutorial/sql-window-functions/",
              "resource_type": "深度文章/互动教程",
              "reason": "业界享有盛誉的免费教程，不仅教“如何做”，更阐述“为何要这么做”。"
            },
            {
              "resource_name": "LeetCode - Top SQL 50",
              "resource_url": "https://leetcode.com/studyplan/top-sql-50/",
              "resource_type": "编程练习/实战平台",
              "reason": "LeetCode官方精选50道SQL面试高频题，是检验和提升SQL实战能力的最佳演练场。"
            }
          ]
        },
        {
          "step": 3,
          "skill": "Linux 命令行",
          "prerequisites": [],
          "resources": [
            {
              "resource_name": "The Linux Command Line (免费电子书)",
              "resource_url": "https://linuxcommand.org/tlcl.php",
              "resource_type": "电子书 (免费PDF)",
              "reason": "被广泛认为是学习Linux命令行的“圣经”，全面覆盖从基础到Shell脚本的知识体系。"
            },
            {
              "resource_name": "learnshell.org",
              "resource_url": "https://www.learnshell.org/",
              "resource_type": "互动教程",
              "reason": "无需安装任何环境，直接在浏览器中边学边练，快速建立对命令行的体感。"
            }
          ]
        },
        {
          "step": 4,
          "skill": "版本控制 (Git)",
          "prerequisites": [],
          "resources": [
            {
              "resource_name": "Pro Git (官方书籍)",
              "resource_url": "https://git-scm.com/book/en/v2",
              "resource_type": "电子书 (免费在线版)",
              "reason": "Git官方推荐的最权威学习材料，从底层模型讲起，助你真正掌握Git而非死记命令。"
            },
            {
              "resource_name": "Learn Git Branching",
              "resource_url": "https://learngitbranching.js.org/",
              "resource_type": "互动式可视化教程",
              "reason": "革命性的Git分支学习工具，通过可视化动画和沙盒练习，完美理解复杂的分支操作。"
            }
          ]
        },
        {
          "step": 5,
          "skill": "数据建模与理论 (Kimball/Inmon)",
          "prerequisites": ["高级 SQL (窗口函数, CTEs)"],
          "resources": [
            {
              "resource_name": "The Data Warehouse Toolkit (书籍)",
              "resource_url": "http://www.r-5.org/files/books/computers/databases/warehouses/Ralph_Kimball_Margy_Ross-The_Data_Warehouse_Toolkit-EN.pdf",
              "resource_type": "经典书籍 (免费PDF)",
              "reason": "维度建模“圣经”的免费PDF版，是每个数据工程师构建知识体系的必读之作。"
            },
            {
              "resource_name": "Holistics - Kimball's Dimensional Modeling",
              "resource_url": "https://www.holistics.io/books/setup-analytics/kimball-s-dimensional-data-modeling/",
              "resource_type": "深度文章",
              "reason": "以现代数据栈的视角解读Kimball理论，清晰阐述了其在当今时代的现实意义。"
            }
          ]
        },
        {
          "step": 6,
          "skill": "现代云数仓 (Snowflake / BigQuery)",
          "prerequisites": ["数据建模与理论 (Kimball/Inmon)"],
          "resources": [
            {
              "resource_name": "Snowflake University - Hands-On Essentials",
              "resource_url": "https://learn.snowflake.com/en/pages/hands-on-essentials-track/",
              "resource_type": "官方互动教程",
              "reason": "Snowflake官方学习路径，提供真实环境完成从数据加载到查询的端到端核心任务。"
            },
            {
              "resource_name": "Google Cloud - BigQuery Introduction",
              "resource_url": "https://cloud.google.com/bigquery/docs/introduction?hl=zh-cn",
              "resource_type": "官方文档",
              "reason": "Google Cloud官方中文文档，权威介绍了BigQuery的核心概念、架构与优势。"
            }
          ]
        },
        {
          "step": 7,
          "skill": "大数据处理 (Apache Spark)",
          "prerequisites": ["Python for Data (Pandas & NumPy)", "高级 SQL (窗口函数, CTEs)"],
          "resources": [
            {
              "resource_name": "Databricks - Spark Quick Start",
              "resource_url": "https://www.databricks.com/spark/getting-started-with-apache-spark/quick-start",
              "resource_type": "官方课程/互动笔记本",
              "reason": "由Spark创始团队提供，通过交互式Notebook引导完成数据加载与转换的核心操作。"
            },
            {
              "resource_name": "Apache Spark 官方文档 - Spark SQL Guide",
              "resource_url": "https://spark.apache.org/docs/latest/sql-programming-guide.html",
              "resource_type": "官方文档",
              "reason": "关于Spark DataFrame API最全面、最准确的参考资料，高性能Spark开发的必读文献。"
            }
          ]
        },
        {
          "step": 8,
          "skill": "数据转换 (dbt)",
          "prerequisites": ["高级 SQL (窗口函数, CTEs)", "数据建模与理论 (Kimball/Inmon)"],
          "resources": [
            {
              "resource_name": "dbt Labs - dbt Fundamentals",
              "resource_url": "https://courses.getdbt.com/courses/dbt-fundamentals",
              "resource_type": "官方免费课程",
              "reason": "dbt官方推出的免费基础课程，系统性地学习模型构建、测试、文档和部署。"
            },
            {
              "resource_name": "dbt Labs - Getting Started Tutorial",
              "resource_url": "https://docs.getdbt.com/guides/getting-started",
              "resource_type": "官方文档/动手教程",
              "reason": "手把手指导你从零开始搭建一个完整的dbt项目，理论学习后最好的实践巩固。"
            }
          ]
        },
        {
          "step": 9,
          "skill": "工作流编排 (Apache Airflow)",
          "prerequisites": ["Python for Data (Pandas & NumPy)", "数据转换 (dbt)"],
          "resources": [
            {
              "resource_name": "Astronomer Academy - Airflow 101",
              "resource_url": "https://academy.astronomer.io/path/airflow-101-airflow-2",
              "resource_type": "权威指南/视频课程",
              "reason": "Airflow核心商业公司出品的免费视频学习路径，系统讲解Airflow 2.x的核心概念与实践。"
            },
            {
              "resource_name": "Apache Airflow 官方文档 - Tutorial",
              "resource_url": "https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html",
              "resource_type": "官方文档/动手教程",
              "reason": "每个Airflow新手都应完成的第一步，引导你编写并运行第一个DAG。"
            }
          ]
        },
        {
          "step": 10,
          "skill": "消息队列/事件流 (Apache Kafka)",
          "prerequisites": ["Linux 命令行"],
          "resources": [
            {
              "resource_name": "Confluent Developer - Learn Apache Kafka",
              "resource_url": "https://developer.confluent.io/",
              "resource_type": "官方教程/动手实验",
              "reason": "由Kafka创始团队创建的“黄金资源库”，提供海量高质量免费教程和基于Docker的实验。"
            },
            {
              "resource_name": "Apache Kafka 官方文档 - Quickstart",
              "resource_url": "https://kafka.apache.org/quickstart",
              "resource_type": "官方文档/教程",
              "reason": "理解Kafka底层组件如何协同工作的最直接方式，建立对物理架构的直观理解。"
            }
          ]
        },
        {
          "step": 11,
          "skill": "流处理框架 (Spark/Flink)",
          "prerequisites": ["大数据处理 (Apache Spark)", "消息队列/事件流 (Apache Kafka)"],
          "resources": [
            {
              "resource_name": "Apache Spark 官方 - Structured Streaming Guide",
              "resource_url": "https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html",
              "resource_type": "官方文档",
              "reason": "学习Spark流处理最权威、最全面的资源，详解核心模型与高级特性。"
            },
            {
              "resource_name": "Apache Flink 官方 - Operations Playground",
              "resource_url": "https://nightlies.apache.org/flink/flink-docs-stable/docs/try-flink/flink-operations-playground/",
              "resource_type": "官方教程/动手实验",
              "reason": "在官方提供的Docker沙盒环境中，亲手部署Flink集群、提交作业并模拟故障恢复。"
            }
          ]
        },
        {
          "step": 12,
          "skill": "核心云数据服务 (AWS)",
          "prerequisites": ["数据转换 (dbt)", "工作流编排 (Apache Airflow)"],
          "resources": [
            {
              "resource_name": "AWS Skill Builder - Data Analytics Learning Plan",
              "resource_url": "https://explore.skillbuilder.aws/learn/public/learning_plan/view/20/data-analytics-learning-plan",
              "resource_type": "官方免费课程/学习路径",
              "reason": "AWS官方免费学习中心，系统性介绍S3、Glue、Redshift等核心数据服务。"
            },
            {
              "resource_name": "AWS Workshops",
              "resource_url": "https://workshops.aws/",
              "resource_type": "官方动手实验/项目指南",
              "reason": "海量、免费、手把手的实验指南，指导你在自己账户中从零构建完整的端到端数据管道。"
            },
            {
              "resource_name": "AWS Samples on GitHub",
              "resource_url": "https://github.com/aws-samples",
              "resource_type": "官方代码示例/架构模板",
              "reason": "由AWS官方工程师创建的真实项目代码库，了解生产级代码范例和最佳实践的宝藏。"
            }
          ]
        }
      ]
    }
    ```

根据提供的路径标识符（roadmap_slug），获取该学习路径下的所有教学资源节点，并按学习顺序排列。

* 接口路径: `/api/roadmaps/{roadmap_slug}`
  * 路径参数 (Path Parameter):
    * `roadmap_slug` (string, required): 学习路径的唯一标识。例如: `mobile-developer`。

* 请求方法: `GET`

* 请求参数: 无

* 成功返回示例 (Success 200 OK):
  * 当 `roadmap_slug` 为 `mobile-developer` 时，返回的数据结构如下（stages 为“扁平化字典列表”）：
```json
    {
      "roadmap_title": "移动端开发工程师",
      "stages": [
        {
          "step": 1,
          "skill": "移动端 UI/UX 设计原则",
          "prerequisites": [],
          "resources": [
            {
              "resource_name": "Apple Human Interface Guidelines",
              "resource_url": "https://developer.apple.com/design/human-interface-guidelines/",
              "resource_type": "官方设计规范",
              "reason": "所有iOS、iPadOS、watchOS及visionOS开发的“设计圣经”，是理解苹果生态设计哲学、组件规范和交互模式的权威源头。"
            },
            {
              "resource_name": "Material Design 3",
              "resource_url": "https://m3.material.io/",
              "resource_type": "官方设计系统与规范",
              "reason": "Google官方设计系统，现代Android应用设计的核心指南，尤其Material 3版本在动态色彩、组件更新上都有革新。"
            },
            {
              "resource_name": "Laws of UX",
              "resource_url": "https://lawsofux.com/",
              "resource_type": "深度文章/设计原则合集",
              "reason": "将复杂的心理学原则提炼为简洁的设计法则，为界面和交互决策提供强有力的理论支撑，帮助开发者“知其所以然”。"
            }
          ]
        },
        {
          "step": 2,
          "skill": "版本控制 (Git 核心工作流)",
          "prerequisites": [],
          "resources": [
            {
              "resource_name": "Pro Git (中文版)",
              "resource_url": "https://git-scm.com/book/zh/v2",
              "resource_type": "官方书籍 (免费在线)",
              "reason": "学习Git最权威、最全面的著作，由Git官方推荐，内容覆盖从基础到高级原理，是无可替代的黄金标准。"
            },
            {
              "resource_name": "Learn Git Branching",
              "resource_url": "https://learngitbranching.js.org/?locale=zh_CN",
              "resource_type": "交互式在线教程",
              "reason": "极具创新性的可视化学习工具，通过游戏化的方式动手实践Git核心操作，对初学者极其友好，实战性极强。"
            },
            {
              "resource_name": "GitHub Flow",
              "resource_url": "https://docs.github.com/zh/get-started/using-github/github-flow",
              "resource_type": "官方工作流指南",
              "reason": "由GitHub官方推荐的轻量级、基于分支的协作模型，比GitFlow更简单实用，能帮助学习者快速融入现代软件团队。"
            }
          ]
        },
        {
          "step": 3,
          "skill": "移动端 API 交互 (RESTful API & JSON)",
          "prerequisites": [],
          "resources": [
            {
              "resource_name": "MDN Web Docs - HTTP",
              "resource_url": "https://developer.mozilla.org/zh-CN/docs/Web/HTTP",
              "resource_type": "官方文档/权威教程",
              "reason": "Web技术的黄金标准文档库，详细解释了HTTP协议，是理解RESTful API的基石，内容权威、准确。"
            },
            {
              "resource_name": "Postman Learning Center",
              "resource_url": "https://learning.postman.com/docs/getting-started/introduction/",
              "resource_type": "工具实践教程",
              "reason": "Postman是API开发与测试的事实标准，其学习中心提供了从零开始的实战教程，能将理论与实际操作紧密结合。"
            },
            {
              "resource_name": "JSONPlaceholder",
              "resource_url": "https://jsonplaceholder.typicode.com/",
              "resource_type": "免费在线模拟 API",
              "reason": "免费的在线REST API，无需自己搭建后端即可练习移动端的网络请求、JSON解析和数据建模，是初学者绝佳的“靶场”。"
            }
          ]
        },
        {
          "step": 4,
          "skill": "Swift 编程语言",
          "prerequisites": [],
          "resources": [
            {
              "resource_name": "The Swift Programming Language",
              "resource_url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/",
              "resource_type": "官方书籍 (免费在线)",
              "reason": "苹果官方撰写的Swift语言权威指南，全面、精确地覆盖了所有语法和特性，是学习Swift最权威的“第一手资料”。"
            },
            {
              "resource_name": "Hacking with Swift - 100 Days of Swift",
              "resource_url": "https://www.hackingwithswift.com/100",
              "resource_type": "项目驱动式教程",
              "reason": "社区公认的最佳Swift入门实战课程，完全免费，通过100天项目将语言知识与App开发实践紧密结合。"
            },
            {
              "resource_name": "Stanford CS193p",
              "resource_url": "https://cs193p.stanford.edu/2023",
              "resource_type": "大学公开课",
              "reason": "斯坦福大学的王牌iOS开发课程，以深度和严谨性著称，深入剖析MVVM架构和SwiftUI核心思想，是殿堂级的免费资源。"
            }
          ]
        },
        {
          "step": 5,
          "skill": "SwiftUI 声明式UI框架",
          "prerequisites": ["Swift 编程语言"],
          "resources": [
            {
              "resource_name": "Apple Developer - SwiftUI Tutorials",
              "resource_url": "https://developer.apple.com/tutorials/swiftui",
              "resource_type": "官方实战教程",
              "reason": "学习SwiftUI的最佳起点，通过构建一个真实应用，手把手教会核心概念，内容权威，与Xcode深度集成。"
            },
            {
              "resource_name": "Hacking with Swift - 100 Days of SwiftUI",
              "resource_url": "https://www.hackingwithswift.com/100/swiftui",
              "resource_type": "项目驱动式教程",
              "reason": "提供了海量的项目和挑战，覆盖从基础到高级的方方面面，其实战性和社区活跃度无可匹敌，是精通SwiftUI的必经之路。"
            }
          ]
        },
        {
          "step": 6,
          "skill": "iOS 核心概念",
          "prerequisites": ["Swift 编程语言"],
          "resources": [
            {
              "resource_name": "Apple Developer Documentation",
              "resource_url": "https://developer.apple.com/documentation/",
              "resource_type": "官方API文档",
              "reason": "针对URLSession、Core Data和最新的SwiftData，苹果官方文档是最终的真相来源，提供了最精确的API定义和示例。"
            },
            {
              "resource_name": "Kodeco (Ray Wenderlich) Tutorials",
              "resource_url": "https://www.kodeco.com/ios/",
              "resource_type": "深度文章/实战教程",
              "reason": "质量极高的教程网站，其关于URLSession、Core Data和SwiftData的教程通常包含完整项目，并详细解释原理和陷阱。"
            }
          ]
        },
        {
          "step": 7,
          "skill": "依赖管理 (Swift Package Manager)",
          "prerequisites": ["Swift 编程语言"],
          "resources": [
            {
              "resource_name": "Swift.org - Swift Package Manager",
              "resource_url": "https://www.swift.org/package-manager/",
              "resource_type": "官方文档",
              "reason": "SPM的官方主页和文档入口，详细描述了清单文件结构、依赖解析规则，是创建和分发代码包的权威参考。"
            }
          ]
        },
        {
          "step": 8,
          "skill": "Kotlin 编程语言",
          "prerequisites": [],
          "resources": [
            {
              "resource_name": "Kotlin Koans",
              "resource_url": "https://play.kotlinlang.org/koans/",
              "resource_type": "交互式在线练习",
              "reason": "JetBrains官方出品的Kotlin入门“道场”，通过在线编程练习，以“闯关式”体验掌握Kotlin语法，趣味且高效。"
            }
          ]
        },
        {
          "step": 9,
          "skill": "Android Basics in Kotlin",
          "prerequisites": ["Kotlin 编程语言"],
          "resources": [
            {
              "resource_name": "Android Basics in Kotlin",
              "resource_url": "https://developer.android.com/courses/android-basics-kotlin/course",
              "resource_type": "官方入门课程",
              "reason": "Google官方为初学者设计的免费课程，将Kotlin学习与Android开发基础完美结合，是新手进入Android世界的最佳路径。"
            }
          ]
        },
        {
          "step": 10,
          "skill": "现代 Android UI (Jetpack Compose)",
          "prerequisites": ["Kotlin 编程语言"],
          "resources": [
            {
              "resource_name": "Jetpack Compose Pathway",
              "resource_url": "https://developer.android.com/courses/pathways/compose",
              "resource_type": "官方学习路径",
              "reason": "Google官方为学习Compose打造的全方位学习路径，包含高质量的Codelabs、视频和文档，系统且权威。"
            },
            {
              "resource_name": "Now in Android (Official Sample App)",
              "resource_url": "https://github.com/android/nowinandroid",
              "resource_type": "官方示例项目",
              "reason": "完全使用Kotlin和Compose构建的官方开源应用，是理论通向实践的最佳桥梁，展示了现代Android架构的最佳实践。"
            }
          ]
        },
        {
          "step": 11,
          "skill": "Android 核心概念",
          "prerequisites": ["Kotlin 编程语言"],
          "resources": [
            {
              "resource_name": "Google Codelabs for Android",
              "resource_url": "https://codelabs.developers.google.com/?cat=Android",
              "resource_type": "官方实战教程",
              "reason": "提供针对Room、Retrofit等特定技术点的“手把手”教程，项目完整、步骤清晰，是学习Jetpack核心库的最佳方式。"
            },
            {
              "resource_name": "Retrofit Official Documentation",
              "resource_url": "https://square.github.io/retrofit/",
              "resource_type": "官方库文档",
              "reason": "Android生态最流行的类型安全HTTP客户端，官方文档简洁明了，是使用该库时最权威的参考。"
            }
          ]
        },
        {
          "step": 12,
          "skill": "构建系统 (Gradle)",
          "prerequisites": ["Kotlin 编程语言"],
          "resources": [
            {
              "resource_name": "Android Gradle Plugin User Guide",
              "resource_url": "https://developer.android.com/studio/build",
              "resource_type": "官方指南",
              "reason": "Google官方提供的权威指南，解释了Android项目特有的构建逻辑，如依赖配置、构建变体、签名等。"
            }
          ]
        },
        {
          "step": 13,
          "skill": "Flutter 框架与 Dart 语言",
          "prerequisites": [],
          "resources": [
            {
              "resource_name": "Flutter Official \"Get Started\"",
              "resource_url": "https://docs.flutter.dev/get-started/install",
              "resource_type": "官方入门教程",
              "reason": "Flutter官方文档被公认为业界典范，引导清晰，体验流畅，并内置Dart语言之旅，一站式完成基础学习。"
            },
            {
              "resource_name": "The Boring Flutter Development Show",
              "resource_url": "https://www.youtube.com/watch?v=JFm_89xDM_k&list=PLjxrf2q8roU3ahJVrSgAnPjzkpGmL9Czl",
              "resource_type": "官方视频实战秀",
              "reason": "由Flutter团队工程师“实时编程”，充满了真实的开发过程和问题解决，能让学习者看到专家如何思考和使用Flutter。"
            }
          ]
        },
        {
          "step": 14,
          "skill": "Flutter 状态管理 (Provider / BLoC)",
          "prerequisites": ["Flutter 框架与 Dart 语言"],
          "resources": [
            {
              "resource_name": "Flutter Official State Management Docs",
              "resource_url": "https://docs.flutter.dev/data-and-backend/state-mgmt/simple",
              "resource_type": "官方概念指南",
              "reason": "清晰地解释了状态管理的核心概念，并简要介绍了多种方案，为后续学习具体库打下坚实的理论基础。"
            },
            {
              "resource_name": "BLoC Library Official Documentation",
              "resource_url": "https://bloclibrary.dev/",
              "resource_type": "官方库文档与教程",
              "reason": "BLoC是适合大型应用的结构化状态管理模式，其官网提供了从核心概念到最佳实践的完整教程，是不二之选。"
            }
          ]
        },
        {
          "step": 15,
          "skill": "与原生平台通信 (Platform Channels)",
          "prerequisites": ["Flutter 框架与 Dart 语言"],
          "resources": [
            {
              "resource_name": "Flutter Docs - Platform Channels",
              "resource_url": "https://docs.flutter.dev/platform-integration/platform-channels",
              "resource_type": "官方权威教程",
              "reason": "学习Flutter与原生代码通信的最权威资源，通过一个完整示例清晰展示了如何在Dart和原生端(Swift/Kotlin)编写通信代码。"
            }
          ]
        },
        {
          "step": 16,
          "skill": "应用商店发布流程",
          "prerequisites": [],
          "resources": [
            {
              "resource_name": "App Store Connect Help",
              "resource_url": "https://help.apple.com/app-store-connect/",
              "resource_type": "官方帮助文档",
              "reason": "在苹果App Store发布和管理应用的最权威指南，详细说明了从创建到提交审核的每一个步骤。"
            },
            {
              "resource_name": "Google Play Console Help",
              "resource_url": "https://support.google.com/googleplay/android-developer/",
              "resource_type": "官方帮助文档",
              "reason": "Google Play商店的官方指南，涵盖应用发布、测试、商品详情、政策合规等所有管理任务。"
            },
            {
              "resource_name": "fastlane",
              "resource_url": "https://fastlane.tools/",
              "resource_type": "自动化工具与文档",
              "reason": "开源工具集，可以自动化所有繁琐的发布任务（截图、证书、上传等），是专业移动端开发者提升效率的必备技能。"
            }
          ]
        },
        {
          "step": 17,
          "skill": "移动端 CI/CD (Codemagic 或 GitHub Actions)",
          "prerequisites": [],
          "resources": [
            {
              "resource_name": "Codemagic Documentation",
              "resource_url": "https://docs.codemagic.io/",
              "resource_type": "官方工具文档",
              "reason": "专为移动应用设计的CI/CD平台，文档友好，提供了大量预设工作流，可以快速实现自动化构建、测试和发布。"
            },
            {
              "resource_name": "GitHub Actions Documentation",
              "resource_url": "https://docs.github.com/en/actions",
              "resource_type": "官方平台文档",
              "reason": "目前最主流的CI/CD解决方案之一，结合社区提供的actions，可以为iOS/Android搭建功能强大的自动化流程。"
            }
          ]
        },
        {
          "step": 18,
          "skill": "应用分析与崩溃监控 (Firebase / Sentry)",
          "prerequisites": [],
          "resources": [
            {
              "resource_name": "Firebase Crashlytics Documentation",
              "resource_url": "https://firebase.google.com/docs/crashlytics",
              "resource_type": "官方工具文档",
              "reason": "Google提供的核心崩溃报告工具，官方文档提供了在各平台集成的详细步骤，是保障应用稳定性的首选。"
            },
            {
              "resource_name": "Sentry for Mobile Documentation",
              "resource_url": "https://docs.sentry.io/platforms/mobile/",
              "resource_type": "官方工具文档",
              "reason": "业界领先的错误和性能监控平台，在错误上下文追踪、性能监控方面功能更强大，适合进行更深入的性能分析。"
            }
          ]
        }
      ]
    }
    ```

* **失败返回示例 (Error 404 Not Found)**:
    * 当提供的 `roadmap_slug` 不存在时，（例如 `/api/roadmaps/non-existent-slug`），返回：

    ```json
    {
      "error": "Not Found",
      "message": "Roadmap with slug 'non-existent-slug' not found."
    }
    ```