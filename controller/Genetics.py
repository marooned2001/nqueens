import sys
from pathlib import Path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))
from model.board import Board

community = []

for _ in range(300):
    community.append(Board(8))

print(community)