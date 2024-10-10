from names import make_full_name, extract_family_name, extract_given_name

import pytest

def test_make_full_name():
  assert make_full_name("Sally", "Brown") == "Brown; Sally"
  assert make_full_name("John", "Doe") == "Doe; John"
  assert make_full_name("Mary", "Johnson") == "Johnson; Mary"
  assert make_full_name("Jane", "Smith") == "Smith; Jane"
  assert make_full_name("Michael", "Johnson") == "Johnson; Michael"
  assert make_full_name("Jean-Pierre", "Dubois") == "Dubois; Jean-Pierre"
  assert make_full_name("María José", "García López") == "García López; María José"
  assert make_full_name("", "") == "; "  

def test_extract_family_name():
  assert extract_family_name("Brown; Sally") == "Brown"
  assert extract_family_name("Doe; John") == "Doe"
  assert extract_family_name("Johnson; Mary") == "Johnson"
  assert extract_family_name("Smith; Jane") == "Smith"
  assert extract_family_name("Johnson; Michael") == "Johnson"
  assert extract_family_name("Dubois; Jean-Pierre") == "Dubois"
  assert extract_family_name("García López; María José") == "García López"
  assert extract_family_name("; ") == ""  

def test_extract_given_name():
  assert extract_given_name("Brown; Sally") == "Sally"
  assert extract_given_name("Doe; John") == "John"
  assert extract_given_name("Johnson; Mary") == "Mary"
  assert extract_given_name("Smith; Jane") == "Jane"
  assert extract_given_name("Johnson; Michael") == "Michael"
  assert extract_given_name("Dubois; Jean-Pierre") == "Jean-Pierre"
  assert extract_given_name("García López; María José") == "María José"
  assert extract_given_name("; ") == ""

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])