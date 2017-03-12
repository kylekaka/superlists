#!/usr/bin/env python
# coding=utf-8
from selenium import webdriver

brower = webdriver.Chrome('/home/kyle/bin/chromedriver')
brower.get('http://localhost:8000')

assert 'Django' in brower.title
