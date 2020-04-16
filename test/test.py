# -*- coding: utf-8 -*-
from model.text import Text
from fixture.application import Application

def test_test(app):
    app.click_mypage_left()
    app.menu__top()
    app.group.add_text(Text(text="sss"))


def test_test_empty(app):
    app.click_mypage_left()
    app.menu__top()
    app.group.add_text(Text(text=" "))

