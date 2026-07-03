"""누적 보고서 렌더 빌더.

analyses/*.md 를 읽어 docs/index.html (자급식 뷰어, CDN 불필요) 하나로 만든다.
GitHub Pages(docs/) 나 모바일 브라우저 render 로 그대로 열 수 있다.

사용:
  python -m render.build
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ANALYSES_DIR = ROOT / "analyses"
PERSONA_DIR = ROOT / "config" / "personas"
TEMPLATE_PATH = Path(__file__).resolve().parent / "template.html"
OUT_PATH = ROOT / "docs" / "index.html"

_FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)


def parse_report(path: Path) -> dict:
    """보고서 1건 → 메타 + 본문. 프런트매터가 없으면 파일명·첫 제목에서 유추한다."""
    text = path.read_text(encoding="utf-8")
    meta: dict = {}
    m = _FRONT_MATTER.match(text)
    if m:
        meta = yaml.safe_load(m.group(1)) or {}
        text = text[m.end():]

    stem_parts = path.stem.split("_")  # 관례: YYYY-MM-DD_대상_페르소나.md
    heading = re.search(r"^#\s+(.+)$", text, re.M)
    meta.setdefault("date", stem_parts[0])
    meta.setdefault("title", heading.group(1).strip() if heading else path.stem)
    meta.setdefault("target", stem_parts[1] if len(stem_parts) > 1 else "-")
    meta.setdefault("persona", stem_parts[2] if len(stem_parts) > 2 else "-")

    return {
        "id": path.stem,
        "title": str(meta["title"]),
        "date": str(meta["date"]),
        "target": str(meta["target"]),
        "persona": str(meta["persona"]),
        "scope": str(meta.get("scope", "")),
        "quarter": str(meta.get("quarter_anchor", "")),
        "md": text.strip(),
    }


def _git(*args: str) -> str:
    return subprocess.check_output(["git", "-C", str(ROOT), *args],
                                   text=True).strip()


def build_config() -> dict:
    """'새 분석 실행' 패널이 쓰는 저장소·워크플로 정보. git/CI 환경에서 유추한다."""
    owner, repo = "orcus07", "IR-Analysis"
    try:
        url = re.sub(r"\.git$", "", _git("remote", "get-url", "origin")).rstrip("/")
        owner, repo = url.split("/")[-2:]
    except Exception:
        pass
    # CI(detached HEAD)에서는 git보다 환경변수가 정확하다.
    branch = (os.environ.get("GITHUB_REF_NAME")        # GitHub Actions
              or os.environ.get("RENDER_GIT_BRANCH"))  # render.com
    if not branch:
        try:
            branch = _git("rev-parse", "--abbrev-ref", "HEAD")
        except Exception:
            branch = "main"
    if branch == "HEAD":  # detached
        branch = "main"
    personas = sorted(p.stem for p in PERSONA_DIR.rglob("*.yaml")
                      if not p.stem.startswith("_"))  # imported/ 포함
    return {"owner": owner, "repo": repo, "branch": branch,
            "workflow": "analyze.yml", "personas": personas}


def main() -> None:
    paths = sorted(ANALYSES_DIR.glob("*.md"))
    if not paths:
        sys.exit("analyses/ 에 보고서가 없습니다.")
    reports = sorted((parse_report(p) for p in paths),
                     key=lambda r: r["date"], reverse=True)

    payload = json.dumps(reports, ensure_ascii=False)
    payload = payload.replace("</", "<\\/")  # </script> 조기 종료 방지
    config = json.dumps(build_config(), ensure_ascii=False)
    html = TEMPLATE_PATH.read_text(encoding="utf-8").replace(
        "/*__DATA__*/",
        f"const REPORTS = {payload};\nconst CONFIG = {config};")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(html, encoding="utf-8")
    print(f"✔ {OUT_PATH.relative_to(ROOT)}  (보고서 {len(reports)}건)")


if __name__ == "__main__":
    main()
