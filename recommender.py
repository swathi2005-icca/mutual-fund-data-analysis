import pandas as pd


def recommend_funds(risk_appetite):
    performance = pd.read_csv(
        "data/processed/09_scheme_performance.csv"
    )

    risk_map = {
        "Low": "Low",
        "Moderate": "Moderate",
        "High": "Very High"
    }

    risk_grade = risk_map.get(risk_appetite)

    if risk_grade is None:
        print("Risk appetite must be Low, Moderate, or High.")
        return

    recommendations = (
        performance[
            performance["risk_grade"] == risk_grade
        ]
        .sort_values("sharpe_ratio", ascending=False)
        .head(3)
    )

    print("\nRecommended Funds:")
    print(
        recommendations[
            [
                "scheme_name",
                "category",
                "risk_grade",
                "sharpe_ratio",
                "return_3yr_pct"
            ]
        ].to_string(index=False)
    )


if __name__ == "__main__":
    risk = input(
        "Enter risk appetite (Low / Moderate / High): "
    )

    recommend_funds(risk)