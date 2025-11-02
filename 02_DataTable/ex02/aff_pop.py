from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


THOUSAND = 1_000
MILLION = 1_000_000
BILLION = 1_000_000_000

X_INTERVAL = 40
Y_INTERVAL = 20_000_000


def convert_float(arg):
    if arg.isalpha():
        return arg
    if isinstance(arg, str) and arg.endswith('B'):
        return float(arg[:-1]) * BILLION
    elif isinstance(arg, str) and arg.endswith('M'):
        return float(arg[:-1]) * MILLION
    elif isinstance(arg, str) and arg.endswith('k'):
        return float(arg[:-1]) * THOUSAND
    else:
        return float(arg)


def millions_formatter(x, pos):
    return f'{int(x / MILLION)}M'


def load_and_prepare_data(filename, countries):
    df = load(filename)
    countries = sorted(countries)
    data = df[df["country"].isin(countries)].copy()
    for col in data.columns[1:]:
        data[col] = data[col].apply(convert_float)
    years = [int(y) for y in data.columns[1:-50]]
    values = [data.iloc[i, 1:-50] for i in range(data.shape[0])]
    return years, values, countries


def get_ticks(values, years, Y_INTERVAL):
    xticks = list(range(min(years), max(years), X_INTERVAL))
    start = Y_INTERVAL
    # start = int(min(v.min() for v in values))
    end = int(max(v.max() for v in values))
    yticks = list(range(start, end, Y_INTERVAL))
    return xticks, yticks


def plot_population(years, values, countries, xticks, yticks):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    for index, value in enumerate(values):
        ax.plot(years, value, label=countries[index])
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(millions_formatter))
    ax.set_title("Population Projections")
    ax.set_ylabel("Population")
    ax.set_xlabel("Year")
    ax.legend(loc="lower right")
    plt.show()


def main():
    """Main function to read CSV files and create graphs."""
    try:
        years, values, countries = load_and_prepare_data(
            "population_total.csv",
            ["France", "Belgium"]
            )
        xticks, yticks = get_ticks(values, years, Y_INTERVAL)
        plot_population(years, values, countries, xticks, yticks)

    except Exception as e:
        print(f"Error(main): {e}")


if __name__ == "__main__":
    main()
