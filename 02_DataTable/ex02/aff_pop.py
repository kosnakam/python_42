from load_csv import load
import matplotlib.pyplot as plt


def convert_float(arg: str) -> float:
    if isinstance(arg, str) and arg.endswith('M'):
        return float(arg[:-1]) * 1000000
    elif isinstance(arg, str) and arg.endswith('k'):
        return float(arg[:-1]) * 1000
    else:
        return float(arg)


def main():
    """Main function to read CSV files and create graphs."""
    # try:
    df = load("population_total.csv")
    countries = ["France", "Japan"]
    data = df[df['country'].isin(countries)]

    print(type(data))

    # for line in data[0, 1:]:
    #     print(data[line])
        # data[col] = data[col].apply(convert_float)

    # years = [int(y) for y in data.columns[1:-50]]
    # values1 = data.iloc[0, 1:-50]
    # values2 = data.iloc[1, 1:-50]
    # yticks = list(range(int(min(values1.min(), values2.min())), int(max(values1.max(), values2.max())), 20))
    # xticks = list(range(min(years), max(years), 40))

    # plt.figure(figsize=(8, 6))
    # plt.plot(years, values1)
    # plt.plot(values2)
    # plt.show()

    # except Exception as e:
    #     print(f"Error(main): {e}")


if __name__ == "__main__":
    main()
