class Hand():
    def __init__(self, cards):
        self.cards = cards

    @property
    def _hand_validation_from_best_to_worst(self):
        return (
            ('Royal Flush', self._royal_flush),
            ('Straight Flush', self._straight_flush),
            ('Four of a Kind', self._four_of_a_kind),
            ('Full House', self._full_house),
            ('Flush', self._flush),
            ('Straight', self._straight),
            ('Three of a Kind', self._three_of_a_kind),
            ('Two Pair', self._two_pair),
            ('Pair', self._pair),
            ('High Card', self._high_card)
        )

    def best_rank(self):
        for rank in self._hand_validation_from_best_to_worst:
            hand_name, validator_method = rank
            if validator_method():
                return hand_name

    def _royal_flush(self):
        pass

    def _straight_flush(self):
        pass

    def _four_of_a_kind(self):
        four_of_a_kind = self._ranks_with_count(4)
        return len(four_of_a_kind) == 1

    def _full_house(self):
        pass

    def _flush(self):
        pass

    def _straight(self):
        pass

    def _three_of_a_kind(self):
        three_of_a_kind = self._ranks_with_count(3)
        return len(three_of_a_kind) == 1

    def _two_pair(self):
        two_pair = self._ranks_with_count(2)
        return len(two_pair) == 2

    def _pair(self):
        pair = self._ranks_with_count(2)
        return len(pair) == 1

    def _high_card(self):
        return True

    def _ranks_with_count(self, count):
        return {
            rank: rank_count
            for rank, rank_count in self._card_rank_counts.items()
            if rank_count == count
        }

    @property
    def _card_rank_counts(self):
        card_rank_counts = {}
        for card in self.cards:
            card_rank_counts.setdefault(card.rank, 0)
            card_rank_counts[card.rank] += 1
        return card_rank_counts
