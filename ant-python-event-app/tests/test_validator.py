import unittest
from src.validator import validate_attendee, is_valid_registration_code

class TestValidator(unittest.TestCase):

    def test_valid_attendee(self):
        attendee = {
            "name": "Sara Palacios",
            "email": "sara@example.com",
            "age": 25,
            "ticket_type": "vip",
            "registration_code": "EV-1234"
        }
        self.assertEqual(validate_attendee(attendee), [])

    def test_invalid_email(self):
        attendee = {
            "name": "Juan",
            "email": "juanexample.com",
            "age": 20,
            "ticket_type": "general",
            "registration_code": "EV-5678"
        }
        self.assertIn("Invalid email", validate_attendee(attendee))

    def test_underage_attendee(self):
        attendee = {
            "name": "Ana",
            "email": "ana@example.com",
            "age": 16,
            "ticket_type": "student",
            "registration_code": "EV-9012"
        }
        self.assertIn("Attendee must be 18 or older", validate_attendee(attendee))
    
    def test_valid_registration_code(self):
        """Test that valid registration code passes validation"""
        attendee = {
            "name": "Carlos Ruiz",
            "email": "carlos@example.com",
            "age": 30,
            "ticket_type": "vip",
            "registration_code": "EV-1234"
        }
        errors = validate_attendee(attendee)
        self.assertNotIn("Invalid registration code format (must be EV- followed by 4 digits)", errors)
        self.assertEqual(len(errors), 0)
    
    def test_invalid_registration_code_too_short(self):
        """Test that registration code with less than 4 digits is invalid"""
        attendee = {
            "name": "Maria Lopez",
            "email": "maria@example.com",
            "age": 28,
            "ticket_type": "general",
            "registration_code": "EV-12"
        }
        self.assertIn("Invalid registration code format (must be EV- followed by 4 digits)", 
                     validate_attendee(attendee))
    
    def test_invalid_registration_code_too_long(self):
        """Test that registration code with more than 4 digits is invalid"""
        attendee = {
            "name": "Pedro Martinez",
            "email": "pedro@example.com",
            "age": 35,
            "ticket_type": "student",
            "registration_code": "EV-12345"
        }
        self.assertIn("Invalid registration code format (must be EV- followed by 4 digits)", 
                     validate_attendee(attendee))
    
    def test_invalid_registration_code_wrong_prefix(self):
        """Test that registration code without EV- prefix is invalid"""
        attendee = {
            "name": "Laura Gomez",
            "email": "laura@example.com",
            "age": 22,
            "ticket_type": "vip",
            "registration_code": "AB-1234"
        }
        self.assertIn("Invalid registration code format (must be EV- followed by 4 digits)", 
                     validate_attendee(attendee))
    
    def test_invalid_registration_code_non_numeric(self):
        """Test that registration code with non-numeric digits is invalid"""
        attendee = {
            "name": "Jorge Diaz",
            "email": "jorge@example.com",
            "age": 27,
            "ticket_type": "general",
            "registration_code": "EV-12AB"
        }
        self.assertIn("Invalid registration code format (must be EV- followed by 4 digits)", 
                     validate_attendee(attendee))
    
    def test_registration_code_optional(self):
        """Test that registration code is optional (not required)"""
        attendee = {
            "name": "Elena Torres",
            "email": "elena@example.com",
            "age": 32,
            "ticket_type": "student"
            # No registration_code provided
        }
        errors = validate_attendee(attendee)
        self.assertNotIn("Invalid registration code format (must be EV- followed by 4 digits)", errors)
        self.assertEqual(len(errors), 0)
    
    def test_is_valid_registration_code_function(self):
        """Test the standalone validation function"""
        # Valid cases
        self.assertTrue(is_valid_registration_code("EV-1234"))
        
        # Invalid cases
        self.assertFalse(is_valid_registration_code("EV-12"))
        self.assertFalse(is_valid_registration_code("EV-12345"))
        self.assertFalse(is_valid_registration_code("AB-1234"))
        self.assertFalse(is_valid_registration_code("EV-12AB"))
        self.assertFalse(is_valid_registration_code(""))
        self.assertFalse(is_valid_registration_code(None))
        self.assertFalse(is_valid_registration_code(1234))

if __name__ == "__main__":
    unittest.main()
