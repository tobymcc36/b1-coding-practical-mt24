import pandas as pd

class Mission:
    def __init__(self, reference, cave_height, cave_depth):
        self.reference = reference
        self.cave_height = cave_height
        self.cave_depth = cave_depth

    @classmethod
    def from_csv(cls, filepath):
        df = pd.read_csv(filepath)
        required_cols = {"reference", "cave_height", "cave_depth"}
        if not required_cols.issubset(df.columns):
            raise ValueError(f"CSV must contain columns: {required_cols}")
        return cls(
            reference=df["reference"],
            cave_height=df["cave_height"],
            cave_depth=df["cave_depth"]
        )

    def __repr__(self):
        return f"<Mission with {len(self.reference)} entries>"