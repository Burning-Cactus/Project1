import unittest
import User

class AcceptanceTests(unittest.TestCase):
    {
    def test_things(self):
        self.assertEquals(CreateAccount("1, AKelly, password, Null, Null, Andrew, Kelly, 262-262-2626, 414-414-4141, 5698"),"Account successfully created.");
        user = User;
        user.permission = 1;
        user2 = User;
        user2.databaseID = 45;
        self.assertEquals(DeleteAccount(user.permission, user2.databaseID), user2.username+"'s account has been deleted.");
        user3 = User
        self.assertEquals(EditAccount(user.permission, user3), "Account has been edited.")
        self.assertEquals()
    }