
from frenchdeck import FrenchDeck, Card

def test_len_and_getitem():
    deck = FrenchDeck()
    assert len(deck) == 52
    assert isinstance(deck[0], Card)
    assert deck[:5][0].rank in FrenchDeck.ranks
