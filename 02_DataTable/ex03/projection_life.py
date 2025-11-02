from load_csv import load
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt


def thousand_formatter(x, pos) -> str:
    """Change the way thousand are expressed."""
    if x == 300:
        return "300"
    return f"{int(x / 1000)}k"


def main():
    try:
        """Read the CSV files, prepare it, and draw graph."""
        df_incom = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
            )
        df_life = load("life_expectancy_years.csv")

        data_incom = df_incom["1900"]
        data_life = df_life["1900"]

        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(1, 1, 1)
        ax.scatter(data_incom, data_life)
        ax.set_xscale("log")
        ax.set_xticks([300, 1000, 10000])
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(thousand_formatter))
        ax.set_title("1900")
        ax.set_ylabel("Life Expectancy")
        ax.set_xlabel("Gross domestic product")
        plt.show()

    except Exception as e:
        print(f"Error(main): {e}")
        return


if __name__ == "__main__":
    main()
