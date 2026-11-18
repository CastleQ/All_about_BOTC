# All about BOTC

**시계탑에 흐른 피(Blood on the Clocktower, 시계피)의 한국어 지식 원천이자 만능 도구.**
Claude에 설치하면 룰 판정, 커스텀 스크립트 분석, 홈브류 설계, 이야기꾼 퀴즈 출제까지 시계피와 관련한 일을 함께하는 조언자가 됩니다.

> 제작사 The Pandemonium Institute(TPI)와 관계없는 비공식 커뮤니티 자료입니다.

---

## 무엇을 할 수 있나요

| 스킬 | 이름 | 하는 일 | 사용 방법 |
|---|---|---|---|
| `botc-rules-advisor` | 룰 조언자 | "독살범한테 중독된 픽시는 어떻게 돼?", "마귀할멈이 만든 임프는 그날 밤 깨워?" 같은 룰·상호작용·징크스 판정을 물어보면, 출처와 근거에 따른 이야기꾼의 진행에 가장 합리적인 조언을 해줍니다. | 별다른 사용방법이 없습니다. 이 플러그인을 설치하고, 룰이나 상호작용의 해석 등을 질문하면 클로드가 알아서 스킬을 켜고 답변합니다. |
| `botc-script-analysis` | 스크립트 분석 | 커스텀 스크립트(캐릭터 시트 이미지·JSON)의 인원별 선악 밸런스, 플레이 경험, 캐릭터 존재감 등을 객관화된 시각으로 분석하고, 결과를 이미지나 PDF 자료로 만듭니다. | 스크립트 JSON 파일이나 시트 이미지를 클로드 창에 입력하고 "분석"이라고 말하세요. 클로드가 알아서 스킬을 켜고 분석합니다. |
| `botc-homebrew-design` | 홈브류 디자이너 | 창의적인 홈브류 캐릭터 아이디어 제안 및 다듬기, 능력 문구와 단어를 공식 용어집에 맞게 쓰기, 밸런스 점검, 캐릭터 목록 및 밤 순서를 논리에 맞게 정돈한 뒤 JSON 파일로 만들어 줍니다. | "홈브류 캐릭터(또는 홈브류 시트)를 만들고 싶다"고 말하고, 머릿속 아이디어를 두서없이 클로드 대화창에 써넣으세요. 클로드가 알아서 스킬을 켜고 홈브류 캐릭터 설계와 디자인을 돕습니다. |
| `botc-quiz-maker` | 퀴즈 메이커 | 마도서 셋팅을 보고 푸는 이야기꾼 룰 퀴즈를 만듭니다. | 퀴즈나 아인슈타인 퍼즐처럼 만들고 싶은 상황 또는 마도서 현황을 클로드 대화창에 글로 쓰세요. |

스킬 이름을 몰라도 됩니다. 평소처럼 질문하면 Claude가 알맞은 스킬을 골라 씁니다.

### 이 플러그인이 지키는 원칙

- **공식으로 확인되지 않은 내용은 사실처럼 말하지 않습니다.** 근거가 없으면 "명시된 것이 없습니다. 다만 저는 ~를 제안합니다"라고 답합니다.
- **공식 정보에는 출처를 붙입니다.** (번역 위키 문서, 용어집 항목, 룰북, TPI 공식 답변 등)
- **공식 한글 용어만 씁니다.** 능력 문구는 누가·언제·무엇을·어떻게를 엄밀하게 나눠 해석합니다.

자세한 원칙은 [운영방침](plugins/all-about-botc/skills/botc-rules-advisor/references/운영방침.md)에 있습니다.

### 들어 있는 자료

| 자료 | 내용 |
|---|---|
| [번역 위키](plugins/all-about-botc/skills/botc-rules-advisor/references/wiki/INDEX.md) | 공식 위키 캐릭터 181종 + 규칙 문서 한국어판 ([웹사이트](https://castleq.github.io/botc-wiki-ko/)) |
| [기타 예외 규칙](plugins/all-about-botc/skills/botc-rules-advisor/references/기타예외규칙.md) | 이야기꾼 판단 원칙, TPI 공식 답변, 비공인 징크스, 룰 해석 기록 |
| [공식 용어집](plugins/all-about-botc/skills/botc-rules-advisor/references/Glossary_filled.csv) | 영문 ↔ 한글 공식어 |
| 룰북 | [한국어](plugins/all-about-botc/skills/botc-rules-advisor/references/rulebook-ko.md) · [영어](plugins/all-about-botc/skills/botc-rules-advisor/references/rulebook-en.md) |
| [홈브류 캐릭터 설계 안내서](plugins/all-about-botc/skills/botc-homebrew-design/references/홈브류_캐릭터_설계_안내서.md) | 중국 커뮤니티 원문(원작자 미상)의 한국어판 |
| [커스텀 스크립트 가이드 (영어)](plugins/all-about-botc/skills/botc-script-analysis/custom-script-guide-nqt.md) | Not Quite Tangible의 스크립트 설계 가이드 |
| [영상 콘텐츠 제작 가이드](plugins/all-about-botc/skills/botc-rules-advisor/references/video-content-guide.md) | TPI 영상 제작·사용 가이드 요약 |
| [시계피 입문 가이드 (PDF)](assets/Blood_on_the_Clocktower_Guide_KR.pdf) | 사람이 보는 한국어 입문 슬라이드 |

---

## 설치방법

### claude.ai (웹·데스크톱 앱) — 코딩 몰라도 됩니다

1. claude.ai에서 **Customize → Plugins**로 갑니다.
2. **Add → Add marketplace**를 누르고 `CastleQ/All_about_BOTC`를 입력합니다.
3. 목록에 나타난 **all-about-botc**를 **Add**합니다.

설치하면 같은 계정의 claude.ai 채팅, 데스크톱 앱, Claude Code 어디서나 쓸 수 있습니다. 새 버전이 나오면 Plugins 화면의 **Check for updates**로 받습니다.

### Claude Code (터미널)

```
/plugin marketplace add CastleQ/All_about_BOTC
/plugin install all-about-botc@all-about-botc
```

---

## 기여하기 — 함께 지식을 쌓아 주세요

이 플러그인은 끝이 없는 프로젝트입니다. 커뮤니티가 함께 쌓을수록 더 정확해집니다.

| 이런 것을 알고 있다면 | 이렇게 보내 주세요 |
|---|---|
| TPI 공식 답변, 공식 위키에 없는 판정, 새 비공인 징크스 | [예외 규칙 제보](https://github.com/CastleQ/All_about_BOTC/issues/new?template=exception-rule.yml) |
| 번역 위키·용어·룰북의 오역, 잘못된 판정 | [오류 신고](https://github.com/CastleQ/All_about_BOTC/issues/new?template=error-report.yml) |
| 새 스킬·기능 아이디어 | [아이디어 제안](https://github.com/CastleQ/All_about_BOTC/issues/new?template=idea.yml) |

- 제보는 기록 전에 확인합니다. **TPI 공식 답변은 누구나 확인할 수 있는 링크(디스코드 메시지 링크, 레딧 글, 공식 사이트 등)가 있어야** 공식으로 기록됩니다. 링크가 없으면 "룰 해석"이나 "진행 지침"으로 분류합니다.
- 확인된 제보는 [기타 예외 규칙](plugins/all-about-botc/skills/botc-rules-advisor/references/기타예외규칙.md)에 기록됩니다.
- 파일을 직접 고칠 수 있다면 Pull Request도 환영합니다.

---

## 만든 사람

**CastleQ** — 시계피 이야기꾼

- 2023년 입문, 온·오프라인 수백 시간 플레이, 사회(진행) 수백 회
- 이야기꾼 웹 도구 개발: [포켓 그리모어 플러스+](https://castleq.github.io/pocket-grimoire/) (한국어 가상 그리모어), [번역 위키](https://castleq.github.io/botc-wiki-ko/), [서번트 명제 생성기](https://github.com/CastleQ/BOTC-Savant-generator), [기억상실자 능력 생성기](https://github.com/CastleQ/BOTC-Amnesiac-Abilities-Generator)
- 제작사(TPI) 공식 오픈소스 한글화 작업 기여
- 포켓몬·반지의 제왕 등 홈브류 스크립트 제작·무료 공유
- 2026년 2월부터 시계피 사회 무료 재능기부 진행

---

## 알려 두는 점

- 비공식 커뮤니티 자료입니다. 게임 규칙의 최종 근거는 영어 원문 [공식 위키](https://wiki.bloodontheclocktower.com/)와 TPI 공식 자료입니다.
- 캐릭터 문서 번역은 TPI의 Community Created Content 정책에 따른 것입니다.
- 각 자료의 권리는 원작자에게 있습니다. 출처는 각 문서 머리에 적혀 있습니다.

---

<img src="assets/community-created-content.png" alt="Community Created Content" width="300">

공식 롤 아이콘은 The Pandemonium Institute의 저작물이며, Community Created Content 정책에 따라 사용합니다. 이 프로젝트는 Pandemonium Institute와 관련이 없습니다.
