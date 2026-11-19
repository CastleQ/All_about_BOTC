"""PDF용 HTML의 캐릭터 이름을 한글 번역 위키 링크(<a>)로 감싼다.

사용: python3 link_names.py <INDEX.md 경로> <입력.html> <출력.html>
- 이름은 INDEX.md 캐릭터 표(이름 | 영문 | id | 유형 ...)에서 읽는다.
- 긴 이름부터 바꾸고, 다른 낱말 속 이름(예: "대부분" 속 "대부")은 바꾸지 않는다.
- 태그 속성, 이미 있는 <a>, <style>, <title> 안은 건드리지 않는다.
- 주민·외지인은 class="good"(파란색), 하수인·악마는 class="evil"(빨간색). 여행자·전설·설화는 class 없음.
- 끝나면 HTML의 모든 위키 링크 id가 INDEX.md에 있는지 확인한다.
"""
import re
import sys

URL = "https://castleq.github.io/botc-wiki-ko/c/{}.html"
TYPES = {"주민", "외지인", "하수인", "악마", "여행자", "전설", "설화"}
TEAM = {"주민": "good", "외지인": "good", "하수인": "evil", "악마": "evil"}
# 이름 바로 뒤에 붙어도 되는 조사. 이 밖의 한글이 붙으면 다른 낱말로 본다.
# shortcut: 조사 목록에 없는 어미가 붙은 이름은 링크가 빠진다. 빠지는 사례가 보이면 목록에 더한다.
JOSA = "으로서|으로|에게서|에게|한테|까지|부터|처럼|보다|이나|이랑|과의|와의|의|은|는|이|가|을|를|와|과|에|로|도|만|랑|나|님"
HANGUL = "가-힣"


def load(index_path):
    names = {}
    for line in open(index_path, encoding="utf-8"):
        c = [x.strip() for x in line.split("|")]
        if len(c) > 5 and c[4] in TYPES and re.fullmatch(r"[a-z_]+", c[3]):
            names[c[1]] = (c[3], TEAM.get(c[4]))
    return names


def link(html, names):
    alt = "|".join(re.escape(n) for n in sorted(names, key=len, reverse=True))
    pat = re.compile(rf"(?<![{HANGUL}])({alt})(?=(?:{JOSA})?(?![{HANGUL}]))")
    out, skip = [], 0
    for part in re.split(r"(<[^>]+>)", html):
        if part.startswith("<"):
            tag = re.match(r"</?\s*(\w+)", part)
            if tag and tag.group(1).lower() in ("a", "style", "title", "script"):
                skip += -1 if part.startswith("</") else 1
            out.append(part)
        elif skip > 0:
            out.append(part)
        else:
            out.append(pat.sub(lambda m: tag_for(m.group(1), names), part))
    return "".join(out)


def tag_for(name, names):
    cid, team = names[name]
    cls = f' class="{team}"' if team else ""
    return f'<a{cls} href="{URL.format(cid)}">{name}</a>'


def check(html, names):
    ids = {cid for cid, _ in names.values()}
    bad = [i for i in re.findall(r"botc-wiki-ko/c/([^\".]+)\.html", html) if i not in ids]
    assert not bad, f"INDEX.md에 없는 id: {bad}"


if __name__ == "__main__":
    if sys.argv[1:] == ["--test"]:
        n = {"대부": ("godfather", "evil"), "노 다시": ("nodashii", "evil"), "노": ("x", "good"), "세탁부": ("washerwoman", "good"), "기사": ("knight", None)}
        r = link("<p>대부분 대부가 노 다시를 <b>대부</b>.</p><a href='#'>대부</a>", n)
        assert r.count("godfather") == 2 and "대부분" in r and "nodashii" in r and "/x." not in r, r
        r2 = link("<p>세탁부와 기사</p>", n)
        assert 'class="good" href="https://castleq.github.io/botc-wiki-ko/c/washerwoman.html"' in r2 and '<a href="https://castleq.github.io/botc-wiki-ko/c/knight.html">' in r2, r2
        print("ok")
        sys.exit()
    names = load(sys.argv[1])
    html = link(open(sys.argv[2], encoding="utf-8").read(), names)
    check(html, names)
    open(sys.argv[3], "w", encoding="utf-8").write(html)
    print(f"링크 {html.count('botc-wiki-ko/c/')}개, id 확인 완료")
