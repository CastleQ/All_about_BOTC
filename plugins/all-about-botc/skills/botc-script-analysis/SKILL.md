---
name: botc-script-analysis
description: BOTC 커스텀 스크립트(캐릭터 시트 이미지·JSON)를 인원별 선악 밸런스·플레이 경험·존재감 기준으로 분석하고, 결과를 제목 달린 캡처형 PNG(원본 zip 포함)나 PDF로 만들 때 사용.
---

# BOTC 커스텀 스크립트 분석 + 캡처형 이미지 제작

사용자가 시계탑에 흐른 피(BOTC) 커스텀 시트를 주며 "분석해줘", "밸런스 봐줘", "같은 방식으로 분석" 등을 요청할 때 쓴다. 이미지까지 요청하면(또는 이전에 이미지를 받았던 흐름이면) 2부 이미지 제작까지 진행한다.

## 자료 위치 (이 플러그인)

이 스킬은 같은 플러그인의 `botc-rules-advisor` 스킬 폴더에 있는 자료를 함께 쓴다. 아래에서 `<자료>`는 그 스킬의 `references/` 폴더다.

- 기본 위치: 이 스킬 폴더의 형제 폴더 `../botc-rules-advisor/references/`
- 거기에 없으면 찾는다: `find / -type f -path '*botc-rules-advisor/references/wiki/INDEX.md' 2>/dev/null | head -1`
- 파일 도구를 쓸 수 없는 환경이면 번역 위키 사이트(`https://castleq.github.io/botc-wiki-ko/c/<id>.html`)를 웹에서 연다.

| 자료 | 경로 |
|---|---|
| 운영방침 (답변 원칙의 원본) | `<자료>/운영방침.md` |
| 기타 예외 규칙 | `<자료>/기타예외규칙.md` |
| 공식 용어집 | `<자료>/Glossary_filled.csv` |
| 번역 위키 | `<자료>/wiki/` (`INDEX.md`부터) |
| 커스텀 스크립트 설계 가이드 (영어, Not Quite Tangible) | 이 스킬 폴더의 `custom-script-guide-nqt.md` — 스크립트 구조를 볼 때의 참고 관점(아래 "분석 기준" 1번) |

## 공통 원칙 (운영방침 준수)

- `<자료>/운영방침.md`의 0장 불변 규칙과 1장 용어·출처 표기를 그대로 따른다.
- 모든 출력은 한글. 두괄식(결론 먼저). 답변 끝에 `---`로 구분하고, 사용자의 가정을 짚는 역질문 + 후속 작업 제안을 붙인다.
- 공식 캐릭터명·용어는 `Glossary_filled.csv` 한글 공식용어로만 쓴다. 상태 용어는 취함·중독·**집착**(광기 X).
- 비공식/홈브류 캐릭터·하우스룰은 반드시 출처를 밝히거나 홈브류임을 표기한다. 시트 작성자("지은이")가 보이면 "OO 님이 만든 커스텀 스크립트", 없으면 "작성자 표기가 없는 커스텀 스크립트"라고 밝힌다.
- 밸런스 권장은 `기타예외규칙.md` 0번 원칙(이야기꾼 선택 범위 안에서 선악 유리함을 가급적 맞춘다)에 근거해 쓴다.
- 밸런스 평가는 "실전 데이터가 아니라 이론상 추정"임을 표 제목에 명시한다.

## 분석 기준

1. **설계 가이드는 참고 관점일 뿐이다.** 커스텀 시트 작성·분석의 권장 기준은 Not Quite Tangible「Beginner's guide to Blood on the Clocktower custom scripts」(https://notquitetangible.blogspot.com/2024/07/clocktower-custom-scripts.html, 10개 항목)로 둔다. 다만 초보 제작자용 가이드이지 원칙·진리가 아니므로 판정 근거로 쓰지 않는다. "원칙 N"처럼 법칙인 양 인용하지 않는다.
2. **좋은 플레이 경험·재미는 전 세계 게이머의 일반론으로 판단한다.** BOTC와 소셜 디덕션을 즐기는 사람들이 보편적으로 좋아하고 싫어하는 것을 기준으로 삼는다.
3. **특정 셋업을 권하지 않는다.** 좋은 스크립트는 특정 셋업을 강요할 필요가 없다. 셋업이 적당히 무작위여도 같은 게임 경험이 유지된다(점철되는 혼란, 화단에 꽃피운 이단, 로마의 몰락, 심리사회가 좋은 사례). 특정 셋업이 필수로 따라오는 구조라면 오히려 스크립트의 피드백 포인트로 지적한다. 꼭 필요하면 "홈브류 규칙으로 명시"를 제안한다.
4. **난도 별점** — 플레이어 난도와 이야기꾼 난도를 각각 별점(★ 5점 만점)과 근거로 표기한다.
5. **출처는 공개 자료로 단다.** 분석은 외부에 공유될 수 있으므로, 출처·근거를 사용자만 볼 수 있는 자료(로컬 파일·플러그인 내부 파일명)로 적지 않는다. 영어 원문 위키 문서(각 위키 파일 맨 위 `source` 칸의 주소), 번역 위키 사이트 주소(`page` 칸), 룰북, 공개된 TPI 답변 링크로 적는다.
6. **밀주업자(Bootlegger)는 언급하지 않는다.** 사용자가 따로 요청할 때만 다룬다. 공식 스크립트 도구에 외부 JSON을 한 번이라도 넣어 내보내면 자동으로 붙는 로고이고, 한글 번역 때문에 JSON을 직접 번역해 이미지로만 출력하는 경우가 많아서다.
7. **매 분석은 독립시행이다.** 같은 대화에서 이전에 분석한 다른 시트가 있더라도 비교·대조·언급을 넣지 않는다. 각 분석은 그 시트 하나만 다루는 독립된 자료다.
8. **모자 장수는 단점으로 보지 않는다.** 판을 통째로 새로 짜는 것이 모자 장수의 존재 의의이며, 선한 팀에 처형할지 유보할지의 딜레마를 준다.

# 1부. 분석 방법론

## 1단계: 캐릭터 목록 확정

시트에서 주민·외지인·하수인·악마·전설(설화)과 징크스 아이콘(캐릭터 이름 옆 작은 아이콘)을 모두 읽어 목록화한다. 유형별 개수도 센다.

## 2단계: 번역 위키로 검증 (필수)

위치: `<자료>/wiki/`. `ALL.md`는 이 플러그인에 없으며, 있더라도 읽지 않는다.

**자료 연결 확인 (분석 시작 전 필수):** 위키 파일도, 번역 위키 사이트도 열 수 없으면 분석을 시작하지 말고 먼저 사용자에게 이렇게 되묻는다.

> 자료가 연결되지 않아 분석이 정확하지 않을 수 있습니다. 그래도 만들까요?

- 사용자가 진행을 원하면 그때 분석을 진행한다.
- 둘 중 하나라도 열리면 묻지 않고 바로 진행한다.

1. `INDEX.md`에서 시트의 한글명으로 grep → id·유형·에디션·파일 경로 확보. 이 단계에서 **공식 캐릭터 여부**와 **실험 캐릭터 수**를 확정한다.
2. 시트 캐릭터 파일을 연다.
3. 징크스 추출 — 각 파일의 `## 징크스` 섹션에서 **양쪽 다 시트에 있는** 조합만 남긴다:

```bash
cd "<자료>/wiki/characters"
S="캐릭터1|캐릭터2|..."   # 시트의 한글 캐릭터명 전부
for f in */*.md; do o=$(awk '/^## 징크스/{p=1;next} /^## /{p=0} p' "$f" | grep -E "^- ($S) \+ ($S):"); [ -n "$o" ] && echo "=== $f" && echo "$o"; done
```

   시트의 징크스 아이콘과 위키 결과가 일치하는지 대조해 보고에 적는다.
4. 판정에 핵심인 캐릭터(악마, 외지인 수 변경자, 특이 셋업 캐릭터)는 `## 요약` 불릿을 읽어 세부 규칙을 확인한다:

```bash
awk '/^## 요약/{p=1} /^## 진행/{p=0} p' <파일들> | grep -E "^- "
```

5. 기존 `기타예외규칙.md` 항목(예: 꼭두각시×은둔자, 전도사×꼭두각시)과 연결되는 조합이 있으면 함께 적는다. 자료 간 충돌이 보이면 양쪽 출처를 모두 적고 사용자에게 알린다.

## 3단계: 분석 축

### 기본 인원 구성표 (주민/외지인/하수인/악마)
10인 7/0/2/1 · 11인 7/1/2/1 · 12인 7/2/2/1 · 13인 9/0/3/1 · 14인 9/1/3/1 · 15인 9/2/3/1

### 반드시 따져볼 것
- **정보 vs 오정보 재고 조사:** 첫날 정보 / 매일 정보 / 1회 정보 / 사망 트리거 정보로 분류. 취함·중독·오인식(위장)·집착 원인을 전부 세어 "원인 N개"로 제시.
- **보호·생존 vs 처치 압력:** 보호 캐릭터 수, 악마 처치 빈도, 추가 처치(암살자 등), 처형 방어(악마의 변호사 등). 게임 길이를 추정.
- **외지인 성향:** 시트 외지인이 선에게 이득인지 손해인지 하나씩 판정 → "외지인 수 증가 = 누구 이득"을 결론으로 낸다. 외지인 수 변경자(남작, 팡 구, 카잘리, 잔 등)와 연결.
- **악마별 특징:** 악마끼리 무엇으로 구별되는지(처치 방식/셋업 변형/중독 패턴), 선이 악마를 판별할 단서.
- **인원 스케일링:** 소인원(하수인 2)에서 한 방 카운터(예: 전도사)의 비중, 대인원에서 정보 희석·블러핑 공간·투표력 변화.
- **이야기꾼 레버:** "~할 수도 있습니다"·임의 정보·외지인 ±?·잔의 X·기억상실자 능력 등 밸런스를 좌우하는 이야기꾼 선택지 → 구체적 권장값 제시.
- **이야기꾼 부담:** 실험 캐릭터 수, 첫날 밤 처리량, 집착 판정, 수학자류 집계.

## 4단계: 보고 구조 (이 순서·형식 고정)

1. **결론 문단** — 가장 균형 좋은 인원대, 소/대인원 경향, 핵심 재미(콘셉트), 약점 3가지. 이어서 **플레이어 난도·이야기꾼 난도를 별점(★ 5점 만점)과 근거**로 적는다.
2. **인용 블록** — 작성자/출처, 공식 캐릭터 확인 여부, 실험 캐릭터 수와 목록.
3. `---`
4. `## 1. 구성 요약` — 표(유형 | 구성 | 성격) + 징크스 행 → **중요:** 핵심 구조 통찰(외지인 이득 방향, 오정보 원인 수 등).
5. `## 2. 인원별 선악 밸런스 (실전 데이터가 아니라 이론상 추정)` — 표(악마 × 10~11인/12~13인/14~15인) → 특수 변수 문단 → **인원대별 판단 근거**(불릿) → **이야기꾼 운영 권장** (기타예외규칙 0번 원칙, 번호 목록).
6. `## 3. 좋은 플레이 경험을 만드는 요인` — 굵은 소제목 불릿.
7. `## 4. 나쁜 플레이 경험을 만드는 요인` — 표(요인 | 문제 | 완화 방안).
8. `## 5. 캐릭터별 존재감` — 표(높음/중간/낮음) + 불균형 지점 + "균등 분배가 꼭 정답은 아니다(조용한 캐릭터 = 블러핑 공간)" 관점과 손볼 칸 제안.
9. `## 6. 판정할 때 미리 알아둘 점` — 징크스 위키 원문, 기타예외규칙 연결, 헷갈리기 쉬운 상호작용.
10. `---` + 역질문 + 후속 제안(이미지화, PDF, 문서화 등).


# 2부. 캡처형 이미지 제작

요청 시 분석 답변을 **한 글자도 빠짐없이** 그대로 옮겨 세로로 긴 PNG 한 장으로 만든다.

## 규칙
- 맨 위에 제목: `<h1>{{시트이름}} 분석</h1>` (크게, 굵게). 시트이름은 시트 상단 표기 그대로(예: `Devil's Plan 1.2`, `Who doesn't learn the numbers?`).
- 본문은 답변 원문 그대로 HTML로 옮긴다(요약·수정 금지). 표·불릿·인용·`---` 구분선 구조 유지.
- **항상 PNG + 원본 화질 zip을 함께 보낸다.** (대화창 미리보기는 세로 8000px 초과 시 축소됨)

## HTML 템플릿 (작업 폴더에 저장)

```html
<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<style>
body{margin:0;background:#f5f4ef;font-family:"Noto Sans CJK KR","Noto Sans KR",sans-serif;color:#1f1e1c;}
.wrap{box-sizing:border-box;width:1000px;margin:0 auto;padding:44px 52px 52px;background:#fbfaf6;}
h1{font-size:40px;font-weight:900;line-height:1.3;margin:0 0 28px;padding-bottom:20px;border-bottom:3px solid #1f1e1c;}
p,li{font-size:17px;line-height:1.75;margin:0 0 12px;}
h2{font-size:23px;margin:34px 0 14px;font-weight:700;}
hr{border:none;border-top:1px solid #d9d6cc;margin:30px 0;}
blockquote{margin:0 0 14px;padding:4px 18px;border-left:4px solid #c9c4b6;color:#55524a;}
blockquote p{margin:6px 0;}
table{border-collapse:collapse;width:100%;margin:6px 0 18px;font-size:15.5px;line-height:1.6;}
th,td{border:1px solid #d9d6cc;padding:9px 11px;vertical-align:top;text-align:left;}
td:first-child,th:first-child{white-space:nowrap;}
th{background:#eeebe2;font-weight:700;}
ul,ol{padding-left:26px;margin:0 0 14px;}
ul ul{margin:6px 0 4px;}
li{margin-bottom:6px;}
strong{font-weight:700;}
</style></head><body><div class="wrap">
<h1>{{시트이름}} 분석</h1>
<!-- 답변 본문 그대로 -->
</div></body></html>
```

주의: `.wrap`에 `box-sizing:border-box`가 없으면 가로 스크롤이 생겨 이미지 폭이 두 배가 된다. 첫 열 `nowrap`은 "주민 13" 같은 짧은 라벨이 줄바꿈되는 것을 막는다.

## 렌더링 (Playwright, 사전 설치된 Chromium 사용 — `playwright install` 금지)

Playwright나 Chromium이 없는 환경이면 이미지 대신 HTML 파일을 전달하고, 브라우저에서 열어 캡처하면 된다고 안내한다.

```bash
cd <작업 폴더> && mkdir -p out && python3 -c "
from playwright.sync_api import sync_playwright
import os
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1000,'height':800},device_scale_factor=2)
    pg.goto('file://'+os.path.abspath('cap.html')); pg.wait_for_timeout(500)
    pg.screenshot(path='out/<파일명>_분석.png',full_page=True); b.close()
"
```

- 결과 폭은 2000px이어야 한다(아니면 레이아웃 오버플로 → 수정 후 재렌더).
- 파일명: 시트이름을 영문/숫자/밑줄로 정리 + `_분석.png` (예: `Devils_Plan_1.2_분석.png`).

## PDF로 원할 때

사용자가 PDF를 원하면 같은 HTML을 PDF로도 저장한다. 표가 페이지 경계에서 잘리지 않게 `tr{page-break-inside:avoid}`를 스타일에 더한다.

```bash
cd <작업 폴더> && python3 -c "
from playwright.sync_api import sync_playwright
import os
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page()
    pg.goto('file://'+os.path.abspath('cap.html')); pg.wait_for_timeout(500)
    pg.pdf(path='out/<파일명>_분석.pdf',format='A4',print_background=True,margin={'top':'12mm','bottom':'12mm','left':'10mm','right':'10mm'}); b.close()
"
```

## 검수

이미지를 3등분 크롭·축소해 Read로 직접 보고, 글자 깨짐·표 줄바꿈·누락이 없는지 확인한다:

```bash
python3 -c "
from PIL import Image
im=Image.open('out/<파일명>_분석.png');w,h=im.size
for i in range(3): im.crop((0,i*h//3,w,(i+1)*h//3)).resize((1000,h//6)).save(f'q{i}.png')
"
```

## 전달

1. 무압축 zip 생성: `zip -0 -q out/<묶음이름>_원본.zip out/<파일명>_분석.png ...` → `unzip -l`로 확인.
2. PNG와 zip을 **함께** 사용자에게 파일로 보낸다.
3. 답변에 원본 해상도(가로×세로 px)를 적는다. 미리보기가 축소됐다면 zip이 원본임을 한 줄로 알린다.
