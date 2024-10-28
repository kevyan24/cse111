import pytest
from unittest.mock import patch
from rpsls_game import (
    scores,
    scores_for_game,
    get_player_choice,
    get_computer_choice,
    determine_winner,
    display_rules,
    update_score,
    reset_scores_for_game
)

def test_valid_choices():
    with patch('builtins.input', side_effect=['1']):
        choice = get_player_choice()
        assert choice == 'Rock✊'

    with patch('builtins.input', side_effect=['10']):
        choice = get_player_choice()
        assert choice == 'YOU CHOSE DIE\n'

    with patch('builtins.input', side_effect=['a']):
        choice = get_player_choice()
        assert choice == 'YOU CHOSE DIE\n'

def test_computer_choice_range():
    choice = get_computer_choice()
    assert choice in range(1, 6)

def test_winner_determination():
    # Test de empate
    result = determine_winner('Rock✊', 1)  
    assert result == 'tie'
    
    # Test de victoria del jugador
    result = determine_winner('Rock✊', 3)  
    assert result == 'win'
    
    # Test de derrota del jugador
    result = determine_winner('Rock✊', 2)  
    assert result == 'lose'

def test_game_rules():
    rules = display_rules()
    expected_rules = (
        'RULES\n'
        'Scissors✌️  cut Paper✋\n'
        'Paper✋ covers Rock✊\n'
        'Rock✊ crushes Lizard🦎\n'
        'Lizard🦎 poisons Spock🖖\n'
        'Spock🖖 smashes Scissors✌️\n'
        'Scissors✌️  decapitate Lizard🦎\n'
        'Lizard🦎 eats Paper✋\n'
        'Paper✋ disproves Spock🖖\n'
        'Spock🖖 vaporizes Rock✊\n'
        'And as always, Rock✊ crushes Scissors✌️.\n\n'
        '1: Rock✊\n2: Paper✋\n3: Scissors✌️\n4: Lizard🦎\n5: Spock🖖\n'
    )
    assert rules == expected_rules

def test_score_updating():
    scores['win'] = 0
    scores['lose'] = 0
    scores['tie'] = 0
    update_score('win')
    assert scores['win'] == 1
    assert scores['lose'] == 0
    assert scores['tie'] == 0

    scores_for_game['win'] = 2
    scores_for_game['lose'] = 1
    scores_for_game['tie'] = 0
    reset_scores_for_game()
    assert scores_for_game['win'] == 0
    assert scores_for_game['lose'] == 0
    assert scores_for_game['tie'] == 0

pytest.main(["-v", "--tb=line", "-rN", __file__])