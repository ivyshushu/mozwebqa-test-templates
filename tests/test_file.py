#!/usr/bin/env python

from unittestzero import Assert
from pages.page_object import MySiteHomePage


class TestTemplate():

    def test_load_baseurl_and_assert_header(self, mozwebqa):
        '''
        Demo Test - Verify Header is correct on Amo Page
        '''
        home_page = MySiteHomePage(mozwebqa)
        home_page.go_to_home_page()
        Assert.equal(home_page.header_text, 'mozilla')

    def test_that_we_do_something_to_find_a_bug(self, mozwebqa):
        pass
