import tailwiz
import pandas as pd


def test_classify_no_training_data():
    results = tailwiz.classify(
        pd.DataFrame(['I hate you', 'You are my best friend'], columns=['text']),
        None,
        False
    )
    assert 'label_from_tailwiz' in results.columns
    assert len(results) == 2
    assert sorted(list(set(results.label_from_tailwiz.tolist()))) == [0, 1]


def test_classify():
    results = tailwiz.classify(
        pd.DataFrame(['I hate you'], columns=['text']),
        pd.DataFrame([['You are ugly', 0], ['Lovely weather today!', 1], ['Everything sucks', 0]], columns=['text', 'label']),
        False
    )
    assert 'label_from_tailwiz' in results.columns
    assert len(results) == 1
    assert results.label_from_tailwiz.iloc[0] == 0


def test_classify_with_metrics():
    results, metrics = tailwiz.classify(
        pd.DataFrame(['I hate you'], columns=['text']),
        pd.DataFrame([['You are ugly', 0], ['Lovely weather today!', 1], ['Everything sucks', 0]], columns=['text', 'label']),
        True
    )
    assert 'label_from_tailwiz' in results.columns
    assert len(results) == 1
    assert results.label_from_tailwiz.iloc[0] == 0
    assert metrics is not None
    assert 'acc' in metrics
    assert type(metrics['acc']) == dict
    assert type(metrics['acc'][0]) == float


def test_classify_multi():
    results = tailwiz.classify(
        pd.DataFrame(['Not in a million years.'], columns=['text']),
        pd.DataFrame([['I am positive!', 0], ['No. Absolutely not.', 1], ['Hm, I am not sure.', 2]], columns=['text', 'label']),
        False
    )
    assert 'label_from_tailwiz' in results.columns
    assert len(results) == 1
    assert results.label_from_tailwiz.iloc[0] in (0, 1, 2)


def test_classify_multi_with_metrics():
    results, metrics = tailwiz.classify(
        pd.DataFrame(['Not in a million years.'], columns=['text']),
        pd.DataFrame([['I am positive!', 0], ['No. Absolutely not.', 1], ['Hm, I am not sure.', 2]], columns=['text', 'label']),
        True
    )
    assert 'label_from_tailwiz' in results.columns
    assert len(results) == 1
    assert results.label_from_tailwiz.iloc[0] in (0, 1, 2)
    assert metrics is not None
    assert 'acc' in metrics
    assert type(metrics['acc']) == dict
    assert type(metrics['acc'][0]) == float