# S4P2 项目 API 文档 (V1.0 - 核心路径完成版)

本文档用于说明 S4P2 项目后端 API 的使用方法。

---

## 学习路径 (Learning Roadmaps)

### 1. 获取特定学习路径下的所有资源

根据提供的路径标识符（`roadmap_slug`），获取该学习路径下的所有教学资源节点，并按学习顺序排列。

* **接口路径**: `/api/roadmaps/{roadmap_slug}`
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

* **失败返回示例 (Error 404 Not Found)**:
    * 当提供的 `roadmap_slug` 不存在时（例如 `/api/roadmaps/non-existent-path`），返回：

    ```json
    {
      "error": "Not Found",
      "message": "The requested learning roadmap was not found."
    }
    ```