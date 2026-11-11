# 自我认知与修炼 · Self Understanding & Cultivation

> 一个从真实情境出发、允许被反驳的自我认知与行为成长开放框架。

**状态：v0.2（12 道情境交互与复盘演示，2026-11-11）**。这是一套可讨论、可复核的设计提案，**不是**已验证的人格量表、心理测验或已证明有效的干预产品。

## 核心主张

人不是一个恒定的“优点/缺点清单”。同一种行为在不同目标、约束、关系和风险下，可能带来不同结果。

系统应当从一个人的**具体选择 → 真实事件 → 当时条件 → 行为与结果 → 替代策略 → 后续验证**中建立可更新的情境性假设，而不是把一次选择归结为“自私”“软弱”“完美主义”等永久标签。

## 六步闭环

1. **情境选择**：先回答有明确冲突、代价与条件的问题；选择本身不赋予人格分数。
2. **真实经历**：主动记录近期一件真实事件，区分可观察事实、想法、感受和未知。
3. **情境分析**：检查能力（C）、机会/环境（O）、动机（M）以及具体目标、时间、权力、可逆性、关系成本。
4. **动态画像**：只输出证据支撑的“在何种情境下出现何种应对方式”的假设，附例外和反例。
5. **历史与文学镜鉴**：用同一分析表阅读历史人物、小说人物的选择；多角度分析，不把人物当作标准答案。
6. **行为实验**：制定 If–Then 行动计划，在下一次真实场景中记录实际行为与后果；允许修订之前判断。

## 在线体验（无需登录）

**[立即体验 12 道情境与行为复盘](https://longqaz27-web.github.io/self-understanding-cultivation/)**。现在支持 12 道情境逐题选择、真实事件记录、两种待验证解释、COM-B 三因素检查、If–Then 实验、复盘状态和 JSON 本地导入/导出。也可直接打开 `docs/index.html` 离线使用。

页面不使用账号、服务器上传、Cookie 或浏览器持久保存。**关闭或刷新前必须主动导出，之后再导入继续**。情境选择只能代表当前假设偏好，单条事件无法构成稳定人格画像。

## 从哪里开始

- [使用者入门：完成第一次自我分析](docs/QUICKSTART.md)
- [开放框架与行为规则](docs/FRAMEWORK.md)
- [情境题设计原则](docs/SCENARIO_METHOD.md)
- [证据等级、画像更新与禁止推断](docs/EVIDENCE_AND_PROFILE.md)
- [经典与历史使用方式](docs/HISTORY_AND_LITERATURE.md)
- [隐私与边界](docs/PRIVACY_AND_SAFETY.md)
- [如何检验是否真的有用](docs/VALIDATION_PLAN.md)
- [可填写的真实事件模板](forms/episode_form.md)
- [7 天复盘模板](forms/seven_day_review.md)
- [虚构示例](examples/fictional_episode.json)
- [参与讨论与贡献](CONTRIBUTING.md)

## 开放内容与可复核性

公开方法说明、情境卡、字段定义、样例、验收测试、版本修改记录；公开任何规则变动及理由。内部“3 条可比事件/2 个日期”的画像发布门槛仅是 **v0.1 审慎产品规则，不是心理测量学效度证明**。

```bash
python3 -m unittest discover -s tests -v
```

## 依据与声明

该框架**借鉴** COM-B 行为系统、CBT 事件/想法记录与实施意向，但本项目自己的题目、画像规则和训练流程**尚未经过独立效度验证**。

- Michie et al. (2011), Behaviour Change Wheel / COM-B: https://doi.org/10.1186/1748-5908-6-42
- NHS, Thought record (CBT): https://www.nhs.uk/every-mind-matters/mental-wellbeing-tips/self-help-cbt-techniques/thought-record/
- Gollwitzer & Sheeran (2006), Implementation intentions: https://doi.org/10.1016/S0065-2601(06)38002-1

## 发布到 GitHub

本文件包在你本机解压后，进入目录运行 `bash publish.sh`。脚本会先运行测试，要求输入 `PUBLISH`，再创建 `longqaz27-web/self-understanding-cultivation` 公开仓库并推送 v0.1；它不会覆盖同名现有仓库。发布前请检查不含个人事件记录。

## 许可

原创文字、模板和情境卡采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)；`docs/index.html` 和 `tests/` 中原创代码采用 MIT 许可，详见 [`LICENSE`](LICENSE) 与 [`LICENSE-CODE`](LICENSE-CODE)。引用文献及古今作品不因此转入本项目许可。

**不收集参与者真实事件作为公开贡献；请勿在 Issue/PR 发布可识别个人的经历。**
