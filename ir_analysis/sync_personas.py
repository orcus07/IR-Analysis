"""내 다른 레포의 페르소나를 config/personas/imported/ 로 동기화.

config/config.yaml 에 소스를 적는다:
  persona_repos:
    - "orcus07/다른레포:personas"        # "owner/repo:디렉터리" (디렉터리 생략 가능)

사용:
  python -m ir_analysis.sync_personas

- YAML(.yaml/.yml)은 그대로, 마크다운/텍스트(.md/.txt)는 전문을 viewpoint 로
  감싼 페르소나 YAML 로 변환해 저장한다. 파일명은 "레포명__파일명.yaml".
- 프라이빗 레포는 GH_TOKEN 또는 GITHUB_TOKEN 환경변수(해당 레포 read 권한) 필요.
  퍼블릭 레포는 토큰 없이 된다.
"""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config" / "config.yaml"
IMPORT_DIR = ROOT / "config" / "personas" / "imported"

_EXTS = (".yaml", ".yml", ".md", ".txt")


def _fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={
        "User-Agent": "ir-analysis",
        "Accept": "application/vnd.github+json",
    })
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def _slug(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9가-힣]+", "-", text).strip("-").lower() or "persona"


def _discover_files(repo: str, path: str) -> list[dict]:
    """대상 파일 목록. 경로를 지정하면 그 디렉터리, 비우면 레포 전체 트리에서
    persona/prompt/agent 냄새가 나는 파일을 찾고, 없으면 루트의 파일을 쓴다."""
    if path:
        listing = json.loads(_fetch(
            f"https://api.github.com/repos/{repo}/contents/{path}"))
        if isinstance(listing, dict):
            listing = [listing]
        return [i for i in listing if i.get("type") == "file"]

    tree = json.loads(_fetch(
        f"https://api.github.com/repos/{repo}/git/trees/HEAD?recursive=1"))
    hits: list[dict] = []
    root: list[dict] = []
    for node in tree.get("tree", []):
        p = node.get("path", "")
        if node.get("type") != "blob" or not p.lower().endswith(_EXTS):
            continue
        entry = {
            "name": p.rsplit("/", 1)[-1],
            "download_url": f"https://raw.githubusercontent.com/{repo}/HEAD/{p}",
        }
        if any(k in p.lower() for k in ("persona", "prompt", "agent", "관점")):
            hits.append(entry)
        elif "/" not in p:
            root.append(entry)
    return (hits or root)[:40]  # 과다 수집 방지


def sync_repo(spec: str) -> int:
    repo, _, path = spec.partition(":")
    count = 0
    prefix = _slug(repo.split("/")[-1])
    for item in _discover_files(repo, path):
        name = item.get("name", "")
        if not name.lower().endswith(_EXTS):
            continue
        raw = _fetch(item["download_url"])
        stem = _slug(name.rsplit(".", 1)[0])
        out = IMPORT_DIR / f"{prefix}__{stem}.yaml"
        if name.lower().endswith((".yaml", ".yml")):
            data = yaml.safe_load(raw)
            if not (isinstance(data, dict) and data.get("viewpoint")):
                print(f"  건너뜀(페르소나 형식 아님): {repo}/{name}", file=sys.stderr)
                continue
            out.write_text(raw, encoding="utf-8")
        else:
            data = {
                "name": stem,
                "viewpoint": raw.strip()[:6000],
                "output_language": "한국어",
            }
            out.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False),
                           encoding="utf-8")
        print(f"  ✔ {repo}/{name} → {out.name}")
        count += 1
    return count


def main() -> None:
    cfg = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8")) or {}
    repos = cfg.get("persona_repos") or []
    if not repos:
        print("config.yaml 의 persona_repos 가 비어 있다 — 동기화할 소스 없음.")
        return
    IMPORT_DIR.mkdir(parents=True, exist_ok=True)
    total = 0
    for spec in repos:
        print(f"▶ {spec}")
        try:
            total += sync_repo(str(spec))
        except Exception as e:
            print(f"  ✖ 실패: {e}", file=sys.stderr)
    print(f"완료: 페르소나 {total}개 → {IMPORT_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
