from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Main function to read CSV files and create graphs."""
    try:
        df = load("life_expectancy_years.csv")
        country = "Japan"
        data = df[df['country'] == country]
        years = [int(y) for y in data.columns[1:]]
        values = data.iloc[0, 1:].astype(float)
        xticks = list(range(min(years), max(years), 40))

        plt.figure(figsize=(8, 6))
        plt.plot(years, values, label=country)
        plt.xticks(xticks)
        plt.title(f"{country} Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.show()

    except Exception as e:
        print(f"Error(main): {e}")


if __name__ == "__main__":
    main()
