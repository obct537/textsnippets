import unittest2 as unittest
import pdb

from Products.CMFCore.utils import getToolByName

from uwosh.snippets.testing import BaseTest

from uwosh.snippets.testing import \
    UWOSH_SNIPPETS_INTEGRATION_TESTING

from plone.app.testing import setRoles, login, TEST_USER_NAME

from uwosh.snippets.parser import SnippetParser


class TestSnippetParser(BaseTest):

    layer = UWOSH_SNIPPETS_INTEGRATION_TESTING

    def test_find_ids(self):
        sp = SnippetParser()
        ids = sp.findIds(self.testString)

        self.assertEqual(ids[0], self.doc.getId())

    def test_replace_ids(self):
        sp = SnippetParser()
        text = sp.replaceIds(self.testString)

        correct = "This is a meaningless test! Or is it meaningless?"

        self.assertTrue( text != '' )
        self.assertEqual(text, correct)

