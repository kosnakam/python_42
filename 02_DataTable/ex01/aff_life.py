from load_csv import load


def main():
    df = load("life_expectancy_years.csv")
    print(df)
    return


if __name__ == "__main__":
    main()
