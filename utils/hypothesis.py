from scipy import stats

ALPHA = 0.05
def check_mean_value_hypothesis(df, attribute_name, hypothesis):
    _, p_val = stats.ttest_1samp(df[attribute_name], hypothesis, nan_policy="omit")
    print(f"sprawdzanie hipotezy o średniej wartości dla atrybutu {attribute_name} wynoszącej {hypothesis}")
    if p_val > ALPHA:
        print(
            f"P-wartość={'{0:.2f}'.format(p_val)} jest wyższa niż przyjęty poziom istotności statystycznej={ALPHA}. Nie ma podstaw do odrzucenia hipotezy.")
    else:
        print(
            f"P-wartość={'{0:.4f}'.format(p_val)} jest niższa niż przyjęty poziom istotności statystycznej={ALPHA}. Hipotezę odrzucamy, ponieważ różnice są istotne statystycznie.")