#! /usr/bin/env python
import os
import sys
import unittest


class TestCollection(unittest.TestCase):
    test_coll_path = "/tempZone/home/rods/test_dir"

    def setUp(self):
        from irods.session import iRODSSession
        import config

        self.sess = iRODSSession(host=config.IRODS_SERVER_HOST,
                                 port=config.IRODS_SERVER_PORT,
                                 user=config.IRODS_USER_USERNAME,
                                 password=config.IRODS_USER_PASSWORD,
                                 zone=config.IRODS_SERVER_ZONE)

        self.coll = self.sess.create_collection(self.test_coll_path)

    def tearDown(self):
        """ Delete the test collection after each test """
        self.coll.remove()

    def test_get_collection(self):
        #path = "/tempZone/home/rods"
        coll = self.sess.get_collection(self.test_coll_path)
        self.assertEquals(self.test_coll_path, coll.path)

    #def test_new_collection(self):
    #    self.assertEquals(self.coll.name, 'test_dir')

    def test_append_to_collection(self):
        """ Append a new file to the collection"""
        pass

    def test_remove_from_collection(self):
        """ Delete a file from a collection """
        pass

    def test_update_in_collection(self):
        """ Modify a file in a collection """
        pass

    def test_move_collection(self):
        new_path = "/tempZone/home/rods/test_dir_moved"
        self.coll.move(new_path)
        self.assertEquals(new_path, self.coll.path)

    #def test_delete_collection(self):
    #    pass

if __name__ == "__main__":
    # let the tests find the parent irods lib
    sys.path.insert(0, os.path.abspath('../..'))
    unittest.main()
