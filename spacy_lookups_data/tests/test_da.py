# coding: utf-8
from __future__ import unicode_literals

from spacy.lang.da import Danish
import pytest


@pytest.fixture(scope="session")
def da_nlp():
    return Danish()


@pytest.mark.parametrize(
    "string,lemma",
    [
        ("affaldsgruppernes", "affaldsgruppe"),
        ("detailhandelsstrukturernes", "detailhandelsstruktur"),
        ("kolesterols", "kolesterol"),
        ("åsyns", "åsyn"),
    ],
)
def test_da_lemmatizer_lookup_assigns(da_nlp, string, lemma):
    tokens = da_nlp(string)
    assert tokens[0].lemma_ == lemma


@pytest.mark.parametrize(
    "text,norm", [("akvarium", "akvarie"), ("bedstemoder", "bedstemor")]
)
def test_da_nlp_norm_exceptions(da_nlp, text, norm):
    tokens = da_nlp(text)
    assert tokens[0].norm_ == norm
