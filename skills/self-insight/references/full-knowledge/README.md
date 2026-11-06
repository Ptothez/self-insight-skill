# 知识原子库 / Knowledge Atom Library

本库保留九模块的原有知识、方法与案例，并把全部已提供文本的补充知识接入同一检索入口。原有知识文件没有被改写或删减。

The original nine-module knowledge, methods and cases remain intact. Additional knowledge from every supplied text is available through the same local search interface.

## 原子与知识包 / Atoms and Knowledge Packs

知识原子仍分为概念（含方法、条件与区分）、关系、案例、反例四类，不是单纯的概念定义。每条保留完整内容、来源、适用条件、限制及相关原子；案例保留已知事实和未知结果，关系保留方向与成立条件。原有五类知识文档与补充原子库一起服务九模块，不以摘要替代正文。

当前共 13,479 条知识原子：原有 477 条，加全量补充 13,002 条。按类型为概念 11,144、关系 166、案例 1,960、反例 209；另有 42 条背景存档，不计入原子数量，仍保留且可显式查询。不同语境中的同类观点保持各自条件，不把条数宣传成互不重复的概念数。分类与模块统计见 `atom-inventory.json`。各模块可共享原子，模块计数不能相加作为全库数量。

The library contains 13,479 knowledge atoms: concepts (including methods and conditions), relations, cases and counterexamples. This includes 477 retained atoms and 13,002 expanded atoms. Another 42 context items remain available but are not counted as knowledge atoms. Atom entries are not a count of unique concepts; shared module membership is not additive. See `atom-inventory.json` for the breakdown.

`records/*.jsonl` 与 `legacy-records.jsonl` 是兼容既有检索的存储文件名，不是另一种知识产品，也不改变原子标准。关系网另含原子间的连接；连接数不冒充原子数。

## 查找具体知识 / Find Knowledge

从自观入口目录执行，不需要 API、账号、课程原件或作者的电脑路径：

```powershell
python scripts/search-knowledge.py "当前问题的关键词"
python scripts/search-knowledge.py "界限 责任" --module "界限"
python scripts/search-knowledge.py --id "legacy:jx-c-01" --related
```

- 默认同时查找旧库与全文补充库。`--origin legacy`、`--origin expanded` 可分别查看；不要求使用者理解内部编号才能提问。
- `--id` 读取完整记录，`--related` 连同原有关系和新旧库的语义连接一起展开。阅读正文、步骤、条件、限制、依据及 `review_notes`，不仅看标题；原文没有记下的动作不能自行补成操作步骤。
- `--source` 按来源读取；同一原子来自多个课次时，各来源均可找到它。用 `--limit` 与 `--offset` 继续分页，不能把首屏当成全课内容。
- 履历、营销等背景不作为咨询知识默认返回；必要核查可使用 `--include-context`。匿名实践案例不属于这类背景，仍保留在正常知识中。
- 没有 Python 时，按 `module-index/*.md` 定位，在 `records/*.jsonl` 或 `legacy-records.jsonl` 读取对应编号的完整内容。

Search includes both retained and expanded records. Read each record together with its steps, conditions, limits and evidence. Related results may cross modules; a search hit does not authorize switching the main dialogue route.

## 关系与来源 / Relations and Provenance

- `legacy-records.jsonl`：原有 477 条原子的只读检索映射，原始文件仍在各模块中。
- `legacy-bridges.jsonl`：新旧知识之间的等价、补充、条件差异或冲突。每条连接包含理由和条件；不因相似而删除任一原子。
- `maps/`：保留课次概念与流程图谱，补入逐点提取的记录索引。
- `point-index.jsonl`：知识点到原子的定位关系，不包含课程长段原文、私人路径或审计中的身份资料。
- `module-links.json`：辅助模块的适用线索。必须同时检查主入口 catalog 和来源限制；模块标签不把儿童方法自动扩展到成人。

Semantic links distinguish equivalence, complementary detail, different applicability and unresolved conflict. Different conditions must not be collapsed into a single rule. Source block identifiers support traceability without distributing the original transcripts.

关系标记为 `uncertain` 时，只能视为待核对的关联，不能据此推出原因或建议；先使用已经有依据的内容，必要时确认会改变判断的事实。`knowledge-differences.json` 保留新旧表述之间的条件差异与未解决冲突，不默默选一边。

An `uncertain` relation is not evidence for a causal conclusion or recommendation. Consult the recorded differences instead of silently choosing the more convenient claim.

## 使用边界 / Use Boundaries

课程主张、实际案例、假设、角色扮演和模型整理出的关联不是同一类证据。忠实提取不等于独立科学验证；角色扮演中的对立观点不是课程建议。来源未回答的问题继续保留未知，不用常识补造答案。

涉及药物、诊断、体罚、暴力与危机时，必须遵循自观入口的安全边界。不得把课程中的药物说法改成自行用药指导，不以性别认同或性倾向为病理，不提供改变性取向的干预。

Course claims are not clinical validation. Do not turn medication claims into prescribing instructions, present an opponent's role-play position as advice, or invent missing case outcomes. Safety rules in the main Skill take precedence over ordinary dialogue flows.

公开包不包含课程原件、私人提取记录、API 凭据或真实文件路径。表达重合检查与匿名化降低发布风险，但不等于权利人的授权或法律保证。

The distributable package excludes original transcripts, private audit records, credentials and private paths. De-identification and expression review are not a copyright license or a legal guarantee.
