import unittest
from bs4 import BeautifulSoup
from pathlib import Path

class TestHTMLValidity(unittest.TestCase):
    def test_navbar_in_body(self):
        repo_root = Path(__file__).resolve().parent.parent
        html_files = repo_root.glob('*.html')
        for html_file in html_files:
            with open(html_file, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')
            body = soup.body
            nav = soup.find('div', class_='navbar')
            self.assertIsNotNone(body, f"{html_file.name} missing <body> tag")
            if nav is not None:
                self.assertIn(nav, body.descendants, f"Navbar not inside body in {html_file.name}")

if __name__ == '__main__':
    unittest.main()
