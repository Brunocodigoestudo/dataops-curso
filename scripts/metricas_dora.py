"""Métricas DORA do projeto a partir da API do GitHub."""

import os
from collections import Counter
from datetime import date, datetime
from statistics import median

import requests

REPO = "Brunocodigoestudo/dataops-curso"
API = f"https://api.github.com/repos/{REPO}"


def buscar(caminho: str, params: dict) -> dict | list:
    headers = {"Accept": "application/vnd.github+json"}
    token = os.getenv("GITHUB_TOKEN")  # opcional em repositório público
    if token:
        headers["Authorization"] = f"Bearer {token}"
    resposta = requests.get(
        f"{API}/{caminho}", headers=headers, params=params, timeout=30
    )
    resposta.raise_for_status()
    return resposta.json()


def horas_entre(inicio: str, fim: str) -> float:
    i = datetime.fromisoformat(inicio)
    f = datetime.fromisoformat(fim)
    return (f - i).total_seconds() / 3600


def deploys_por_semana(runs: list[dict]) -> dict[str, int]:
    """Deployment frequency: execuções com sucesso do cd.yml, por semana."""
    por_semana = Counter()
    for r in runs:
        ano, semana, _ = date.fromisoformat(r["created_at"][:10]).isocalendar()
        por_semana[f"{ano}-S{semana:02d}"] += 1
    return dict(sorted(por_semana.items()))


def lead_time_horas(prs: list[dict]) -> float | None:
    """Lead time aproximado: mediana do tempo entre abrir o PR e fazer o merge."""
    tempos = [
        horas_entre(p["created_at"], p["merged_at"]) for p in prs if p.get("merged_at")
    ]
    return median(tempos) if tempos else None


def recuperacao_horas(issues: list[dict]) -> float | None:
    """MTTR: mediana do tempo entre abrir e fechar issues com a label incidente."""
    tempos = [
        horas_entre(i["created_at"], i["closed_at"])
        for i in issues
        if i.get("closed_at")
        and "pull_request" not in i  # a API de issues também devolve PRs
    ]
    return median(tempos) if tempos else None


def main() -> None:
    runs = buscar(
        "actions/workflows/cd.yml/runs",
        {"branch": "main", "status": "success", "per_page": 100},
    )["workflow_runs"]
    prs = buscar("pulls", {"state": "closed", "per_page": 100})
    incidentes = buscar(
        "issues", {"labels": "incidente", "state": "closed", "per_page": 100}
    )

    print("Deployment frequency (deploys por semana):")
    for semana, total in deploys_por_semana(runs).items():
        print(f"  {semana}: {total}")
    print(f"Lead time (mediana, horas): {lead_time_horas(prs)}")
    print(f"Tempo de recuperação (mediana, horas): {recuperacao_horas(incidentes)}")


if __name__ == "__main__":
    main()
