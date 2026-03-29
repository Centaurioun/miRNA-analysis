import csv
from pathlib import Path

base = Path("/Users/centaurioun/Repos/miRNA-analysis/NewAgents-Skills/_cleanup_reports")
ex = base / "executed_moves_20260325_080239.csv"
rt = base / "retained_items_20260325_080239.csv"
rb = base / "rollback_map_20260325_080239.csv"

rows = list(csv.DictReader(ex.open()))
rrows = list(csv.DictReader(rt.open()))
rbrows = list(csv.DictReader(rb.open()))
coll = sum(1 for r in rows if r.get("collision_resolved") == "yes")

print(f"executed={len(rows)}")
print(f"retained={len(rrows)}")
print(f"rollback={len(rbrows)}")
print(f"collisions={coll}")
print("-- moved sample --")
for r in rows[:15]:
    print(f"{r['source']} -> {r['destination']}")
print("-- retained sample --")
for r in rrows[:15]:
    print(f"{r['path']} | {r['category']}")
