import pandas as pd


def load(path: str) -> pd.core.frame.DataFrame:
    """Reads the specified file and returns it."""
    try:
        assert type(path) is str, "This argument is not accepted."

        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df

    except (AssertionError, FileNotFoundError,
            pd.errors.EmptyDataError, pd.errors.ParserError) as e:
        print(f"Error(load): {e}")
        return None
