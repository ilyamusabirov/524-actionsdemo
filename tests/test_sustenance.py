from vancouver_survival.sustenance import recommend_beverage


def test_recommend_beverage():
    assert recommend_beverage(1.0) == "Iced Americano"
    assert recommend_beverage(5.0) == "Hot Coffee"
    # Intentionally omitting the Hot Chocolate case (> 8) for partial coverage
