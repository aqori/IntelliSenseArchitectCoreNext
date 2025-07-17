# test_intellisensearchitectcorenext.py
"""
Tests for IntelliSenseArchitectCoreNext module.
"""

import unittest
from intellisensearchitectcorenext import IntelliSenseArchitectCoreNext

class TestIntelliSenseArchitectCoreNext(unittest.TestCase):
    """Test cases for IntelliSenseArchitectCoreNext class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = IntelliSenseArchitectCoreNext()
        self.assertIsInstance(instance, IntelliSenseArchitectCoreNext)
        
    def test_run_method(self):
        """Test the run method."""
        instance = IntelliSenseArchitectCoreNext()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
