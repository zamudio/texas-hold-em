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
            ('High Card', self._high_card),
            ('No Cards', self._no_cards)
        )

    def best_rank(self):
        for rank in self._hand_validation_from_best_to_worst:
            hand_name, validator_method = rank
            if validator_method():
                return hand_name

    def _royal_flush(self):
        is_straight_flush = self._straight_flush()

        # catch index error when no cards given to player
        if not is_straight_flush:
            return False

        is_royal = self.cards[-1].rank == 'Ace'
        return is_straight_flush and is_royal

    def _straight_flush(self):
        return self._straight() and self._flush()

    def _four_of_a_kind(self):
        four_of_a_kind = self._ranks_with_count(4)
        return len(four_of_a_kind) == 1

    def _full_house(self):
        return self._three_of_a_kind() and self._pair()

    def _flush(self):
        suits_that_occur_five_times = {
            suit: suit_count
            for suit, suit_count in self._card_suit_counts.items()
            if suit_count >= 5
        }

        return len(suits_that_occur_five_times) == 1

    def _straight(self):
        if len(self.cards) < 5:
            return False

        rank_index_position = [card.rank_index for card in self.cards]
        starting_rank_index = rank_index_position[0]
        last_rank_index = rank_index_position[-1]
        straight_by_index = list(
            range(starting_rank_index, last_rank_index + 1)
        )

        return rank_index_position == straight_by_index

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
        return len(self.cards) >= 2

    def _no_cards(self):
        return len(self.cards) == 0

    def _ranks_with_count(self, count):
        return {
            rank: rank_count
            for rank, rank_count in self._card_rank_counts.items()
            if rank_count == count
        }

    @property
    def _card_suit_counts(self):
        card_suit_counts = {}
        for card in self.cards:
            card_suit_counts.setdefault(card.suit, 0)
            card_suit_counts[card.suit] += 1
        return card_suit_counts

    @property
    def _card_rank_counts(self):
        card_rank_counts = {}
        for card in self.cards:
            card_rank_counts.setdefault(card.rank, 0)
            card_rank_counts[card.rank] += 1
        return card_rank_counts
